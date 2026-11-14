import importlib.util
from pathlib import Path
import tempfile
import unittest

PATH = Path(__file__).resolve().parents[1] / 'scripts/update.py'

class UpdateTests(unittest.TestCase):
    def test_github_release_assets_and_notes(self):
        self.assertTrue(PATH.exists(), 'collector must exist')
        spec = importlib.util.spec_from_file_location('update', PATH)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        item = {'id': 'demo', 'name': 'Demo', 'category': 'Tools', 'platforms': ['Windows'], 'homepage': 'https://example.org', 'description': 'demo', 'source': {'type': 'github', 'repo': 'owner/demo'}}
        payload = '{"tag_name":"v1","html_url":"https://github.com/owner/demo/releases/tag/v1","body":"Fixed bug","published_at":"2026-01-01","assets":[{"name":"demo.exe","browser_download_url":"https://github.com/owner/demo/releases/download/v1/demo.exe"}],"draft":false,"prerelease":false}'
        with tempfile.TemporaryDirectory() as root:
            result = m.update_one(item, Path(root), lambda url: payload)
            self.assertEqual(result['version'], 'v1')
            self.assertEqual(result['notes'], 'Fixed bug')
            self.assertEqual(len(result['downloads']), 1)
            m.render([item], Path(root))
            self.assertIn('demo.exe', (Path(root) / 'docs/software/demo.md').read_text())
            self.assertIn('demo.md', (Path(root) / 'docs/software/README.md').read_text())

class HtmlTests(unittest.TestCase):
    def test_official_page_resolves_relative_downloads(self):
        spec = importlib.util.spec_from_file_location('update', PATH)
        assert spec and spec.loader
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        item = {'id': 'official', 'name': 'Official', 'category': 'Tools', 'platforms': ['Windows'], 'homepage': 'https://example.org/', 'description': 'demo', 'source': {'type': 'html', 'url': 'https://example.org/', 'version_regex': r'Download ([0-9.]+)', 'download_regex': r'href="(?P<url>[^"]+\.exe)"', 'notes_url': 'https://example.org/history.txt'}}
        pages = {'https://example.org/': '<p>Download 2.0</p><a href="dist/tool.exe">Download</a>', 'https://example.org/history.txt': '2.0: fixed bugs'}
        with tempfile.TemporaryDirectory() as root:
            result = m.update_one(item, Path(root), pages.__getitem__)
            self.assertEqual(result['version'], '2.0')
            self.assertEqual(result['downloads'][0]['url'], 'https://example.org/dist/tool.exe')
            self.assertEqual(result['notes'], '2.0: fixed bugs')

    def test_official_source_rejects_html_challenge_as_update_notes(self):
        spec = importlib.util.spec_from_file_location('update', PATH)
        assert spec and spec.loader
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        item = {'id': 'official', 'name': 'Official', 'category': 'Tools', 'platforms': ['Windows'], 'homepage': 'https://example.org/', 'description': 'demo', 'source': {'type': 'html', 'url': 'https://example.org/', 'version_regex': r'Download ([0-9.]+)', 'download_regex': r'href="(?P<url>[^"]+\.exe)"', 'notes_url': 'https://example.org/history.txt'}}
        pages = {'https://example.org/': '<p>Download 2.0</p><a href="dist/tool.exe">Download</a>', 'https://example.org/history.txt': '<!DOCTYPE html><html><title>Just a moment</title></html>'}
        with tempfile.TemporaryDirectory() as root:
            result = m.update_one(item, Path(root), pages.__getitem__)
            self.assertTrue(result.get('error'))
            self.assertNotIn('version', result)
            m.render([item], Path(root))
            self.assertIn('失败', (Path(root) / 'docs/software/official.md').read_text())

class FailureTests(unittest.TestCase):
    def test_failed_refresh_preserves_last_success_and_reports_error(self):
        spec = importlib.util.spec_from_file_location('update', PATH)
        assert spec and spec.loader
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        item = {'id': 'demo', 'name': 'Demo', 'category': 'Tools', 'platforms': ['Windows'], 'homepage': 'https://example.org', 'description': 'demo', 'source': {'type': 'github', 'repo': 'owner/demo'}}
        good = {'tag_name': 'v1', 'html_url': 'https://github.com/owner/demo/releases/tag/v1', 'body': 'notes', 'assets': [{'name': 'demo.exe', 'browser_download_url': 'https://example.org/demo.exe'}]}
        import json
        with tempfile.TemporaryDirectory() as root:
            first = m.update_one(item, Path(root), lambda url: json.dumps(good))
            for bad in [dict(good, prerelease=True), dict(good, draft=True), dict(good, assets=[]), dict(good, tag_name=''), dict(good, assets=[{'name': 'bad', 'browser_download_url': 'http://example.org/bad'}])]:
                result = m.update_one(item, Path(root), lambda url: json.dumps(bad))
                self.assertTrue(result.get('error'), bad)
                self.assertEqual(result['version'], 'v1')
                self.assertEqual(result['notes'], 'notes')
                self.assertEqual(result['checked_at'], first['checked_at'])
            def fail(url):
                raise OSError('connection failed')
            result = m.update_one(item, Path(root), fail)
            self.assertIn('connection failed', result['error'])
            m.render([item], Path(root))
            self.assertIn('失败', (Path(root) / 'docs/software/demo.md').read_text())

class CatalogTests(unittest.TestCase):
    def test_rejects_unsafe_or_ambiguous_configuration(self):
        spec = importlib.util.spec_from_file_location('update', PATH)
        assert spec and spec.loader
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        import json
        item = {'id': 'demo', 'name': 'Demo', 'category': 'Tools', 'platforms': ['Windows'], 'homepage': 'https://example.org/', 'description': 'demo', 'source': {'type': 'github', 'repo': 'owner/demo'}}
        cases = [[dict(item, id='../escape')], [item, item], [dict(item, homepage='http://example.org')], [dict(item, source={'type': 'unknown'})], [dict(item, source={'type': 'github', 'repo': 'owner/repo/extra'})], [dict(item, platforms=[])]]
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / 'catalog.json'
            path.write_text(json.dumps({'software': [item]}))
            self.assertEqual(m.load_catalog(path)[0]['id'], 'demo')
            for case in cases:
                path.write_text(json.dumps({'software': case}))
                with self.assertRaises(ValueError, msg=str(case)):
                    m.load_catalog(path)

class CliTests(unittest.TestCase):
    def test_offline_cli_renders_missing_snapshot_without_network(self):
        import json
        import subprocess
        item = {'id': 'demo', 'name': 'Demo', 'category': 'Tools', 'platforms': ['Windows'], 'homepage': 'https://example.org/', 'description': 'demo', 'source': {'type': 'github', 'repo': 'owner/demo'}}
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / 'catalog.json'
            path.write_text(json.dumps({'software': [item]}))
            result = subprocess.run(['python3', str(PATH), '--catalog', str(path), '--root', root, '--render-only'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            page = Path(root) / 'docs/software/demo.md'
            self.assertTrue(page.exists())
            first = page.read_text()
            self.assertIn('尚未', first)
            subprocess.run(['python3', str(PATH), '--catalog', str(path), '--root', root, '--render-only'], check=True, capture_output=True)
            self.assertEqual(page.read_text(), first)

class NetworkTests(unittest.TestCase):
    def test_fetch_retries_and_only_authenticates_github_api(self):
        from unittest.mock import patch
        import io
        spec = importlib.util.spec_from_file_location('update', PATH)
        assert spec and spec.loader
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        with patch.dict('os.environ', {'GITHUB_TOKEN': 'test-secret'}):
            with patch.object(m, 'open_request', side_effect=[OSError('retry'), io.BytesIO(b'ok')]) as opening, patch('time.sleep'):
                self.assertEqual(m.fetch_text('https://api.github.com/repos/o/r/releases/latest'), 'ok')
                self.assertEqual(opening.call_count, 2)
                request = opening.call_args[0][0]
                self.assertEqual(request.get_header('Authorization'), 'Bearer test-secret')
            with patch.object(m, 'open_request', return_value=io.BytesIO(b'official')) as opening:
                self.assertEqual(m.fetch_text('https://example.org/'), 'official')
                self.assertIsNone(opening.call_args[0][0].get_header('Authorization'))
            with self.assertRaises(ValueError):
                m.fetch_text('http://example.org/')

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Collect official software metadata and render a Markdown catalog (Python 3.9+)."""
import json
import re
from urllib.parse import urljoin, urlparse
from pathlib import Path


def load_catalog(path):
    catalog = json.loads(path.read_text(encoding='utf-8'))
    items = catalog.get('software')
    if not isinstance(items, list) or not items:
        raise ValueError('software must be a nonempty list')
    seen = set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError('Each software entry must be an object')
        identifier = item.get('id', '')
        if not isinstance(identifier, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identifier) or identifier in seen or identifier == 'readme':
            raise ValueError('Invalid, reserved or duplicate software id')
        seen.add(identifier)
        for key in ('name', 'category', 'description', 'homepage'):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError('Missing text field: ' + key)
        if not isinstance(item.get('platforms'), list) or not item['platforms'] or any(not isinstance(p, str) or not p.strip() for p in item['platforms']):
            raise ValueError('platforms must be a nonempty list of strings')
        https_url(item['homepage'])
        source = item.get('source', {})
        if not isinstance(source, dict):
            raise ValueError('source must be an object')
        if source.get('type') == 'github':
            if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', source.get('repo', '')):
                raise ValueError('GitHub repo must be owner/name')
        elif source.get('type') == 'html':
            for key in ('url', 'notes_url'):
                https_url(source.get(key, ''))
            try:
                version = re.compile(source['version_regex'])
                downloads = re.compile(source['download_regex'])
            except (KeyError, re.error, TypeError) as exc:
                raise ValueError('Invalid website extraction regex') from exc
            if version.groups < 1 or 'url' not in downloads.groupindex:
                raise ValueError('Version needs a capture group; download needs named url group')
        else:
            raise ValueError('Unsupported source type')
    return items


def collect(item, root, fetch):
    source = item['source']
    if source['type'] == 'html':
        page = fetch(source['url'])
        version_match = re.search(source['version_regex'], page)
        if not version_match:
            raise ValueError('Official page did not match version_regex')
        version = version_match.group(1)
        downloads = []
        for match in re.finditer(source['download_regex'], page):
            url = urljoin(source['url'], match.group('url'))
            downloads.append({'name': urlparse(url).path.rsplit('/', 1)[-1], 'url': url})
        notes = fetch(source['notes_url'])
        if not notes.strip() or re.search(r'<(?:!doctype|html|head|body)\b', notes, re.IGNORECASE):
            raise ValueError('Expected official plain-text changelog, received empty text or HTML')
        result = {'version': version, 'notes': notes, 'source_url': source['url'], 'published_at': None, 'downloads': downloads}
    else:
        payload = json.loads(fetch('https://api.github.com/repos/' + source['repo'] + '/releases/latest'))
        if payload.get('prerelease') or payload.get('draft'):
            raise ValueError('Upstream did not return a stable published release')
        result = {'version': payload['tag_name'], 'notes': payload.get('body') or '',
                  'source_url': payload['html_url'], 'published_at': payload.get('published_at'),
                  'downloads': [{'name': a['name'], 'url': a['browser_download_url']} for a in payload['assets']]}
    if not result['version'] or not result['downloads']:
        raise ValueError('Missing version or downloadable release assets')
    for download in result['downloads']:
        https_url(download['url'])
    https_url(result['source_url'])
    return result


def https_url(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password or any(c.isspace() for c in url):
        raise ValueError('Only HTTPS URLs without embedded credentials are allowed')
    return url


def update_one(item, root, fetch):
    from datetime import datetime, timezone
    path = root / 'data' / (item['id'] + '.json')
    previous = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    try:
        result = collect(item, root, fetch)
        result.update(checked_at=now, last_attempt=now, error=None)
    except Exception as exc:
        result = dict(previous)
        result.update(last_attempt=now, error=type(exc).__name__ + ': ' + str(exc))
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)
    return result


def render(items, root):
    import html
    from urllib.parse import quote
    def text(value):
        return html.escape(str(value), quote=False).replace('|', '&#124;').replace('\n', ' ').replace('[', '&#91;').replace(']', '&#93;')
    def link_url(value):
        return quote(https_url(value), safe=':/?#@!$&*+,;=%~_-')
    directory = root / 'docs/software'
    directory.mkdir(parents=True, exist_ok=True)
    index = ['# 软件目录', '', '[返回首页](../../README.md)', '', '版本为最近成功检查时的上游稳定版本，失败时保留旧数据。时间采用 UTC。', '', '| 软件 | 分类 | 平台 | 版本 | 状态 | 最近成功检查 |', '| --- | --- | --- | --- | --- | --- |']
    for item in items:
        path = root / 'data' / (item['id'] + '.json')
        result = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
        status = '失败（旧数据，仅供参考）' if result.get('error') else ('正常' if result.get('checked_at') else '尚未采集')
        version = result.get('version', '尚未获取')
        checked = result.get('checked_at', '尚未成功检查')
        lines = ['# ' + text(item['name']), '', '[软件目录](README.md) · [首页](../../README.md)', '', text(item['description']), '', '- 分类：' + text(item['category']), '- 平台：' + text(' / '.join(item['platforms'])), '- 官网：<' + link_url(item['homepage']) + '>', '- 版本：' + text(version), '- 状态：' + status, '- 最近成功检查（UTC）：' + text(checked), '- 最近尝试（UTC）：' + text(result.get('last_attempt', '尚未尝试')), '- 上游发布时间：' + text(result.get('published_at') or '上游未提供'), '']
        if result.get('source_url'):
            lines += ['上游发布/下载页：<' + link_url(result['source_url']) + '>', '']
        if result.get('error'):
            lines += ['> 采集失败：' + text(result['error']), '']
        lines += ['## 官方下载', '', '按文件名核对系统、架构和安装类型，下载前核对上游签名或校验值。', '']
        lines += ['- [' + text(d['name']) + '](' + link_url(d['url']) + ')' for d in result.get('downloads', [])]
        if not result.get('downloads'):
            lines += ['尚未获取下载链接；请前往官网。']
        notes = '\n'.join(line.rstrip() for line in (result.get('notes') or '上游未提供更新说明，或尚未成功采集。').splitlines())
        fence = '`' * max(3, max((len(s) + 1 for s in re.findall(r'`+', notes)), default=3))
        lines += ['', '## 上游更新说明（原文）', '', '以下为上游原文的纯文本展示；官网来源可能提供完整历史日志，不仅当前版本。', '', fence + 'text', notes, fence, '']
        (directory / (item['id'] + '.md')).write_text('\n'.join(lines), encoding='utf-8')
        index.append('| [' + text(item['name']) + '](' + item['id'] + '.md) | ' + text(item['category']) + ' | ' + text(' / '.join(item['platforms'])) + ' | ' + text(version) + ' | ' + status + ' | ' + text(checked) + ' |')
    (directory / 'README.md').write_text('\n'.join(index) + '\n', encoding='utf-8')


def open_request(request):
    from urllib.request import build_opener, HTTPRedirectHandler
    class SafeRedirect(HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            https_url(newurl)
            redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
            if redirected is not None:
                redirected.remove_header('Authorization')
            return redirected
    return build_opener(SafeRedirect()).open(request, timeout=30)


def fetch_text(url):
    import os
    import time
    from urllib.request import Request
    https_url(url)
    headers = {'User-Agent': 'setup-toolbox/1.0 (+https://github.com/dickz922/setup-toolbox)'}
    if urlparse(url).hostname == 'api.github.com':
        headers.update({'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'})
        token = os.environ.get('GITHUB_TOKEN')
        if token:
            headers['Authorization'] = 'Bearer ' + token
    last_error = None
    for attempt in range(3):
        try:
            with open_request(Request(url, headers=headers)) as response:
                body = response.read(8 * 1024 * 1024 + 1)
                if len(body) > 8 * 1024 * 1024:
                    raise ValueError('Upstream metadata exceeds 8 MiB')
                return body.decode('utf-8-sig')
        except OSError as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise OSError('Failed after 3 attempts: ' + str(last_error))


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, default=Path('catalog.json'))
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--render-only', action='store_true')
    parser.add_argument('--strict', action='store_true', help='Explicit failure-on-error (also the default)')
    args = parser.parse_args(argv)
    items = load_catalog(args.catalog)
    failed = False
    if not args.render_only:
        for item in items:
            result = update_one(item, args.root, fetch_text)
            failed = failed or bool(result.get('error'))
            print(item['id'] + ': ' + (result.get('error') or result.get('version', 'unknown')))
    render(items, args.root)
    return 1 if failed else 0


if __name__ == '__main__':
    import sys
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('Error: ' + str(exc), file=sys.stderr)
        sys.exit(2)

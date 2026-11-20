# Microsoft PowerToys

[软件目录](README.md) · [首页](../../README.md)

微软开源效率工具集：窗口布局、快捷启动、批量重命名等。

- 分类：系统增强
- 平台：Windows
- 官网：<https://learn.microsoft.com/windows/powertoys/>
- 版本：v0.102.3101
- 状态：正常
- 最近成功检查（UTC）：2026-11-20T08:30:44+00:00
- 最近尝试（UTC）：2026-11-20T08:30:44+00:00
- 上游发布时间：2026-11-06T09:54:30Z

上游发布/下载页：<https://github.com/microsoft/PowerToys/releases/tag/v0.102.3101>

## 官方下载

按文件名核对系统、架构和安装类型，下载前核对上游签名或校验值。

- [GroupPolicyObjectFiles-0.102.3101.0.zip](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/GroupPolicyObjectFiles-0.102.3101.0.zip)
- [PowerToysSetup-0.102.3101.0-arm64.exe](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysSetup-0.102.3101.0-arm64.exe)
- [PowerToysSetup-0.102.3101.0-x64.exe](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysSetup-0.102.3101.0-x64.exe)
- [PowerToysUserSetup-0.102.3101.0-arm64.exe](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysUserSetup-0.102.3101.0-arm64.exe)
- [PowerToysUserSetup-0.102.3101.0-x64.exe](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysUserSetup-0.102.3101.0-x64.exe)
- [symbols-arm64.zip](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/symbols-arm64.zip)
- [symbols-x64.zip](https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/symbols-x64.zip)

## 上游更新说明（原文）

以下为上游原文的纯文本展示；官网来源可能提供完整历史日志，不仅当前版本。

```text
# Release v0.102.3101.0

This hotfix release improves File Explorer thumbnail generation, fixes Mouse Without Borders pairing failures, and restores optional diagnostic event reporting. See the [v0.102.2933.0 release notes](https://github.com/microsoft/PowerToys/releases/tag/v0.102.2933.0) for the full list of changes in PowerToys v0.102.

## Installer Hashes

| Description | Filename | SHA256 |
| --- | --- | --- |
| Per user - x64 | [PowerToysUserSetup-0.102.3101.0-x64.exe][ptUserX64] | `4B4C49A31E8B7E6A36647CCD3033ACB0AD56C306595A9409E59865C3C27D1CF2` |
| Per user - ARM64 | [PowerToysUserSetup-0.102.3101.0-arm64.exe][ptUserArm64] | `E80D5E784173101BBB4BD95EDE66CF1974C230CA81EBEB16FEBA25FDD5FFCE87` |
| Machine wide - x64 | [PowerToysSetup-0.102.3101.0-x64.exe][ptMachineX64] | `F1D24A49346167322EB64A2458BD82810519920D1DA4C0AEB1788E54C345D142` |
| Machine wide - ARM64 | [PowerToysSetup-0.102.3101.0-arm64.exe][ptMachineArm64] | `65663AFB8FA77B4DB257BC9494F66AC91A2B063AE0BFE2CD85E9DE958C92EE8B` |

## Highlights

This patch addresses three areas since the previous stable release.

### File Explorer

- Improved handling of stalled thumbnail renderers, isolated concurrent SVG requests, and preserved supported SVG formatting and UTF-8 STL names, in [#49950](https://github.com/microsoft/PowerToys/pull/49950).

### General

- Updated telemetry to version 2.0.5 and restored optional diagnostic event reporting from native and managed components, without changing diagnostic-data preferences, in [#51896](https://github.com/microsoft/PowerToys/pull/51896) and [#51940](https://github.com/microsoft/PowerToys/pull/51940).

### Mouse Without Borders

- Fixed Mouse Without Borders pairing failures that could show an untrusted-signature error in signed PowerToys builds, in [#51789](https://github.com/microsoft/PowerToys/pull/51789) by [@mvanhorn](https://github.com/mvanhorn).

[ptUserX64]: https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysUserSetup-0.102.3101.0-x64.exe
[ptUserArm64]: https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysUserSetup-0.102.3101.0-arm64.exe
[ptMachineX64]: https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysSetup-0.102.3101.0-x64.exe
[ptMachineArm64]: https://github.com/microsoft/PowerToys/releases/download/v0.102.3101/PowerToysSetup-0.102.3101.0-arm64.exe
```

# LocalSend

[软件目录](README.md) · [首页](../../README.md)

跨平台局域网文件传输工具；移动平台可能需通过官方应用商店安装。

- 分类：文件传输
- 平台：Windows / macOS / Linux / Android / iOS
- 官网：<https://localsend.org/>
- 版本：v1.18.2
- 状态：正常
- 最近成功检查（UTC）：2026-11-20T08:30:44+00:00
- 最近尝试（UTC）：2026-11-20T08:30:44+00:00
- 上游发布时间：2026-08-21T14:02:01Z

上游发布/下载页：<https://github.com/localsend/localsend/releases/tag/v1.18.2>

## 官方下载

按文件名核对系统、架构和安装类型，下载前核对上游签名或校验值。

- [LocalSend-1.18.2-android-arm32v7.apk](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-android-arm32v7.apk)
- [LocalSend-1.18.2-android-arm64v8.apk](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-android-arm64v8.apk)
- [LocalSend-1.18.2-android-google-play.apk](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-android-google-play.apk)
- [LocalSend-1.18.2-android-x64.apk](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-android-x64.apk)
- [LocalSend-1.18.2-linux-arm-64.deb](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-linux-arm-64.deb)
- [LocalSend-1.18.2-linux-arm-64.tar.gz](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-linux-arm-64.tar.gz)
- [LocalSend-1.18.2-linux-x86-64.AppImage](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-linux-x86-64.AppImage)
- [LocalSend-1.18.2-linux-x86-64.deb](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-linux-x86-64.deb)
- [LocalSend-1.18.2-linux-x86-64.tar.gz](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-linux-x86-64.tar.gz)
- [LocalSend-1.18.2-windows-arm-64.zip](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-windows-arm-64.zip)
- [LocalSend-1.18.2-windows-x86-64-unsigned.exe](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-windows-x86-64-unsigned.exe)
- [LocalSend-1.18.2-windows-x86-64.exe](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-windows-x86-64.exe)
- [LocalSend-1.18.2-windows-x86-64.zip](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-windows-x86-64.zip)
- [LocalSend-1.18.2.dmg](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2.dmg)
- [LocalSend-CLI-1.18.2-linux-arm-64.tar.gz](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-CLI-1.18.2-linux-arm-64.tar.gz)
- [LocalSend-CLI-1.18.2-linux-x86-64.tar.gz](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-CLI-1.18.2-linux-x86-64.tar.gz)
- [LocalSend-CLI-1.18.2-macos-arm-64.tar.gz](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-CLI-1.18.2-macos-arm-64.tar.gz)
- [LocalSend-CLI-1.18.2-macos-x86-64.tar.gz](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-CLI-1.18.2-macos-x86-64.tar.gz)
- [LocalSend-CLI-1.18.2-windows-arm-64.exe](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-CLI-1.18.2-windows-arm-64.exe)
- [LocalSend-CLI-1.18.2-windows-x86-64.exe](https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-CLI-1.18.2-windows-x86-64.exe)

## 上游更新说明（原文）

以下为上游原文的纯文本展示；官网来源可能提供完整历史日志，不仅当前版本。

```text
This release fixes compatibility issues with 1.17.0 and earlier.
Note: The Windows binaries have been updated to include a signature.

- feat: drag and drop files into the "Receive via link" browser page
- feat(desktop): allow customizing the web share pages by placing HTML files in a `web` folder next to the executable
- feat(cli): add version info to the Windows executable
- feat(linux): set actual version in the AppImage
- security: do not follow HTTP redirects sent by peers
- fix: restore compatibility with 1.17.0 and earlier versions on missing multicast networks
- fix: devices running 1.17.0 and earlier could not add 1.18.0+ device as favorite
- fix: ignore proxies, fixes "TLS info not found" when a system proxy (e.g. Shadowrocket) is enabled
- fix: automatically restart the HTTP / multicast server when it dies or when the app resumes
- fix: drag and drop with a mix of folders and files
- fix: during transfer, add bottom padding when Advanced is open (@Chethan616)
- fix: do not crash at startup when the executable path cannot be resolved (@Shlomo116)
- fix(android): ignore unknown or invalid file modification times when reading files
- i18n: add Armenian
```

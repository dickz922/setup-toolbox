# Ventoy

[软件目录](README.md) · [首页](../../README.md)

多镜像启动 U 盘工具。首次安装会涉及磁盘分区和格式化，操作前务必备份。

- 分类：装机与启动
- 平台：Windows / Linux
- 官网：<https://www.ventoy.net/>
- 版本：v1.1.18
- 状态：正常
- 最近成功检查（UTC）：2026-11-17T09:11:16+00:00
- 最近尝试（UTC）：2026-11-17T09:11:16+00:00
- 上游发布时间：2026-10-09T05:20:45Z

上游发布/下载页：<https://github.com/ventoy/Ventoy/releases/tag/v1.1.18>

## 官方下载

按文件名核对系统、架构和安装类型，下载前核对上游签名或校验值。

- [sha256.txt](https://github.com/ventoy/Ventoy/releases/download/v1.1.18/sha256.txt)
- [ventoy-1.1.18-linux.tar.gz](https://github.com/ventoy/Ventoy/releases/download/v1.1.18/ventoy-1.1.18-linux.tar.gz)
- [ventoy-1.1.18-livecd.iso](https://github.com/ventoy/Ventoy/releases/download/v1.1.18/ventoy-1.1.18-livecd.iso)
- [ventoy-1.1.18-windows.zip](https://github.com/ventoy/Ventoy/releases/download/v1.1.18/ventoy-1.1.18-windows.zip)

## 上游更新说明（原文）

以下为上游原文的纯文本展示；官网来源可能提供完整历史日志，不仅当前版本。

````text
**Changelog**
1. Experimental support for SteamOS recovery images. (#3712 #2875 #1815)
2. Improve the Linux remount feature to make the ISO partition mountable out of the box on mainstream desktop distros. ([Notes](https://www.ventoy.net/en/doc_linux_remount.html))
3. Suppress the duplicate disk icons in the sidebar on some Linux desktop distros.
4. Change the ISO partition dm name to stable /dev/mapper/VentoyPart, please refer [Notes](https://www.ventoy.net/en/doc_linux_remount.html)
5. Make the ISO partition mountable for CloneZilla. (#3274)
6. Fix Fedora 45 beta boot issue.
7. Fix the Windows/WinPE secure boot version check failed issue.
8. Fix Persistence intermittently fails on Ubuntu desktop. (#3718)
9. Fix the boot issue for Grml 2026.09. (#3751)
10. Add support for custom Syslinux-based ISO. (#3760)
11. Improvement for latest LinuxConsole release. (#3745)
12. Add check for Boot Conf Replace entries in VentoyPlugson. (#3727 #3593)


**SHA256**
```
d86ff9de63d94c8b8f1f6b14d23c55af4b88e8207bf2893890892a6a97b1ad54  ventoy-1.1.18-linux.tar.gz
ee3917bd5a9973c0b2f8f3ef85048bf68ae089ec88f5561ad78b6ad308b51ab5  ventoy-1.1.18-livecd.iso
082c478e8c432e1ac653899fcf50e3a4077a2851bc6112b5ddd30545962164a9  ventoy-1.1.18-windows.zip
```

<br><br><br><br>
------------------------------------------------------------------------------------------------------------------------
Wana boot and install OS through network (PXE/HTTPBoot)? Welcome to my new project iVentoy.

About iVentoy https://www.iventoy.com/
iVentoy is an enhanced version of the PXE/HTTPBoot server with .
Extremely easy to use, Many advanced features.
x86 Legacy BIOS, IA32 UEFI, x86_64 UEFI (Secure Boot), ARM64 UEFI and LoongArch64 UEFI mode supported
110+ common types of OS supported (Windows/WinPE/Linux/Unix/VMware)
Turn any PC, laptop, server, NAS, or Raspberry Pi into a PXE/HTTPBoot server instantly!
......



[![Download Ventoy](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/ventoy/files/v1.1.18/)
````

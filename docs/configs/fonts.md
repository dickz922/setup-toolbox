# 字体安装与终端/编辑器配置

[返回配置目录](README.md) · [软件与版本目录](../software/README.md)

收录 Fira Code、Iosevka、Hack、朱雀仿宋。版本、上游下载链接和更新说明由软件详情页自动维护；本页人工维护安装与配置方法，不在用户设备上自动执行。

## 字体选择

| 字体 | 用途 | 最新版本与下载 |
| --- | --- | --- |
| Fira Code | 编程等宽字体，支持编程连字 | [详情](../software/fira-code.md) |
| Iosevka | 窄体编程字体，提供多个家族和变体 | [详情](../software/iosevka.md) |
| Hack | 源代码阅读的等宽字体 | [详情](../software/hack.md) |
| 朱雀仿宋 | 中文正文排版，非等宽编程字体 | [详情](../software/zhuque.md) |

朱雀仿宋当前条目显式允许采集上游预发行版，页面会标注“预发行版”。重要排版任务先测试缺字、标点和导出效果，不将其误认为正式稳定版。

## macOS：Homebrew 安装

前提：已安装并能正常使用 Homebrew。以下命令仅作为使用说明，不会由采集器执行。

用户提供的原始命令（原样保留）：

```sh
brew install font-fira-code
brew install --cask font-iosevka
```

经 Homebrew 官方 Cask API 核验，这两项均为 Cask。推荐显式指定类型，表达更清楚；不表示上面的 Fira Code 原始命令一定不能被 Homebrew 自动识别：

```sh
brew install --cask font-fira-code
brew install --cask font-iosevka
```

安装前如需检查当前包信息：

```sh
brew info --cask font-fira-code
brew info --cask font-iosevka
```

包管理器版本可能落后于上游 Releases；软件详情页跟踪的是 GitHub 上游版本，不冒充 Homebrew 已同步。

参考：[Fira Code Cask](https://formulae.brew.sh/cask/font-fira-code) · [Iosevka Cask](https://formulae.brew.sh/cask/font-iosevka)

## 通用：从 GitHub 发布包安装

1. 通过上方详情页前往上游下载。优先选择桌面字体包，不要误装网页 Webfonts 或源码包。
2. 解压后检查 `.ttf`、`.otf`、`.ttc` 等字体文件。Iosevka 的变体很多，不必一次安装全部；具体格式兼容性以系统为准。
3. macOS：用“字体册”打开字体并验证，优先安装到当前用户，不覆盖不相关字体。
4. Windows：选择所需字体文件，右键“安装”；非必要不使用“为所有用户安装”。
5. Linux：按发行版字体管理方式安装。常见做法是将字体放在当前用户的 `~/.local/share/fonts/`，系统有 fontconfig 时运行 `fc-cache -f` 刷新。
6. 重启终端或编辑器，在字体列表中选择刚安装的字体。文件名与字体内部家族名可能不同，以应用实际显示为准。

## VS Code 配置示例

修改前备份现有用户设置，只合并需要的字段，不要覆盖整个 `settings.json`：

```json
{
  "editor.fontFamily": "'Fira Code', 'Iosevka', 'Hack', monospace",
  "editor.fontLigatures": true,
  "terminal.integrated.fontFamily": "'Iosevka', 'Hack', monospace"
}
```

这些字体按从左到右的顺序回退，并非同时生效；不同变体的内部家族名可能不同。连字需要字体和应用同时支持；终端中的连字显示还取决于终端实现。朱雀仿宋不应作为终端主字体。

## electerm 与远程桌面注意事项

- electerm：在设置中选择已安装的等宽字体，测试中英文混排、光标对齐和特殊符号；不要直接向配置文件写入未经核实的字段。
- 原始项目地址为 `http://github.com/electerm/electerm`；采集使用同一仓库的 HTTPS 地址 `https://github.com/electerm/electerm`。
- Notepad++ 原生面向 Windows，本仓库不会将其标成 macOS 原生应用。
- RustDesk：远程连接不代表字体同步安装；远程应用需要字体时，应在实际运行该应用的系统中安装。不要把设备 ID、访问密码或服务器密钥提交到公开仓库。

## 验证与撤销

在编辑器输入 `0 O 1 l I -> != === 中文标点，。` 检查易混淆字符、连字与中文回退。保存 PDF 后重新打开，检查字体嵌入与缺字情况。

如显示异常，先恢复原来的应用字体配置，再通过字体管理器停用本次安装的字体。Homebrew 安装的字体可按需卸载：

```sh
brew uninstall --cask font-fira-code
brew uninstall --cask font-iosevka
```

仅卸载确认不再需要的字体；不要批量删除系统字体。以上安装与配置步骤是操作指南，未在本机执行安装验证。

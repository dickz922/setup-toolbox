# 装机工具箱 · Setup Toolbox

收集可靠的装机软件、实用技巧与配置方法，以 GitHub Markdown 展示，自动追踪上游稳定版。

[软件与最新版本](docs/software/README.md) · [装机检查清单](docs/guides/setup-checklist.md) · [配置方法](docs/configs/README.md) · [如何添加软件](CONTRIBUTING.md)

## 能做什么

- **GitHub 来源**：通过官方 Releases API 获取最新稳定版、发布资产和原文更新说明，不将测试版当稳定版。
- **官网来源**：按每个站点的解析规则获取版本和官方下载链接，读取指定官方更新日志。首例为 7-Zip。
- **自动维护**：GitHub Actions 每日北京时间 09:17 左右检查，也支持 Actions 页面手动运行。定时任务可能延迟，不保证准点。
- **Markdown 展示**：每个软件有独立页面，总目录提供分类、平台、版本、来源和采集状态。
- **人工知识库**：技巧和配置指南独立保存，自动采集不会改写。
- **失败保护**：失败保留上次成功数据并标注错误，工作流报告失败，避免把旧版本伪装成最新版本。

## 首批软件

| 软件 | 来源 | 主要用途 |
| --- | --- | --- |
| [7-Zip](docs/software/7zip.md) | 官网 | Windows 压缩工具；目前采集 x64 安装包 |
| [PowerToys](docs/software/powertoys.md) | GitHub | Windows 效率工具 |
| [LocalSend](docs/software/localsend.md) | GitHub | 跨平台局域网传输 |
| [Ventoy](docs/software/ventoy.md) | GitHub | 多镜像启动 U 盘 |

## 本地使用

需要 Python 3.9+，仅使用标准库，无付费 API 或依赖服务。

```sh
python3 -m unittest discover -s tests -v
python3 scripts/update.py --catalog catalog.json --root . --strict
# 不联网，仅根据已有快照重新生成 Markdown
python3 scripts/update.py --catalog catalog.json --root . --render-only
```

可选环境变量 `GITHUB_TOKEN` 可提升 API 限额；GitHub Actions 自动使用内置令牌。不要把令牌写入文件或提交仓库。

## 目录

```text
catalog.json          软件定义与采集规则（人工维护）
scripts/              采集器与 Markdown 生成器
tests/                自动测试
data/                 实际采集结果和状态（自动维护）
docs/software/        软件总目录和详情页（自动生成）
docs/guides/          装机与实用技巧（人工维护）
docs/configs/         配置方法（人工维护）
.github/workflows/    测试、定时更新和手动更新
```

## 设计边界与安全

1. 只索引上游地址，不托管安装包、不破解、不自动安装软件。
2. “最新版”表示**最近一次成功检查时，上游标记的稳定发布版**；以页面检查时间和上游发布页为准。API 的 latest 语义由上游决定，并非自行比较版本号。
3. 官网页面千差万别，没有可靠的万能抓取器。新增官网需要设置并测试专用解析规则；网页改版、反爬、限流都可能造成失败。
4. 更新说明保留上游原文，不进行未经验证的摘要或翻译。官网示例展示官方完整历史日志，不冒充只属于当前版本的说明。
5. 下载前核对架构、系统版本、数字签名与上游校验值。收录不代表安全背书。
6. 公开仓库不得提交密码、私网地址、个人信息或真实业务配置。所有教程仅提供通用示例。
7. Actions 提交仅限 `data/` 和 `docs/software/`。默认分支如启用禁止直接推送的保护规则，需改为 PR 更新方式。
8. GitHub 定时工作流在公开仓库长期无活动时可能被平台停用；请关注 Actions 状态。未来私有化时需自行检查 Actions 额度。

## 许可

项目原创代码和文档采用 [MIT](LICENSE)。抓取的更新说明、软件名称及安装包属于各自权利人，项目许可证不覆盖第三方内容。

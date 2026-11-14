# 添加软件与知识条目

## GitHub 托管的软件

在 `catalog.json` 的 `software` 数组中添加对象：

```json
{
  "id": "example-tool",
  "name": "示例工具",
  "category": "系统工具",
  "platforms": ["Windows", "macOS", "Linux"],
  "homepage": "https://example.org/",
  "description": "说明用途和注意事项。",
  "source": {"type": "github", "repo": "owner/repo"}
}
```

必须填写真实上游仓库，不要照抄占位符。`id` 使用小写字母、数字与连字符并保持唯一。上游须使用 GitHub Releases 并发布可下载资产；仅发布 tag 或源码的仓库不一定适合此适配器。

## 官网来源

参考 `catalog.json` 中 7-Zip 条目：

- `source.type`: `html`。
- `source.url`: 官方下载页 HTTPS 地址。
- `source.version_regex`: 第一个捕获组是版本号。
- `source.download_regex`: 命名组 `(?P<url>...)` 捕获下载地址，支持相对地址。
- `source.notes_url`: 官方纯文本更新日志地址。HTML 格式的日志应开发专用适配器，不要把网页源码当正文。

官网下载按钮有时指向 GitHub，这是正常的；来源表示**在哪里查找版本和链接**，不限制上游使用的分发渠道。只匹配当前版本的目标安装包，不要混入历史版本。不要用“猜版本号拼接 URL”代替真实采集。

## 验证后提交

```sh
python3 -m unittest discover -s tests -v
python3 scripts/update.py --catalog catalog.json --root . --strict
```

检查 `data/<id>.json`、`docs/software/<id>.md` 与总目录，确认版本、下载地址、更新说明、状态准确。不要手工编辑生成页面。需要移除软件时先修改清单，再确认并手动清理旧生成文件；生成器不会擅自删除历史文件。

## 技巧和配置

- 装机步骤和经验：`docs/guides/`。
- 配置方法和通用片段：`docs/configs/`。
- 写清适用平台、前提、操作、验证、撤销办法和风险。
- 涉及删除、格式化、权限变更时明确警告，不提供默认自动执行的危险脚本。
- 提交前清理令牌、账号、设备标识和真实网络信息。

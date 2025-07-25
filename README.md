<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-llm-helper

_✨ 一个支持多平台的帮助插件，基于 LLM 解析 Github 仓库或代码。 ✨_

</div>

## 📖 介绍

LLM-Helper 是一个智能的 NoneBot2 帮助插件，它利用大语言模型（LLM）自动分析插件代码和文档，为用户提供详细的插件使用说明。该插件能够：

- 🔍 **智能解析**：自动扫描并分析所有已安装的插件。
- 🤖 **AI 生成**：使用 LLM 解析插件代码和 README 文档。
- 📚 **详细帮助**：生成包含命令、参数、用法示例的完整帮助文档。
- 🔄 **实时更新**：支持重新生成插件的帮助文档。
- 🔎 **智能搜索**：支持按关键词搜索插件和命令。

## ✨ 特性

- **自动发现**：启动时自动扫描所有用户插件。
- **智能缓存**：缓存生成的帮助文档，提高响应速度。
- **多平台支持**：支持所有 NoneBot2 适配器。
- **灵活配置**：支持 OpenAi 兼容格式，支持大多数的模型。
- **错误重试**：内置重试机制，提高稳定性。

> [!TIP]
> 本插件所生成的帮助文档很大程度上依赖于 LLM 的能力，故所生成的内容仅供参考。

## 💿 安装

### 使用 nb-cli 安装

```bash
nb plugin install nonebot-plugin-llm-helper
```

## ⚙️ 配置

在 NoneBot2 项目的 `.env` 文件中添加以下配置：


| 配置项 | 必填 | 默认值 | 说明 |
|:------:|:----:|:------:|:----:|
| `llm_helper_api_key` | 是 | 无 | LLM API 密钥 |
| `llm_helper_model` | 是 | 无 | 使用的 LLM 模型名称 |
| `llm_helper_base_url` | 否 | 无 | LLM API 基础地址 |
| `github_proxy` | 否 | `https://gh-proxy.com/` | GitHub 代理地址 |
| `llm_helper_timeout` | 否 | `600` | LLM 请求超时时间（秒） |
| `llm_helper_max_retries` | 否 | `3` | 最大重试次数 |
| `llm_helper_retry_delay` | 否 | `10` | 重试间隔时间（秒） |

### 配置示例

```env
# OpenAi Api 兼容配置
llm_helper_api_key=your_api_key_here
llm_helper_model=deepseek-chat
llm_helper_base_url=https://api.deepseek.com

# 网络配置
github_proxy=https://gh-proxy.com/
llm_helper_timeout=600
llm_helper_max_retries=3
llm_helper_retry_delay=10
```

## 🎉 使用

### 基础命令

| 命令 | 别名 | 说明 |
|:----:|:----:|:----:|
| `/llm-help [插件名]` | `/help [插件名]` | 查看指定插件的详细帮助 |
| `/llm-help list` | `/help list` | 查看所有插件列表 |
| `/llm-help search [关键词]` | `/help search [关键词]` | 搜索插件和命令 |
| `/llm-help regenerate [插件名]` | `/help regen [插件名]` | 重新生成插件的帮助文档 |

### 使用示例

#### 查看所有插件列表

```
/help list
```

#### 查看特定插件帮助

```
/help nonebot_plugin_weather
```

#### 搜索与天气相关命令

```
/help search 天气
```

#### 重新生成插件帮助

```
/help regenerate nonebot_plugin_weather
```

## 🔧 工作原理

1. **插件扫描**：启动时自动扫描所有已安装的用户插件。
2. **元数据提取**：获取插件的元数据信息和文件路径。
3. **文档获取**：尝试从 GitHub 获取插件的 README 文档。
4. **代码分析**：使用 LLM 分析插件代码结构和功能。
5. **帮助生成**：生成包含命令、参数、用法的详细帮助文档。
6. **缓存存储**：将生成的帮助文档缓存到本地。

## 📄 许可证

本项目采用 GPL-3.0 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 鸣谢

- [NoneBot2](https://github.com/nonebot/nonebot2) - 优秀的机器人框架。
- [Alconna](https://github.com/ArcletProject/Alconna) - 强大的命令解析器。

---

<div align="center">

**如果这个项目对你有帮助，请给它一个 ⭐️ 十分感谢！**

</div>

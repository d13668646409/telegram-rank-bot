# 🧾 Telegram Rank Bot

一个自动在群B输出榜单信息的 Telegram Bot。

---

## 🚀 功能介绍

本机器人监听群A中的信息（如包含“姓名”、“地区”字段），
并在群B中输出一个可点击跳转的榜单项。

示例：

群A消息：
```
姓名：张三
地区：滨江区
联系方式：123456789
```

群B自动生成：
```
[张三 - 滨江区](https://t.me/source_group/123)
```

点击名字即可跳转到原消息。

---

## 🧩 部署方法（Render 平台）

1. 注册 Render：[https://render.com](https://render.com)
2. 创建 Telegram Bot（用 @BotFather）
3. 上传本项目到 GitHub
4. 在 Render 新建 Web Service
5. 设置环境变量：

| Key | Value |
|-----|--------|
| BOT_TOKEN | 你的 Bot Token |
| SOURCE_CHAT | 群A用户名，如 @source_group |
| TARGET_CHAT | 群B用户名，如 @target_group |

6. 启动后状态为 🟢 Live 即运行成功。

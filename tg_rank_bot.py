import os
import telebot
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 从环境变量读取配置
TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT = os.getenv("SOURCE_CHAT")  # 群A用户名，如 @source_group
TARGET_CHAT = os.getenv("TARGET_CHAT")  # 群B用户名，如 @target_group

bot = Bot(token=TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

@dp.message_handler(commands=["rank"])
async def handle_message(message: types.Message):
    # 确保是来自源群的消息
    if message.chat.username == SOURCE_CHAT.replace("@", ""):
        text = message.text or ""
        match = re.search(r"姓名[:：]\s*(\S+).*?地区[:：]\s*(\S+)", text)
        if match:
            name, area = match.groups()
            msg_link = f"https://t.me/{SOURCE_CHAT.replace('@', '')}/{message.message_id}"
            result = f"[{name} - {area}]({msg_link})"
            await bot.send_message(TARGET_CHAT, result)

if __name__ == "__main__":
    print("✅ Bot is running...")
    executor.start_polling(dp, skip_updates=True)



def start_bot():
    print("Bot 已启动...")
    # 使用 infinity_polling 保持 Bot 持续运行
    bot.infinity_polling()

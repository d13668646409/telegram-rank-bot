import os
from threading import Thread
from flask import Flask
from tg_rank_bot import start_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_server():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

if __name__ == "__main__":
    # 启动 Web server 保持在线
    Thread(target=run_server).start()
    # 启动 Telegram Bot
    start_bot()

import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

# توکن بات از Environment Variable
TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=TOKEN)
app = Flask(__name__)

# دیتابیس موقت داخل رم
users = set()

# دستور /start
def start(update, context):
    user_id = update.effective_user.id
    users.add(user_id)
    update.message.reply_text(
        "✅ شما تو لیست اطلاع‌رسانی برای افتتاح بات ثبت شدی.\n"
        "📢 به محض افتتاح، بهت اطلاع داده میشه."
    )

# مسیر اصلی
@app.route("/", methods=["GET"])
def index():
    return "Bot is running"

# مسیر Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "ok"

if __name__ == "__main__":
    dp = Dispatcher(bot, None, workers=0)
    dp.add_handler(CommandHandler("start", start))

    # آدرس واقعی سرویس Koyeb تو وبهوک
    WEBHOOK_URL = "https://respective-rivi-cp01-16ad3c4c.koyeb.app/webhook"
    bot.set_webhook(url=WEBHOOK_URL)

    app.run(host="0.0.0.0", port=8000)

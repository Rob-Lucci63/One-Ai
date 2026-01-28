from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sqlite3
import os

TOKEN = os.getenv("TOKEN")

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT
)
""")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    cursor.execute(
        "INSERT OR IGNORE INTO users VALUES (?, ?)",
        (user.id, user.username)
    )
    conn.commit()

    await update.message.reply_text(
        "✅ شما تو لیست اطلاع‌رسانی برای افتتاح بات ثبت شدی!\n"
        "📢 به‌محض افتتاح، بهت خبر می‌دیم 😎"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

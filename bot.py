import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import yt_dlp
import os

BOT_TOKEN = "8183843583:AAGFFgPYqt70-2XrHtFlFU61usTYlDjz4E4"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam! Instagram linkini göndərin, media faylını sizə qaytarım.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    if "instagram.com" not in url:
        await update.message.reply_text("Instagram linki göndərin zəhmət olmasa.")
        return

    await update.message.reply_text("⏬ Yüklənir...")

    try:
        ydl_opts = {
            'outtmpl': 'insta_%(id)s.%(ext)s',
            'format': 'best',
            'cookiefile': 'cookies.txt',
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await context.bot.send_document(chat_id=update.effective_chat.id, document=open(filename, 'rb'))
        os.remove(filename)

    except Exception as e:
        await update.message.reply_text(f"❌ Xəta: {str(e)}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()

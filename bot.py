import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

WHATSAPP_LINK = "https://wa.me/2349157231049"
INSTAGRAM_LINK = "https://www.instagram.com/annys_nailuxe"
TIKTOK_LINK = "https://www.tiktok.com/@nailsbyanny"
TELEGRAM_GROUP = "https://t.me/+5xjHDMn8i183MDdi"

TOKEN = os.environ.get("BOT_TOKEN", "8797365427:AAH6b8v4bI0d5X8sX8sX8sX8sX8sX8sX8sX8s")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
        [InlineKeyboardButton("🎵 TikTok", url=TIKTOK_LINK)],
        [InlineKeyboardButton("💬 WhatsApp Us", url=WHATSAPP_LINK)],
        [InlineKeyboardButton("🎓 Join Class Group", url=TELEGRAM_GROUP)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Welcome to Anny's Nailuxe! 💅✨\n\nWhere flawless nails are created and luxury meets art.\n\n👇 Connect with us:"
    await update.message.reply_text(text, reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

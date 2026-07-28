Here is the clean code for *Anny's Nailuxe* — just copy and paste:
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

WHATSAPP_LINK = "https://wa.me/2349157231049?text=Hello%20Anny%27s%20Nailuxe.%20I%27m%20interested%20in%20your%20master%20class"
INSTAGRAM_LINK = "https://www.instagram.com/annysnailuxe"
TIKTOK_LINK = "https://www.tiktok.com/@naileditannie"
TELEGRAM_GROUP = "https://t.me/+5xjHDMn8i183ODVk"

TOKEN = "8797365427:AAF8NEoIP0rcx4OtJlH3og7w3ZZ2jUrZVn4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
        [InlineKeyboardButton("🎵 TikTok", url=TIKTOK_LINK)],
        [InlineKeyboardButton("💬 WhatsApp Us", url=WHATSAPP_LINK)],
        [InlineKeyboardButton("🎓 Join Class Group", url=TELEGRAM_GROUP)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = (
        "Welcome to Anny's Nailuxe! 💅✨\n\n"
        "Where flawless nails are created and pros are trained.\n\n"
        "👇 Choose an option below:"
    )
    await update.message.reply_text(text, reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

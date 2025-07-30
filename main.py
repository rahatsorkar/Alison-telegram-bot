import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# --- আপনার তথ্য অনুযায়ী সেট করা হয়েছে ---
# আপনার টেলিগ্রাম বট টোকেন
import os
TELEGRAM_BOT_TOKEN = obiopage.42web.ios.environ.get("TELEGRAM_BOT_TOKEN")

# আপনার নতুন Linktree পোর্টফোলিও লিংক
PORTFOLIO_URL = "biopage.42web.io/"
# ------------------------------------

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# আপনার পছন্দের আকর্ষণীয় বাটন টেক্সট এবং ইমোজি
PORTFOLIO_BUTTON_TEXT = "💌 View Alison's Social World 💖"

# যখন ব্যবহারকারী /start কমান্ড দেবে
async def start(update: Update, context: CallbackContext) -> None:
    """/start কমান্ড দিলে ব্যবহারকারীকে সরাসরি পোর্টফোলিও বাটন পাঠায়।"""
    
    keyboard = [[InlineKeyboardButton(PORTFOLIO_BUTTON_TEXT, web_app=WebAppInfo(url=PORTFOLIO_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # আপনার দেওয়া পছন্দের স্বাগত বার্তা
    welcome_message = (
        "Hi there!💞\n\nWelcome to my personal space ✨\n\n"
        "Click the button below to see all my social links and connect with me!👇👇👇"
    )
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# যখন ব্যবহারকারী অন্য কোনো মেসেজ পাঠাবে
async def message_handler(update: Update, context: CallbackContext) -> None:
    """যেকোনো সাধারণ মেসেজের উত্তরেও পোর্টফোলিও বাটন পাঠায়।"""

    keyboard = [[InlineKeyboardButton(PORTFOLIO_BUTTON_TEXT, web_app=WebAppInfo(url=PORTFOLIO_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # আপনার দেওয়া পছন্দের উত্তর
    await update.message.reply_text(
        "Here are my links again! Just click the button below 👇👇",
        reply_markup=reply_markup
    )

def main() -> None:
    """বটটি শুরু করুন।"""
    logger.info("Starting bot...")
    
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # কমান্ড এবং মেসেজ হ্যান্ডলার যুক্ত করা
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # বটটি চালু করা
    application.run_polling()

# এই অংশটি কোডটি সঠিকভাবে চালানোর জন্য জরুরি
if __name__ == '__main__':
    main()

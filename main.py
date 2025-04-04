from telegram.ext import Application, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import start, medical_query, voice_handler, track_handler, trend_handler, consult_handler, location_handler, text_handler, button

async def error_handler(update, context):
    """Log and handle errors in the bot."""
    print(f"Update {update} caused error {context.error}")

def main():
    import os
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Telegram Bot Token not found. Set TELEGRAM_BOT_TOKEN as an environment variable.")

    application = Application.builder().token(BOT_TOKEN).build()

    # Define handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, text_handler))
    application.add_handler(MessageHandler(Filters.voice, voice_handler))
    application.add_handler(CommandHandler("track", track_handler))
    application.add_handler(CommandHandler("trend", trend_handler))
    application.add_handler(CommandHandler("consult", consult_handler))
    application.add_handler(MessageHandler(Filters.location, location_handler))
    application.add_handler(CallbackQueryHandler(button))
    application.add_error_handler(error_handler)

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()

from telegram.ext import Application
import os

async def start(update, context):
    await update.message.reply_text("👩‍⚕️ Hi! I'm DrMat, your AI Medical Assistant!")

# Webhook setup
def main():
    # Telegram Bot Token from environment variable
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not BOT_TOKEN:
        raise ValueError("Telegram Bot Token not found. Set TELEGRAM_BOT_TOKEN as an environment variable.")

    # Set up bot
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Webhook settings
    PORT = int(os.getenv('PORT', 8443))  # Default port is 8443
    WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://<your-app-name>.repl.co')  # Replace with your Replit URL

    # Run bot with webhook
    app.run_webhook(
        listen="0.0.0.0",  # Listen on all available IPs
        port=PORT,         # Port to listen on
        url_path=BOT_TOKEN,  
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}"  # Full webhook endpoint
    )

if __name__ == "__main__":
    main()

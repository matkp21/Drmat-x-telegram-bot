from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
from apis import diagnose_symptoms, track_symptom, get_symptom_trend, process_consultation

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("👩‍⚕️ Hi! I'm DrMat, your AI medical assistant. Use /track, /trend, /consult, voice, or text to get started!")

async def medical_query(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_id = str(update.message.from_user.id)
    await update.message.reply_text("⏳ Analyzing...")
    diagnosis = await diagnose_symptoms(user_message, user_id=user_id, context=context)
    keyboard = [
        [InlineKeyboardButton("🔮 Prognosis", callback_data=f"prognosis_{update.message.message_id}")],
        [InlineKeyboardButton("🏥 Resources", callback_data=f"resources_{update.message.message_id}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(diagnosis, parse_mode="Markdown", reply_markup=reply_markup)

async def voice_handler(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    file = update.message.voice.get_file()
    audio_path = await file.download_to_drive("voice_input.ogg")
    await update.message.reply_text("⏳ Processing voice...")
    diagnosis = await diagnose_symptoms(audio_path, user_id=user_id, context=context, voice=True)
    await update.message.reply_text(diagnosis, parse_mode="Markdown")

async def track_handler(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    if not context.args:
        await update.message.reply_text("Usage: /track <symptom> <value> (e.g., /track fever 38C)")
        return
    symptom, value = " ".join(context.args[:-1]), context.args[-1]
    response = await track_symptom(user_id, symptom, value, context)
    await update.message.reply_text(response)

async def consult_handler(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    response = await start_consultation(user_id, context)
    await update.message.reply_text(response, parse_mode="Markdown")

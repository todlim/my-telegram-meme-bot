import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")  # токен из переменных окружения

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower() if update.message.text else ""
    
    # Если сообщение с котиком (пример: содержит слово "кот" или "cat")
    if "кот" in text or "cat" in text:
        await update.message.reply_text("Мяу! 🐱 Очень мило!")
    else:
        # Просто эхо-ответ для остальных сообщений
        await update.message.reply_text(f"Ты написал: {update.message.text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Обрабатываем все текстовые сообщения, кроме команд
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Бот запущен...")
    app.run_polling()
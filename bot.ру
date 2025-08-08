import os
import random
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "8444494219:AAFmRHnNCcPNE4tYGVzYtffuF8zeBalnaVM"
ALLOWED_USER_ID = 6059717931

MEMES_FOLDER = "memes"

FUN_REACTIONS = [
    "😂", "крииинж", "🔥", "АХАХА", "ПХАХПАХПХ",
    "пхахпа", "господи", "👍", "ыхвхаыхвахыв"
]

SUPPORT_REACTIONS = [
    "Эй, держись ❤️", "Ты не один, я тут",
    "Понимаю, это тяжело", "Обними себя от меня 🤗",
    "Боль пройдёт, но я с тобой пока"
]

CUTE_REACTIONS = [
    "😻", "Мяу! 🐾", "ути боже", "какая милота 🥰", "Пушистый друг! 🐈"
]

def react(update: Update, context: CallbackContext):
    message = update.message
    user_id = message.from_user.id

    if user_id != ALLOWED_USER_ID:
        # Игнорируем всех, кроме тебя
        return

    text = (message.text or "").lower()
    sad_words = ["груст", "печаль", "тоска", "одиноко", "плохо", "больно", "разлука"]
    cat_words = ["кот", "котик", "котёнок", "киса", "кися"]

    # Если в тексте есть слова про грусть
    if any(word in text for word in sad_words):
        message.reply_text(random.choice(SUPPORT_REACTIONS))
        return

    # Если в тексте есть слова про котиков — милые реакции
    if any(word in text for word in cat_words):
        message.reply_text(random.choice(CUTE_REACTIONS))
        return

    # Если фото или стикер
    if message.photo or message.sticker:
        caption = (message.caption or "").lower()
        if any(word in caption for word in cat_words):
            message.reply_text(random.choice(CUTE_REACTIONS))
            return

        if random.random() < 0.4 and os.path.exists(MEMES_FOLDER):
            meme_files = os.listdir(MEMES_FOLDER)
            if meme_files:
                meme_path = os.path.join(MEMES_FOLDER, random.choice(meme_files))
                with open(meme_path, 'rb') as meme:
                    message.reply_photo(meme)
        else:
            message.reply_text(random.choice(FUN_REACTIONS))
        return

    # Любое другое сообщение
    message.reply_text(random.choice(FUN_REACTIONS))


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, react))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

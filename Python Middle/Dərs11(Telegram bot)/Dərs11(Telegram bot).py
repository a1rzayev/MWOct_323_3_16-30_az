# Logging(hesabat aparma) və Telegram kitabxanalarını daxil edirik
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import random

students = ["Turan", "Nicat", "Əkbər", "Emil"]

# Logging istemini qoşuruq
logging.basicConfig(level=logging.INFO)

# Tokeni qoşuruq 
TOKEN = "8344727558:AAHo0CNUEeRF_x6mTfUPTxNN5i8HRrU9s8s"

# /start funksiyası
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Salam {update.effective_user.first_name}! \n/kime_bir_yazaq - bir yazmaq istediyiniz telebeni tapmaq')


# Mətnə cavab funksiyası
async def kime_bir_yazaq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    selected_student = random.choice(students)
    print(selected_student)
    await update.message.reply_text(f'{selected_student}-ə 1 bal yazın')

def main():
    # Botu "build"(qurmaq) prosesi
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("kime_bir_yazaq", kime_bir_yazaq))
    app.run_polling()


if __name__ == "__main__":
    main()
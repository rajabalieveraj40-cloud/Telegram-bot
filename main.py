import telebot
import re
import os

TOKEN = os.getenv("BOT_TOKEN")  # Railway yoki Herokuga joylaganda tokenni shu yerdan oladi
bot = telebot.TeleBot(TOKEN)

# Reklama havolalarini aniqlash uchun regex
reklama_pattern = re.compile(r"(https?://\S+|t\.me/\S+)", re.IGNORECASE)

@bot.message_handler(func=lambda message: True)
def check_ads(message):
    if reklama_pattern.search(message.text or ""):
        try:
            bot.delete_message(message.chat.id, message.message_id)
            bot.reply_to(
                message,
                "⚠️ Hurmatli guruh foydalanuvchisi!\n"
                "Guruhda reklama tashlash mumkin emas.\n"
                "Reklama joylashtirish uchun guruh egasiga murojaat qiling: @sav571re"
            )
        except:
            pass  # Agar o‘chirish imkoni bo‘lmasa, xato bermasin

print("Bot ishga tushdi...")
bot.polling()

import os
import telebot

bot= telebot.TeleBot("6110502385:AAFzG0uaHK_fZDWcQ5gWbDtuph8lxt_z_lI")

@bot.message_handler(Commnds=[Start])
def send_welcome(message):
    bot.reply_to(message,"Hello ! I am Teena chat bot")

    @bot.message_handler(commands=[How])
    def send_message(message):
        bot.send_message(message. "Https://t.me/@Marin_xd")

  bot.polling()

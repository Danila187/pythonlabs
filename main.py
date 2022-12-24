import telebot
from telebot import types

bot = telebot.TeleBot("5947205414:AAFiHNyVuoIUIVaAN7j6mCBWa4KzKafNY0w")
@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


# @bot.message_handler()
# def get_user_text(message):
#    if message.text == "Hello":
#         bot.send_message(message.chat.id, "Здравствуй!", parse_mode="html")
#   elif message.text == "id":
#        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")
#    else:
#       bot.send_message(message.chat.id, "I dont understand", parse_mode="html")


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Прикольное фото")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://mai.ru"))
    bot.send_message(message.chat.id, "Откройте ссылку", reply_markup=markup)

@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton("Веб сайт")
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, "Откройте ссылку", reply_markup=markup)


bot.polling(none_stop=True)
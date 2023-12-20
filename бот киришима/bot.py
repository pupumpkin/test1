import telebot
from random import choice
from glob import glob
from info import aboutme, contact

token = ("6317095975:AAEqoqAN_5oirlPhmLY2FS7UQbssRyhn_SA")
bot = telebot.TeleBot(token=token)

helpmes = \
    """Я умею:
/help - узнать, что я могу
/about - расскажу все о себе
/selfie - отправлю свою фотку
/contacts - для связи с моей создательницей"""

startmes = \
    """Привет, я Эйджиро Киришима, ученик академии Юэй,
класса 1-А. Напиши /help и я расскажу тебе, что умею!"""

@bot.message_handler(commands=["start"])
def bot_start(message):
    bot.send_message(message.chat.id, text=startmes)

@bot.message_handler(commands=["help"])
def bot_help(message):
    bot.send_message(message.chat.id, text=helpmes)

@bot.message_handler(commands=["selfie"])
def sendselfie(message):
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\бот киришима\kiri2.jpg', 'rb'))

@bot.message_handler(commands=["contacts"])
def contactss(message):
    bot.send_message(message.chat.id, text=contact)

@bot.message_handler(commands=["about"])
def boutme(message):
    bot.send_message(message.chat.id, text=aboutme)

bot.polling()
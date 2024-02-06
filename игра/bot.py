import random
import telebot

from data import *

token = ('6886269693:AAGBTgnzmvWsxFswFB-qWshMz9ewpIXthZo')
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, text=startmes)

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=helpmes)

@bot.message_handler(commands=['go'])
def badboy(message):
    bot.send_message(message.chat.id, text=badboymes)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\photo_2024-01-19_22-01-12.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton(text="Погнали!")
    keyboard.add(btn1)
    bot.send_message(chat_id=message.chat.id, text="Готов, боец?", reply_markup=keyboard)

@bot.message_handler(commands=['contacts'])
def bot_contacts(message):
    bot.send_message(message.chat.id, text=contmes)

@bot.message_handler(func=lambda message: message.text == "Погнали!")
def firstloc(message):
    bot.send_message(message.chat.id, text=first)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация1\швабра.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton(text="Далее")
    keyboard.add(btn1)
    bot.send_message(chat_id=message.chat.id, text="(Вы): Как же тут воняет..", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Далее")
def firstch(message):
    global firstchoice
    firstchoice = "Швабра.."
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton(text="И?")
    keyboard.add(btn1)
    bot.send_message(chat_id=message.chat.id, text=firstchoice, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "И?")
def gogo(message):
    bot.send_message(message.chat.id, text="Взять рукоятку от нее или нет?")
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton(text="Нет")
    btn2 = telebot.types.KeyboardButton(text="Да")
    keyboard.add(btn1, btn2)
    bot.send_message(chat_id=message.chat.id, text="(Вы в мыслях): Стоит хорошо подумать..", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Да")
def yes(message):
    bot.send_message(message.chat.id, text="Отличный выбор. Вам она еще пригодится")
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Дальше")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="Впрочем, продолжаем", reply_markup=keyboard)
artifact = True

@bot.message_handler(func=lambda message: message.text == "Нет")
def no(message):
    bot.send_message(message.chat.id, text="Ваше право ")

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Дальше")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="Впрочем, продолжаем", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Дальше")
def firstloc2(message):
    bot.send_message(message.chat.id, text=firstloc22)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton(text="Бежать")
    btn2 = telebot.types.KeyboardButton(text="Пойти тихо")
    keyboard.add(btn1, btn2)
    bot.send_message(chat_id=message.chat.id, text="(Вы в мыслях): Этот жалкий колледж реально учит"
                                                   " магов?", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Бежать")
def choice1(message):
    bot.send_message(message.chat.id, text="Вам же сказали быть тише! Вы буквально выбежали из колледжа, да с"
                                           " такой скоростью, что пяточки сверкали.")
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация1\маг колледж.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Наконец-то свобода!")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="(Вы): Чуть не заметили. Не хватало"
                                              " раньше времени натворить делов.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Пойти тихо")
def choice2(message):
    bot.send_message(message.chat.id, "Прекрасно, вы умеете учитывать обстоятельства. Все прошло успешно")
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация1\маг колледж.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Наконец-то свобода!")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="(Вы): Жди меня, Годжо. Тебе конец.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Наконец-то свобода!")
def secloc(message):
    bot.send_message(message.chat.id, text=second)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация2\школа.jpg', 'rb'))
    bot.send_message(message.chat.id, text=second1)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация2\школьницы.jpg', 'rb'))
    bot.send_message(message.chat.id, text=second2)

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Пронесло!")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="(Вы, ворча себе под нос): Вот так нашел себе по "
                                                   "пути проблему..", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Пронесло!")
def thirdloc(message):
    bot.send_message(message.chat.id, text=third)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация3\аrmenia.jpg','rb'))
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация3\сибуя.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Ну так сразимся же!")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="(Вы): В моих жилах уже кипит жажда битвы", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Ну так сразимся же!")
def thirdlocfight(message):
    bot.send_message(message.chat.id, text=third2)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\локация3\сукуна.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Нападай!")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="(Вы): Уже предвкушаю это сражение", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Нападай!")
def thirdlocfight1(message):
    bot.send_message(message.chat.id, text=third1)
    bot.send_photo(chat_id=message.chat.id, photo=open('D:\пайтончик в ии\игра\photo_2024-01-19_22-01-12.jpg', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton(text="Я прикончу тебя, Годжо")
    keyboard.add(btn3)
    bot.send_message(chat_id=message.chat.id, text="Вы врываетесь в битву первыми, и..", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Я прикончу тебя, Годжо")
def fight(message):
    bot.send_video(chat_id=message.chat.id, video=open('D:\пайтончик в ии\игра\локация3\файт.mp4', 'rb'))
    sukuna_health = 1000
    gojo_health = 1000
    while sukuna_health > 0 and gojo_health > 0:
        gojo_damage = random.randint(400, 450)
        if artifact == True:
            sukuna_damage = random.randint(700, 800)
        else:
            sukuna_damage = random.randint(400, 450)

        gojo_health -= sukuna_damage
        sukuna_health -= gojo_damage
    if gojo_health <= 0:
        bot.send_message(message.chat.id, text=halfgojo)
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = telebot.types.KeyboardButton(text="Закончить игру")
        keyboard.add(btn3)
        bot.send_message(chat_id=message.chat.id, text="Отлично сработались, злодей", reply_markup=keyboard)
    elif sukuna_health <= 0:
        bot.send_message(message.chat.id, text=halfsukuna)
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = telebot.types.KeyboardButton(text="Закончить игру")
        keyboard.add(btn3)
        bot.send_message(chat_id=message.chat.id, text="Попробуй еще разок.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Закончить игру")
def end(message):
    bot.send_message(message.chat.id, text="Если хочешь начать сначала, напиши /go")

if __name__ == "__main__":
    bot.polling()
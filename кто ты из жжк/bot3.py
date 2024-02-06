import json
import os
from info2 import reset, character_mapping
import telebot

token = ('6777153143:AAGNQiVHSBF0TDmJhrvTg28sg_UVi8K8Vaw')
bot = telebot.TeleBot(token=token)

helpmes = \
    """Я умею:
/help - узнать, что может бот
/test - начать анкетирование"""

startmes = \
    """Привет, хочешь узнать кто ты из "Магической битвы?"
    Что ж, давай начнем. Для этого напиши /test"""

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, text=startmes)

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=helpmes)

@bot.message_handler(commands=['test'])
def start_quiz(message):
    chat_id = message.chat.id
    points = 0
    questions = reset()
    ask_question(chat_id, message, questions, points)

def ask_question(chat_id, message, remaining_questions, current_points):
    if len(remaining_questions) > 0:
        question = remaining_questions[0]
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = telebot.types.KeyboardButton(text="1")
        btn1 = telebot.types.KeyboardButton(text="2")
        btn3 = telebot.types.KeyboardButton(text="3")
        btn4 = telebot.types.KeyboardButton(text="4")
        btn5 = telebot.types.KeyboardButton(text="5")
        keyboard.add(btn, btn1, btn3, btn4, btn5)
        bot.send_message(chat_id, question["question"], reply_markup=keyboard)

        options = question["options"]
        for option_number, option in options.items():
            bot.send_message(chat_id, f"{option_number}. {option['text']}")

        bot.register_next_step_handler(message, process_answer, remaining_questions, current_points)
    else:
        character = "Неизвестный персонаж"
        for points_range, char in character_mapping.items():
            if points_range[0] <= current_points <= points_range[1]:
                character = char
                break
        result = {
            "points": current_points,
            "character": character
        }
        bot.send_message(chat_id,
                         f"Тест завершен. Ваш результат: {result['points']} баллов. Вы - {result['character']}")

        filename = f"results/{chat_id}.json"

        if not os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump(result, file)
                print("Файл 'result.json' успешно создан и результат сохранен!")
        else:
            print(
                "Файл 'result.json' уже существует. Пожалуйста, удалите его или переименуйте перед сохранением нового результата.")

        if os.path.exists(filename):
            with open(filename, "rb") as file:
                bot.send_document(chat_id, file)
        else:
            print("Файл 'result.json' не найден.")

def process_answer(message, remaining_questions, current_points):
    chat_id = message.chat.id
    answer = message.text

    if answer.isdigit() and int(answer) in remaining_questions[0]["options"]:
        current_points += remaining_questions[0]["options"][int(answer)]["points"]
    else:
        bot.send_message(chat_id, "Некорректный вариант ответа. Попробуйте еще раз.")

    remaining_questions.pop(0)
    ask_question(chat_id, message, remaining_questions, current_points)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower().startswith("test"):
        start_quiz(message)
    else:
        bot.send_message(message.chat.id, "Извини, я не могу ответить на этот вопрос. Напиши команду /test")

bot.polling()
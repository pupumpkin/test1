import io
from gpt import *
from config import *
from telebot.types import ReplyKeyboardMarkup
from database import *
#тестилось на модельке openchat_3.5-16k-Mistral-7B-Instruct-v0.2-slerp.Q5_K_S.gguf

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../log_file.txt",
    filemode="w",
)

def create_keyboard(buttons_list):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*buttons_list)
    return keyboard
@bot.message_handler(commands=['start'])
def bot_start(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, text="Здравствуйте! Виктор Петрович к вашим услугам.")
    keyboard = create_keyboard(["Задать вопрос"])
    bot.send_message(chat_id=message.chat.id, text="Чтобы начать работу,"
                                                   " напишите 'Задать вопрос'", reply_markup=keyboard)
    add_id(user_id)
@bot.message_handler(commands=['debug'])
def debug(message):
    logging.getLogger().setLevel(logging.DEBUG)
    bot.send_message(message.chat.id, 'Режим отладки включен')
    try:
        with open('../log_file.txt', 'r') as file:
            logs = file.read()
    except FileNotFoundError:
        bot.reply_to(message, 'Файл не найден')
        return

    bot.send_document(message.chat.id, io.BytesIO(logs.encode()))

    if message.text != "debug" or message.text != "start" or message.text != "Задать вопрос":
        bot.send_message(message.chat.id, text="Такой команды не существует.")

@bot.message_handler(func=lambda message: message.text == "Задать вопрос")
def hello(message):
    bot.send_message(message.chat.id, text='Можешь спросить у меня рецепт любого блюда в формате'
                                           ' "Дай рецепт <Название блюда>" или "Скажи об инградиентах <Название блюда>",'
                                           'и я постараюсь ответить. Но для начала напиши команду /choose_cuisine'
                                           'для выбора кухни')
    bot.send_message(message.chat.id, text='Если напишешь "продолжи", я продолжу объяснять задачу')
    bot.send_message(message.chat.id, text='Для завершения диалога напиши "конец"')
    bot.register_next_step_handler(message, choose_cuisine)

@bot.message_handler(commands=['choose_cuisine'])
def choose_cuisine(message):
    bot.send_message(message.chat.id, "Выбери кухню: Азиатская кухня, Русская кухня, Кавказская кухня",
                     reply_markup=create_keyboard(['Азиатская кухня', 'Русская кухня', 'Кавказская кухня']))
    bot.register_next_step_handler(message, choose_level)

@bot.message_handler(content_types=["choose_level"])
def choose_level(message):
    bot.send_message(message.chat.id, "Выбери уровень мастерства: Новичок, Опытный или"
                                      " Профессионал",
                     reply_markup=create_keyboard(['Новичок', 'Опытный', 'Профессионал']))
    bot.register_next_step_handler(message, dialog)
@bot.message_handler(content_types=["text"])
def dialog(message):
    gpt_dialog(message)

gpt = GPT(system_content="")

def gpt_dialog(message):
    user_request = message.text
    if user_request.lower() == 'конец':
        bot.send_message(message.chat.id, text='До свидания!')
        user_id = message.from_user.id
        bot.send_message(user_id, "Текущее решение завершено")
        gpt.clear_history()
        hello(message)

    if message.text == "Задать вопрос":
        bot.send_message(message.chat.id, text="Извините, не могу обработать эту команду сейчас.")

    request_tokens = gpt.count_tokens(user_request)
    while request_tokens > gpt.MAX_TOKENS:
        bot.send_message(message.chat_id, text="Запрос несоответствует кол-ву токенов\nИсправьте запрос: ")
        user_request = message.text
        request_tokens = gpt.count_tokens(user_request)
    if user_request.lower() != 'продолжи':
        gpt.clear_history()
    json = gpt.make_promt(user_request)
    resp = gpt.send_request(json)
    response = gpt.process_resp(resp)
    if not response[0]:
        bot.send_message(message.chat.id, text="Не удалось выполнить запрос...")
    bot.send_message(message.chat.id, response[1])
def clear_log_file():
    with open("log_file.txt", "w") as file:
        file.write("")

bot.infinity_polling()
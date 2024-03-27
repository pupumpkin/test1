from gpt import *
from telebot.types import ReplyKeyboardMarkup
from database import *
from debug import *

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="log_file.txt",
    filemode="w",
)


def create_keyboard(buttons_list):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*buttons_list)
    return keyboard


@bot.message_handler(commands=['start'])
def bot_start(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Бот запущен")
    logging.info("Бот запущен")
    bot.send_message(message.chat.id, text=bot_start_message)
    keyboard = create_keyboard(["Задать вопрос"])
    bot.send_message(chat_id=message.chat.id, text=start_work, reply_markup=keyboard)


@bot.message_handler(commands=['debug'])
def debug(message):
    debug(message)


@bot.message_handler(commands=['debug_mode_on'])
def debug_mode_on(message):
    start_debug_mode(message)


@bot.message_handler(commands=['debug_mode_off'])
def debug_mode_off(message):
    stop_debug_mode(message)


@bot.message_handler(func=lambda message: message.text == "Задать вопрос")
def hello(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь начал работу с ботом")
    logging.info("Пользователь начал работу с ботом")
    bot.send_message(message.chat.id, text=question)
    bot.send_message(message.chat.id, text=go_on)
    bot.send_message(message.chat.id, text=end)
    keyboard = create_keyboard(["Ввести дополнительные данные"])
    bot.send_message(chat_id=message.chat.id, text="Используй кнопку <Ввести дополнительные данные> для этого",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Ввести дополнительные данные")
def choose_genre(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь вводит дополнительные данные")
    logging.info("Пользователь вводит дополнительные данные")
    user_id = message.from_user.id
    bot.send_message(message.chat.id, text=genres,
                     reply_markup=create_keyboard(['Романтика', 'Комедия', 'Фэнтези']))
    newdata(user_id, "", "", "", "", "", "", "", "")
    add_sessions(user_id)
    check_users_limit()
    check_token_limit_and_sessions(user_id)
    if check_users_limit() == False:
        bot.send_message(message.chat.id, text='Вы превысили лимит на количество пользователей.')
        bot.register_next_step_handler(message, bot_start)
    if check_token_limit_and_sessions(user_id) == False:
        bot.send_message(message.chat.id, text='Вы привысили лимит на количество сессий.')
        bot.register_next_step_handler(message, bot_start)


@bot.message_handler(func=lambda message: message.text == "Романтика")
def romantic(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь ввел жанр Романтика")
    logging.info("Пользователь ввел жанр Романтика")
    bot.send_message(message.chat.id, text=characters)
    bot.send_message(message.chat.id, text=character1)
    bot.send_message(message.chat.id, text=character2)
    bot.send_message(message.chat.id, text=character3)
    bot.send_message(message.chat.id, text=character4,
                     reply_markup=create_keyboard(['Тодороки Шото', 'Нориаки Какёин', 'Кёко Хори', 'Пауэр']))
    genre = "Романтика"
    user_id = message.from_user.id
    update_row_value(user_id, "genre", genre)


@bot.message_handler(func=lambda message: message.text == "Комедия")
def comedy(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь ввел жанр Комедия")
    logging.info("Пользователь ввел жанр Комедия")
    bot.send_message(message.chat.id, text=characters)
    bot.send_message(message.chat.id, text=character1)
    bot.send_message(message.chat.id, text=character2)
    bot.send_message(message.chat.id, text=character3)
    bot.send_message(message.chat.id, text=character4,
                     reply_markup=create_keyboard(['Тодороки Шото', 'Нориаки Какёин', 'Кёко Хори', 'Пауэр']))
    genre = "Комедия"
    user_id = message.from_user.id
    update_row_value(user_id, "genre", genre)


@bot.message_handler(func=lambda message: message.text == "Фэнтези")
def fantasy(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь ввел жанр Фэнтези")
    logging.info("Пользователь ввел жанр Фэнтези")
    bot.send_message(message.chat.id, text=characters)
    bot.send_message(message.chat.id, text=character1)
    bot.send_message(message.chat.id, text=character2)
    bot.send_message(message.chat.id, text=character3)
    bot.send_message(message.chat.id, text=character4,
                     reply_markup=create_keyboard(['Тодороки Шото', 'Нориаки Какёин', 'Кёко Хори', 'Пауэр']))
    genre = "Фэнтези"
    user_id = message.from_user.id
    update_row_value(user_id, "genre", genre)


@bot.message_handler(func=lambda message: message.text == "Тодороки Шото")
def shouto(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал персонажа Тодороки Шото")
    logging.info("Пользователь выбрал персонажа Тодороки Шото")
    bot.send_message(message.chat.id, text=settings, reply_markup=create_keyboard(['Ведьмак', 'GTA 5', 'Breathedge']))
    character = "Тодороки Шото"
    user_id = message.from_user.id
    update_row_value(user_id, "character", character)


@bot.message_handler(func=lambda message: message.text == "Нориаки Какёин")
def leruleruleru(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал персонажа Нориаки Какёин")
    logging.info("Пользователь выбрал персонажа Нориаки Какёин")
    bot.send_message(message.chat.id, text=settings, reply_markup=create_keyboard(['Ведьмак', 'GTA 5', 'Breathedge']))
    character = "Нориаки Какёин"
    user_id = message.from_user.id
    update_row_value(user_id, "character", character)


@bot.message_handler(func=lambda message: message.text == "Кёко Хори")
def hori(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал персонажа Кёко Хори")
    logging.info("Пользователь выбрал персонажа Кёко Хори")
    bot.send_message(message.chat.id, text=settings, reply_markup=create_keyboard(['Ведьмак', 'GTA 5', 'Breathedge']))
    character = "Кёко Хори"
    user_id = message.from_user.id
    update_row_value(user_id, "character", character)


@bot.message_handler(func=lambda message: message.text == "Пауэр")
def pawa(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал персонажа Пауэр")
    logging.info("Пользователь выбрал персонажа Пауэр")
    bot.send_message(message.chat.id, text=settings, reply_markup=create_keyboard(['Ведьмак', 'GTA 5', 'Breathedge']))
    character = "Пауэр"
    user_id = message.from_user.id
    update_row_value(user_id, "character", character)


@bot.message_handler(func=lambda message: message.text == "Ведьмак")
def witcher(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал вселенную Ведьмак")
    logging.info("Пользователь выбрал вселенную Ведьмак")
    bot.send_message(message.chat.id, text=start_prompt)
    setting = "Ведьмак"
    user_id = message.from_user.id
    update_row_value(user_id, "setting", setting)


@bot.message_handler(func=lambda message: message.text == "GTA 5")
def gta(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал вселенную GTA 5")
    logging.info("Пользователь выбрал вселенную GTA 5")
    bot.send_message(message.chat.id, text=start_prompt)
    setting = "GTA 5"
    user_id = message.from_user.id
    update_row_value(user_id, "setting", setting)
    bot.register_next_step_handler(message, dialog)


@bot.message_handler(func=lambda message: message.text == "Breathedge")
def breathedge(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь выбрал вселенную Breathedge")
    logging.info("Пользователь выбрал вселенную Breathedge")
    bot.send_message(message.chat.id, text=start_prompt)
    setting = "Breathedge"
    user_id = message.from_user.id
    update_row_value(user_id, "setting", setting)
    bot.register_next_step_handler(message, dialog)


@bot.message_handler(content_types=['text'])
def dialog(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Пользователь начал работу с GPT")
    logging.info("Пользователь начал работу с GPT")
    user_id = message.from_user.id
    user_content = message.text
    update_row_value(user_id, "user_content", user_content)
    gpt_dialog(message)


def gpt_dialog(message):
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: GPT_dialog вызвана")
    logging.info("GPT_dialog вызвана")
    user_request = message.text
    user_id = message.from_user.id
    if user_request.lower() == 'конец':
        if debugger.active:
            bot.send_message(message.chat.id, f"Log: Работа с GPT закончена")
        logging.info("Пользователь закончил работу с GPT")
        bot.send_message(message.chat.id, text='До свидания!')
        bot.send_message(user_id, "Текущее решение завершено")
        gpt.clear_history()
        hello(message)

    if user_request.lower() == 'продолжи':
        gpt.save_history(user_request, user_id)
        check_token_limit_and_sessions(user_id)
        if check_token_limit_and_sessions(user_id) == False:
            bot.send_message(message.chat.id, text='Вы привысили лимит на количество сессий/токенов.')
            bot.register_next_step_handler(message, bot_start)

    json = gpt.make_promt(user_request, user_id)
    resp = gpt.send_request(HEADERS, json)
    response = gpt.process_resp(resp, user_id)
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: Статус запроса: {response}, Полный запрос: {user_request}")
    logging.info(f"Статус запроса: {response}, Полный запрос: {user_request}")
    if not response[0]:
        if debugger.active:
            bot.send_message(message.chat.id, f"Log: Не удалось выполнить запрос")
        logging.error("Не удалось выполнить запрос")
        bot.send_message(message.chat.id, text="Не удалось выполнить запрос...")
    bot.send_message(message.chat.id, response[1])
    if debugger.active:
        bot.send_message(message.chat.id, f"Log: 200 ОК")
    assistant_content = response[1]
    update_row_value(user_id, "answer", assistant_content)
    combine_text_and_count_tokens(user_id)


prepare_db(True)
gpt = GPT(system_content="")
bot.infinity_polling()

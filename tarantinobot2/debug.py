import logging
from strings import *
from config import *
import io


def clear_log_file(message):
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        bot.send_message(message.chat.id, f"DEBUG LOG: Лог файл очищен")
    logging.info("Лог файл очищен")
    with open("log_file.log", "w") as file:
        file.write("")


def debug(message):
    logging.info("Режим отладки активирован")
    logging.getLogger().setLevel(logging.DEBUG)
    bot.send_message(message.chat.id, debug_mode)
    try:
        with open('log_file.log', 'r') as file:
            logs = file.read()
    except FileNotFoundError:
        logging.error("Файл log_file.log не найден")
        bot.reply_to(message, 'Файл не найден')
        return

    bot.send_document(message.chat.id, io.BytesIO(logs.encode()))
    clear_log_file(message)

    if message.text != "debug" or message.text != "start" or message.text != "Задать вопрос":
        logging.warning("Получена неизвестная команда")
        bot.send_message(message.chat.id, text="Такой команды не существует.")


class DebugMode:
    def __init__(self):
        self.active = False


debugger = DebugMode()


def start_debug_mode(message):
    debugger.active = True
    bot.send_message(message.chat.id, "Режим отладки включен. Теперь вы получите статусы запросов и логи запросов.")


def stop_debug_mode(message):
    debugger.active = False
    bot.send_message(message.chat.id, "Режим отладки выключен.")

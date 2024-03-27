from database import *
import requests
from config import *

class GPT:
    def __init__(self, system_content=""):
        self.headers = HEADERS
        self.system_content = system_content
        self.MAX_TOKENS = 40
        self.assistant_content = "Ваш сценарий:\n"

    def process_resp(self, response, user_id) -> [bool, str]:
        if response.status_code != 200:
            self.clear_history()
            return False, f"Ошибка: {response.status_code}"
        logging.info(f"Ошибка: {response.status_code}")

        try:
            full_response = response.json()
        except:
            self.clear_history()
            return False, "Ошибка получения JSON"
        logging.info("Ошибка получения JSON")

        if "error" in full_response:
            self.clear_history()
            return False, f"Ошибка: {full_response}"
        logging.info(f"Ошибка: {full_response}")

        result = full_response['result']['alternatives'][0]['message']['text']

        if result == "" or result is None:
            self.clear_history()
            return True, "Объяснение закончено"

        self.save_history(result, user_id)
        return True, self.assistant_content

    def make_promt(self, user_request, user_id):
        user_data = get_data_for_user(user_id)
        system_content = (
            f"Ты - профессиональный сценарист. Ты придумываешь сценарий вместе с пользователем. Сценарий должен"
            f"быть основан на жанре {user_data['genre']}, главным героем должен быть {user_data['character']} "
            f"во вселенной {user_data['setting']}. Ты НЕ"
            f"даешь никаких дополнительных комментариев, просто продолжай сценарий. Можешь дополнить сценарий"
            f"диалогами, но начинай их с новой строки и отделяй знаком тире.")
        update_row_value(user_id, 'system_content', system_content)
        json = {
            "modelUri": "gpt://b1gms73juj33ghtqs68d/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": self.MAX_TOKENS,
            },
            "messages": [
                {"role": "system", "text": system_content},
                {"role": "user", "text": user_request},
                {"role": "assistant", "text": self.assistant_content}
            ]
        }
        return json

    def send_request(self, HEADERS, json):
        resp = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion", headers=HEADERS,
                             json=json)
        return resp

    def save_history(self, content_response, user_id):
        self.assistant_content += content_response
        update_row_value(user_id, 'answer', self.assistant_content)

    def clear_history(self):
        self.assistant_content = "Ваш сценарий:\n"

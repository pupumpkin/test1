import requests
from multipomoshnek2.config import *
class GPT:
    def __init__(self, system_content=""):
        self.system_content = system_content
        self.URL = 'http://localhost:1234/v1/chat/completions'
        self.HEADERS = {"Content-Type": "application/json"}
        self.MAX_TOKENS = 17
        self.assistant_content = "Хмм.."

    def count_tokens(prompt,text):
        return len(text) // 2

    def process_resp(self, response) -> [bool, str]:
        if response.status_code < 200 or response.status_code >= 300:
            self.clear_history()
            return False, f"Ошибка: {response.status_code}"
        logging.info(f"Ошибка: {response.status_code}")

        try:
            full_response = response.json()
        except:
            self.clear_history()
            return False, "Ошибка получения JSON"
        logging.info("Ошибка получения JSON")

        if "error" in full_response or 'choices' not in full_response:
            self.clear_history()
            return False, f"Ошибка: {full_response}"
        logging.info(f"Ошибка: {full_response}")

        result = full_response['choices'][0]['message']['content']

        if result == "" or result is None:
            self.clear_history()
            return True, "Объяснение закончено"

        self.save_history(result)
        return True, self.assistant_content

    def make_promt(self, user_request, difficulty_level, cuisinew):
        difficulty_text = ""
        if difficulty_level == "Новичок":
            difficulty_text = ("Ты шеф-повар, который знает множество рецептов. Ты объясняешь как готовить блюдо просто"
                               "и доступно. Ты объясняешь как готовить блюдо новичку. Ты объясняешь как готовить блюдо"
                               "подростку 15-17 лет.")
        elif difficulty_level == "Опытный":
            difficulty_text = ("Ты шеф-повар, который знает множество рецептов. Ты объясняешь как готовить блюдо человеку,"
                               "который умеет готовить. Ты объясняешь как готовить блюдо взрослому человеку.")
        elif difficulty_level == "Профессионал":
            difficulty_text = ("Ты шеф-повар, который знает множество рецептов. Ты объяснешь как готовить блюдо шеф-повару."
                               "Ты используешь профессиональные термины. Ты объясняешь как готовить блюдо"
                               "профессионалу в готовке.")

        cuisinet = ""
        if cuisinew == "Азиатская кухня":
            cuisinet = ("Ты шеф-повар, который знает множество рецептов азиатской кухни."
                        "Ты объясняешь как готовить блюда азиатской кухни."
                        "Ты объясняешь на понятно и на русском языке.")
        elif cuisinew == "Русская кухня":
            cuisinet = ("Ты шеф-повар, который знает множество рецептов русской кухни."
                        "Ты объясняешь как готовить блюда русской кухни."
                        "Ты объясняешь на понятно и на русском языке.")
        elif cuisinew == "Кавказская кухня":
            cuisinet = ("Ты шеф-повар, который знает множество рецептов кавказской кухни."
                        "Ты объясняешь как готовить блюда кавказской кухни."
                        "Ты объясняешь на понятно и на русском языке.")

        json = {
            "messages": [
                {"role": "system", "content": f"{difficulty_text}"},
                {"role": "system", "content": f"{cuisinet}"},
                {"role": "user", "content": user_request},
                {"role": "assistant", "content": self.assistant_content}
            ],
            "temperature": 1.2,
            "max_tokens": self.MAX_TOKENS,
        }
        return json

    def send_request(self, json):
        resp = requests.post(url=self.URL, headers=self.HEADERS, json=json)
        return resp

    def save_history(self, content_response):
        self.assistant_content += content_response

    def clear_history(self):
        self.assistant_content = "Хмм.."

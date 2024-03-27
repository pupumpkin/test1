import telebot

LOGS_PATH = "log_file.log"
TOKEN = "6366910876:AAF6lmlXCfyTSnjmEEuF2BUHbAyUpDaimI8"
bot = telebot.TeleBot(TOKEN)

IAM_TOKEN = """t1.9euelZqdjo-RmsebyJTJmpHGmMqVi-3rnpWay87Nzs-OjprGmc_Mno-Omp3l8_dqK3FP-e9NHHBo_d3z9ypabk_5700ccGj9zef1656Vmp6OkZeckZqXzsackJTJzYzN7_zF656Vmp6OkZeckZqXzsackJTJzYzNveuelZrIz8-MjJaJlMiSlZmMl4mRmLXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.1Cy2ARCeB1Wa7DONuWJ3T7qKLEAcYqOXjMK9__8pOn_RyAYB5VZA_7NWwMKwtJhM7TC5eRzW9k111p5rPKWRAA"""
HEADERS = {
            "Authorization": f"Bearer {IAM_TOKEN}",
            "Content-Type": "application/json"}
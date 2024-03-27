import sqlite3
import logging
import requests
from strings import DB_NAME, DB_TABLE_USERS_NAME, MAX_TOKENS_IN_SESSION
from config import *

logging.basicConfig(filename=LOGS_PATH, level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filemode='w')


def create_db(database_name=DB_NAME):
    db_path = f'{database_name}'
    conn = sqlite3.connect(db_path)
    conn.close()

    logging.info(f'DATABASE: Output: База данных успешно создана')


def execute_query(sql_query, data=None, db_path=f'{DB_NAME}'):
    logging.info(f'DATABASE: Execute query: {sql_query}')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    if data:
        cur.execute(sql_query, data)
    else:
        cur.execute(sql_query)

    conn.commit()
    conn.close()


def execute_selection_query(sql_query, data=None, db_path=f'{DB_NAME}'):
    logging.info(f'DATABASE: Execute query: {sql_query}')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if data:
        cur.execute(sql_query, data)
    else:
        cur.execute(sql_query)
    rows = cur.fetchall()
    conn.close()
    return rows


def create_table_users(DB_TABLE_USERS_NAME):
    sql_query = f'CREATE TABLE IF NOT EXISTS {DB_TABLE_USERS_NAME}' \
                f'(id INTEGER PRIMARY KEY, ' \
                f'user_id INTEGER,' \
                f'genre TEXT,' \
                f'character TEXT,' \
                f'setting TEXT,' \
                f'system_content TEXT,' \
                f'user_content TEXT,' \
                f'answer TEXT,' \
                f'tokens INTEGER,' \
                f'session_id INTEGER)'
    execute_query(sql_query)
    conn = sqlite3.connect(f'{DB_NAME}')
    conn.commit()
    conn.close()


def insert_row(values):
    columns = "(user_id, genre, character, setting, system_content, user_content, answer, tokens, session_id)"
    sql_query = f'INSERT INTO {DB_TABLE_USERS_NAME} {columns} VALUES (?,?,?,?,?,?,?,?,?)'
    execute_query(sql_query, values)


def is_value_in_table(table_name, column_name, value):
    sql_query = f'SELECT {column_name} FROM {table_name} WHERE {column_name} = {value} LIMIT 1'
    rows = execute_selection_query(sql_query)
    return any(rows) > 0


def update_row_value(user_id, column_name, new_value):
    if is_value_in_table(DB_TABLE_USERS_NAME, "user_id", user_id):
        sql_query = f'UPDATE {DB_TABLE_USERS_NAME} SET {column_name} = ? WHERE user_id = {user_id}'
        execute_query(sql_query, [new_value])
    else:
        logging.info(f"DATABASE: Пользователь с id {user_id} не найден")
        print("DATABASE: Пользователь с таким id не найден")


def get_data_for_user(user_id):
    if is_value_in_table(DB_TABLE_USERS_NAME, 'user_id', user_id):
        sql_query = f'SELECT * FROM {DB_TABLE_USERS_NAME} WHERE user_id = ? LIMIT 1'
        row = execute_selection_query(sql_query, [user_id])[0]
        return {
            "user_id": row[1],
            "genre": row[2],
            "character": row[3],
            "setting": row[4],
            "system_content": row[5],
            "user_content": row[6],
            "answer": row[7],
            "tokens": row[8],
            "session_id": row[9]
        }
    else:
        logging.info(f"DATABASE: Пользователь с id {user_id} не найден")
        print("DATABASE: Пользователь с таким id не найден")
        return {
            "user_id": "",
            "genre": "",
            "character": "",
            "setting": "",
            "system_content": "",
            "user_content": "",
            "answer": "",
            "tokens": "",
            "session_id": ""
        }


def prepare_db(clean_if_exists=False):
    create_db()
    create_table_users(DB_TABLE_USERS_NAME)


def newdata(user_id, genre, character, setting, system_content, user_content, answer, tokens, session_id):
    if is_value_in_table(DB_TABLE_USERS_NAME, 'user_id', user_id):
        update_row_value(user_id, 'genre', genre)
        update_row_value(user_id, 'character', character)
        update_row_value(user_id, 'setting', setting)
        update_row_value(user_id, 'system_content', system_content)
        update_row_value(user_id, 'user_content', user_content)
        update_row_value(user_id, 'answer', answer)
        update_row_value(user_id, 'tokens', tokens)
        update_row_value(user_id, 'session_id', session_id)

        logging.info(f"DATABASE: Данные для пользователя {user_id} обновлены")
    else:
        insert_row((user_id, genre, character, setting, system_content, user_content, answer, tokens, session_id))
        logging.info(f"DATABASE: Данные для пользователя {user_id} добавлены")
    prepare_db(True)


def add_sessions(user_id):
    user_data = get_data_for_user(user_id)
    VIP_ID = [1482726705, 5770464957]
    if user_data['user_id'] not in VIP_ID:
        session_id = 1
        update_row_value(user_id, 'session_id', session_id)


def check_users_limit():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(DISTINCT user_id) FROM {DB_TABLE_USERS_NAME}")
    count = cursor.fetchone()[0]

    if count > 3:
        return False
    else:
        return True


def count_tokens(text):
    headers = HEADERS
    data = {
        "modelUri": f"gpt://b1gms73juj33ghtqs68d/yandexgpt-lite",
        "text": text
    }
    return len(
        requests.post(
            "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenize",
            json=data,
            headers=headers
        ).json()['tokens']
    )


def combine_text_and_count_tokens(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(f"SELECT system_content, user_content, answer FROM {DB_TABLE_USERS_NAME} WHERE user_id = {user_id}")
    rows = cur.fetchall()

    for row in rows:
        combined_text = ' '.join(filter(None, row))

        token_count = count_tokens(combined_text)

        if token_count is not None:
            cur.execute(f"UPDATE {DB_TABLE_USERS_NAME} SET tokens =? WHERE user_id =?", (token_count, user_id))

    conn.commit()
    conn.close()


def check_token_limit_and_sessions(user_id):
    user_data = get_data_for_user(user_id)
    session_id = user_data['session_id']
    vip_id = [1482726705, 5770464957]
    if user_data['user_id'] not in vip_id:
        if user_data and len(user_data['tokens']) >= MAX_TOKENS_IN_SESSION:
            if session_id == 0:
                print("Превышен лимит токенов и сессий.")
                return False
        else:
            return True
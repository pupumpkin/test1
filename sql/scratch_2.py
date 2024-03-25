import sqlite3

def prepare_database():
    connection = sqlite3.connect('sqlite3.db')
    cur = connection.cursor()

    sql_query = f'CREATE TABLE IF NOT EXISTS questions' \
                    f'(id INTEGER PRIMARY KEY, ' \
                    f'user_id INTEGER, ' \
                    f'subject TEXT, ' \
                    f'level TEXT, ' \
                    f'task TEXT, ' \
                    f'answer TEXT)'

    cur.execute(sql_query)

    cur.execute('INSERT INTO questions VALUES (1, 111, "алгебра", "начинающий", "2 в степени 5", "32");')
    cur.execute('INSERT INTO questions VALUES (2, 222, "алгебра", "начинающий", "600+27", "627");')
    cur.execute('INSERT INTO questions VALUES (3, 333, "алгебра", "профи", "Количество нулей в числе Google", "100");')
    cur.execute('INSERT INTO questions VALUES (4, 222, "физика", "начинающий", "Ускорение свободного падения", "9.8");')
    cur.execute('INSERT INTO questions VALUES (5, 444, "физика", "профи", "Кто связал магнитные и электрические явления", "Максвелл");')
    cur.execute('INSERT INTO questions VALUES (6, 555, "физика", "профи", "Мера хаоса", "Энтропия");')
    cur.execute('INSERT INTO questions VALUES (7, 111, "физика", "начинающий", "Единица измерения теплоты", "Джоуль");')
    cur.execute('INSERT INTO questions VALUES (8, 222, "физика", "начинающий", "Единица измерения веса", "Ньютон");')
    cur.execute('INSERT INTO questions VALUES (9, 222, "музыка", "профи", "Знак для продления ноты", "Фермата");')
    cur.execute('INSERT INTO questions VALUES (10, 222, "музыка", "профи", "Сколько всего нот", "7");')
    cur.execute('INSERT INTO questions VALUES (11, 444, "литература", "начинающий", "Как звали Пастернака", "Борис Леонидович");')
    cur.execute('INSERT INTO questions VALUES (12, 444, "литература", "профи", "Восьмой цвет и цвет магии", "Октарин");')
    cur.execute('INSERT INTO questions VALUES (13, 444, "литература", "профи", "Главный вопрос Вселенной", "42");')
    cur.execute('INSERT INTO questions VALUES (14, 666, "литература", "профи", "Деревня Дарьи Пинигиной", "Матёра");')
    cur.execute('INSERT INTO questions VALUES (15, 777, "литература", "начинающий", "Автор истории об алых парусах", "Александр Грин");')

    connection.commit()
    connection.close()

prepare_database()
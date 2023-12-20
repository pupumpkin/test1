import PIL
import os
from PIL import Image
from filters import RedFilter, GreenFilter, InverseFilter

path = input("Введите путь к файлу: ")

while not os.path.exists(path):
    path = input("Файл не найден. Попробуйте ещё раз: ")


def main():
    filter_names = [
        "Усиление красного"
        "Усиление зеленого"
        "Инверсия"
    ]

    filters = [
        RedFilter(),
        GreenFilter(),
        InverseFilter()
    ]

    print("Добро пожаловать в консольный фоторедактор!")
    is_finished = False
    while not is_finished:
        path = input("Введите путь к файлу:")
        img = Image.open(path).convert("RGB")

        while not os.path.exists(path):
            path = input("Файл не найден (неверно введен путь). Попробуйте еще раз")

        print("Какой фильтр вы хотите применить?")
        for i in range(len(filter_names)):
            print(f"{i} - {filter_names[i]}")

        choice = input("Выберите фильтр(введите его номер):")
        while not choice.isdigit() or int(choice) >= len(filters):
            choice = input("Некорректный ввод. Попробуйте еще раз")

        filt = filters[int(choice)]
        img = filt.apply_to_image(img)

        savepath = input("Введите путь для сохранения изображения:")
        img.save(savepath)

        answ = input("Хотите повторить (Да/нет):").upper()

        while answ != "ДА" and answ != "НЕТ":
            answ = input("Некорректный ввод. Попробуйте еще раз")
        is_finished = answ == "НЕТ"


if __name__ == "__main_":
    main()
import json

# 1. Показываем меню
print("--- Менеджер заметок 📝 ---")
print("1 — Создать новую заметку")
print("2 — Прочитать заметку")

# 2. Спрашиваем выбор у пользователя
choice = input("Выберите действие (1 или 2): ")

# 3. Обрабатываем выбор
if choice == "1":
    # Запрашиваем данные
    title = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")

    # Упаковываем в словарь
    note = {
        "title": title,
        "text": text
    }

    # Сохраняем в файл
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(note, file, ensure_ascii=False, indent=4)

    print("Заметка успешно сохранена! 🎉")

elif choice == "2":
    # Открываем и читаем файл
    with open("notes.json", "r", encoding="utf-8") as file:
        note = json.load(file)

    # Выводим на экран
    print("\n--- Ваша заметка ---")
    print("Заголовок 📌:", note["title"])
    print("Текст 📝:", note["text"])

else:
    print("Неверный выбор! Запустите программу снова и введите 1 или 2.")
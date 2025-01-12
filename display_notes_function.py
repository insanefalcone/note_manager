import colorama
from colorama import Fore, Style
from datetime import datetime

colorama.init(autoreset=True)


def display_notes(notes, detail_level='full', sort_by='created_date', items_per_page=5, page=1):
    """Отображает список заметок с возможностью настройки."""

    if not notes:
        print(Fore.RED + "У вас нет сохранённых заметок.")
        return

    # Сортировка заметок
    if sort_by == 'created_date':
        notes.sort(key=lambda x: datetime.strptime(x['created_date'], '%d-%m-%Y'))  # сортировка по дате создания
    elif sort_by == 'issue_date':
        notes.sort(key=lambda x: datetime.strptime(x['issue_date'], '%d-%m-%Y'))  # сортировка по дате дедлайна
    elif sort_by == 'username':
        notes.sort(key=lambda x: x['username'].lower())  # Сортировка по имени

    # Разделение на страницы
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paged_notes = notes[start_index:end_index]

    # Заголовок таблицы
    if detail_level == 'full':
        print(Fore.CYAN + "Заметки: Полные данные" + Style.RESET_ALL)
        print("-" * 80)
        print(f"{'№':<5}{'Имя пользователя':<20}{'Заголовок':<30}{'Дата создания':<15}{'Дедлайн':<15}")
        print("-" * 80)

        for index, note in enumerate(paged_notes, start=start_index + 1):
            print(
                f"{index:<5}{note.get('username', 'Не указано'):<20}{note.get('title', 'Не указано'):<30}{note.get('created_date', 'Не указано'):<15}{note.get('issue_date', 'Не указано'):<15}")
            print("-" * 80)
    elif detail_level == 'titles':
        print(Fore.CYAN + "Заметки: Заголовки только" + Style.RESET_ALL)
        print("-" * 80)

        for index, note in enumerate(paged_notes, start=start_index + 1):
            print(Fore.GREEN + f"Заметка №{index}: {note.get('title', 'Не указано')}" + Style.RESET_ALL)
            print("-" * 80)

    # Уведомление если заметок больше чем показано
    if len(notes) > end_index:
        print(
            Fore.YELLOW + f"Показано {len(paged_notes)} из {len(notes)} заметок. Используйте '<' для предыдущей страницы и '>' для следующей." + Style.RESET_ALL)


def main():
    notes_list = [
        {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты на неделю", "status": "новая",
         "created_date": "08-01-2025", "issue_date": "15-01-2025"},
        {"username": "Мария", "title": "Заметка о встречах", "content": "Встретиться с командой в 15:00",
         "status": "в процессе", "created_date": "05-01-2025", "issue_date": "06-01-2025"},
        {"username": "Иван", "title": "Курс по Python", "content": "Завершить второе задание", "status": "новая",
         "created_date": "26-11-2024", "issue_date": "01-12-2025"},
        {"username": "Ольга", "title": "Чтение книг", "content": "Закончить книгу '1984'", "status": "в процессе",
         "created_date": "24-11-2024", "issue_date": "28-02-2025"},
        {"username": "Павел", "title": "Спорт", "content": "Заниматься 3 раза в неделю", "status": "выполнена",
         "created_date": "23-11-2024", "issue_date": "05-12-2024"},
        {"username": "Елена", "title": "Путешествие", "content": "Запланировать отпуск", "status": "новая",
         "created_date": "22-11-2024", "issue_date": "15-12-2025"},
    ]

    page = 1
    total_items = len(notes_list)

    # Выбор метода сортировки
    sort_method = input("Выберите метод сортировки (1 - по дате создания, 2 - по дедлайну, 3 - по имени): ").strip()
    if sort_method == '1':
        sort_by = 'created_date'
    elif sort_method == '2':
        sort_by = 'issue_date'
    elif sort_method == '3':
        sort_by = 'username'
    else:
        print(Fore.RED + "Некорректный ввод. Будет использована сортировка по дате создания." + Style.RESET_ALL)
        sort_by = 'created_date'

    # Выбор уровня детализации
    detail_level = input("Выберите уровень детализации (1 - полные данные, 2 - только заголовки): ").strip()
    if detail_level == '1':
        detail_level = 'full'
    elif detail_level == '2':
        detail_level = 'titles'
    else:
        print(Fore.RED + "Некорректный ввод. Будет использован уровень детализации по умолчанию (полные данные)." + Style.RESET_ALL)
        detail_level = 'full'

    while True:
        display_notes(notes_list, detail_level=detail_level, sort_by=sort_by, items_per_page=2, page=page)

        command = input("Введите '<' для предыдущей страницы, '>' для следующей страницы или 'выход' для выхода: ").strip()

        if command == '>':
            if page * 2 < total_items:
                page += 1
            else:
                print(Fore.RED + "Это последняя страница." + Style.RESET_ALL)
        elif command == '<':
            if page > 1:
                page -= 1
            else:
                print(Fore.RED + "Это первая страница." + Style.RESET_ALL)
        elif command == 'выход':
            break
        else:
            print(Fore.RED + "Неизвестная команда. Пожалуйста, попробуйте снова." + Style.RESET_ALL)

if __name__ == "__main__":
    main()


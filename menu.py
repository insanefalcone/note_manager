
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

notes = []

def print_menu():
    print(Fore.CYAN + "\nВыберите действие:")
    print(Fore.GREEN + "1: Создать новую заметку")
    print(Fore.GREEN + "2: Показать все заметки")
    print(Fore.GREEN + "3: Обновить заметку")
    print(Fore.GREEN + "4: Удалить заметку")
    print(Fore.GREEN + "5: Найти заметки")
    print(Fore.YELLOW + "6: Выйти из программы")

def create_note():
    note = input(Fore.MAGENTA + "Введите текст заметки: ")
    notes.append(note)
    print(Fore.GREEN + "Заметка добавлена.")

def display_notes():
    if not notes:
        print(Fore.RED + "Заметки отсутствуют.")
    else:
        print(Fore.CYAN + "Список заметок:")
        for index, note in enumerate(notes, start=1):
            print(Fore.WHITE + f"{index}: {note}")

def update_note():
    display_notes()
    try:
        index = int(input(Fore.MAGENTA + "Введите номер заметки для обновления: ")) - 1
        if 0 <= index < len(notes):
            new_note = input(Fore.MAGENTA + "Введите новый текст заметки: ")
            notes[index] = new_note
            print(Fore.GREEN + "Заметка обновлена.")
        else:
            print(Fore.RED + "Неверный номер заметки.")
    except ValueError:
        print(Fore.RED + "Пожалуйста, введите число.")

def delete_note():
    display_notes()
    try:
        index = int(input(Fore.MAGENTA + "Введите номер заметки для удаления: ")) - 1
        if 0 <= index < len(notes):
            confirm = input(Fore.YELLOW + "Вы уверены, что хотите удалить эту заметку? (да/нет): ")
            if confirm.lower() == 'да':
                notes.pop(index)
                print(Fore.GREEN + "Заметка удалена.")
            else:
                print(Fore.RED + "Удаление отменено.")
        else:
            print(Fore.RED + "Неверный номер заметки.")
    except ValueError:
        print(Fore.RED + "Пожалуйста, введите число.")

def search_notes():
    query = input(Fore.MAGENTA + "Введите текст для поиска: ")
    results = [note for note in notes if query.lower() in note.lower()]
    if results:
        print(Fore.CYAN + "Найденные заметки:")
        for note in results:
            print(Fore.WHITE + note)
    else:
        print(Fore.RED + "Заметки не найдены.")

def main_menu():
    while True:
        print_menu()
        choice = input(Fore.MAGENTA
 + "Введите номер действия: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            display_notes()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes()
        elif choice == '6':
            print(Fore.GREEN + "Выход из программы.")
            break
        else:
            print(Fore.RED + "Неверный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main_menu()


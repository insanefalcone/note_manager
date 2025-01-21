
import json
from datetime import datetime

def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print("Заметки успешно сохранены в файл.", filename)
    except IOError as e:
        print(f"Ошибка при записи в файл {filename}: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": datetime.now().strftime("%d-%m-%Y"),
        "issue_date": "30-11-2024"
    }
]

save_notes_json(notes, 'filename.json')


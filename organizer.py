import os
import shutil
import tkinter as tk
from tkinter import filedialog

def sort_files_by_extension(directory):
    if not os.path.exists(directory):
        print("Указанная папка не существует.")
        return
    
    print(f"Сортировка файлов в папке: {directory}")
    
    # Словарь с категориями файлов
    categories = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'],
        'Videos': ['mp4', 'avi', 'mov', 'mkv'],
        'Music': ['mp3', 'wav', 'aac', 'flac'],
        'Archives': ['zip', 'rar', '7z', 'tar', 'gz'],
        'Programs': ['exe', 'msi', 'bat', 'sh'],
        'Other': []
    }
    
    # Проверяем, какие папки уже существуют, создаем только недостающие
    existing_folders = set(os.listdir(directory))
    for category in categories.keys():
        category_path = os.path.join(directory, category)
        if category not in existing_folders:
            os.makedirs(category_path, exist_ok=True)
    
    # Перебираем файлы в указанной директории
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()
            moved = False
            
            # Проверяем, в какой категории находится расширение
            for category, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, category, file))
                    print(f"Файл {file} перемещен в {category}")
                    moved = True
                    break
            
            # Если расширение неизвестное - перемещаем в "Other"
            if not moved:
                other_path = os.path.join(directory, 'Other')
                shutil.move(file_path, os.path.join(other_path, file))
                print(f"Файл {file} перемещен в Other")
    
    print("Сортировка завершена!")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно
    
    folder_path = filedialog.askdirectory(title="Выберите папку для сортировки")
    if folder_path:
        print(f"Выбрана папка для сортировки: {folder_path}")
        sort_files_by_extension(folder_path)
    else:
        print("Папка не выбрана.")

if __name__ == "__main__":
    select_folder()


import json
import os

FILE_NAME = "todos.json"

def load_todos():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_todos(todos):
    with open(FILE_NAME, "w") as file:
        json.dump(todos, file, indent=4)

def list_todos():
    todos = load_todos()
    if not todos:
        print("Hiç görev yok.")
        return
    for i, todo in enumerate(todos):
        status = "✔" if todo["done"] else "✘"
        print(f"{i + 1}. [{status}] {todo['task']}")

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("Görev eklendi.")

def complete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print("Görev tamamlandı.")
    else:
        print("Geçersiz numara.")

def delete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos.pop(index)
        save_todos(todos)
        print("Görev silindi.")
    else:
        print("Geçersiz numara.")

def menu():
    while True:
        print("\n--- TODO APP ---")
        print("1. Görevleri listele")
        print("2. Görev ekle")
        print("3. Görev tamamla")
        print("4. Görev sil")
        print("5. Çıkış")

        choice = input("Seçim: ")

        if choice == "1":
            list_todos()
        elif choice == "2":
            task = input("Görev: ")
            add_todo(task)
        elif choice == "3":
            index = int(input("Numara: ")) - 1
            complete_todo(index)
        elif choice == "4":
            index = int(input("Numara: ")) - 1
            delete_todo(index)
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim.")

if _name_ == "_main_":
    menu()

import csv
import os

def add_task():
    name = input("Vazifa nomini kiriting: ")

    if not name.strip():
        print("Vazifa nomi bo'sh bo'lmasin!")
        return

    tasks = []

    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            tasks = list(reader)

    if tasks:
        new_id = max(int(task["id"]) for task in tasks) + 1
    else:
        new_id = 1

    with open("tasks.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if os.path.getsize("tasks.csv") == 0:
            writer.writerow(["id", "name", "status"])

        writer.writerow([new_id, name, "bajarilmagan"])

    print("Vazifa muvaffaqiyatli qo'shildi!")


if __name__ == "__main__":
    add_task()
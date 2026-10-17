import csv

def complete_task():
    task_id = input("Bajarilgan vazifa ID sini kiriting: ")

    with open("tasks.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        tasks = list(reader)

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "bajarilgan"
            found = True
            break

    if not found:
        print("Bunday ID topilmadi!")
        return

    with open("tasks.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "name", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(tasks)

    print("Vazifa bajarilgan deb belgilandi!")


if __name__ == "__main__":
    complete_task()
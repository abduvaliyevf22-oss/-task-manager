import csv

def show_tasks():
    with open("tasks.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for task in reader:
            print("ID:", task["id"])
            print("Nomi:", task["name"])
            print("Holati:", task["status"])
            print("-------------------")


if __name__ == "__main__":
    show_tasks()
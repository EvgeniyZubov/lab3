import lab3

task_func_dictionary = {
    "1": lab3.proc21,
    "2": lab3.matrix14,
}
if __name__ == '__main__':
    choice = input("Оберіть завдання 1-2 (0-EXIT): ")
    while choice != "0":
        if choice in task_func_dictionary.keys():
          task_func_dictionary.get(choice)()
        else:
          print("Помилка!")
        choice = input("Будь-ласка, оберіть завдання знову (0-EXIT): ")

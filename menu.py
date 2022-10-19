from previev_baza import previev_baza
from add_record import add_record
from delete_record import delete_record


def input_chuise():
    while True:
        user_choise = input('1 - Посмотреть базу\n2 - Добавить запись\n3 - Удалить запись\n4 - Выход\n')
        if user_choise == "1":
            previev_baza()
        elif user_choise == "2":
            add_record()
        elif user_choise == "3":
            delete_record()
        elif user_choise == "4":
            print("Выход")
            break
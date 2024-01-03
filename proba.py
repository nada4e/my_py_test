import time
import os
from datetime import datetime

now_datetime = datetime.now().time()


def welcome_decorator(func):
    def wrapper(*args, **kwargs):
        print("******************************")
        print("*                            *")
        print("*    Добро пожаловать!       *")
        print("*                            *")
        print("******************************")
        return func(*args, **kwargs)
    return wrapper



@welcome_decorator
def greet(name):
    if now_datetime < datetime.strptime('12:00:00', '%H:%M:%S').time():
        print(f"Доброе утро, {name}!")
    elif now_datetime < datetime.strptime('17:00:00', '%H:%M:%S').time():
        print(f"Добрый день, {name}!")
    elif now_datetime > datetime.strptime('17:00:00', '%H:%M:%S').time():
        print(f"Добрый вечер, {name}!")


greet("Нуб")


programm_start = input("Готов начать? Да / Нет\n").lower()


while programm_start != "да" and programm_start != "нет":
    programm_start = input("Что-то невнятное, так ДА или НЕТ?: ").lower()
if programm_start == "да":
    print("Отлично! Ах да, чуть не забыл, тебе лет-то сколько?")
elif programm_start == "нет":
    print("Давай до свидания!\nТеперь питание компьютера можно отключить.")
    exit()


user_age = input()


if 18 <= int(user_age) <= 34:
    print("Ok, хотя это мы ещё проверим.")
elif 35 <= int(user_age) <= 59:
    print("И куда тебя старого занесло...")
elif int(user_age) >= 60:
    print("Дед! Тебя кто к компьютеру пустил?")
else:
    print("Ой! Кого-то мамочка спать зовёт((")
    exit()


user_name = input("Для начала давай познакомимся!\nКак тебя зовут?\n").capitalize()
pc_name = ("PCдр04еR3000")


def say_hello(user_name):
    print(f"Рад тебя приветствовать ", user_name,"! Меня зовут - "+pc_name+"!")


say_hello(user_name)

user_location = input("Ты откуда к нам пожаловал?\n").capitalize()
print(" ".join(user_location) + "!? Бывал я там! Дыра ещё та!")


print("ну что " + user_location + "ский житель - " + user_name + ", для продолжения ответь на простой вопрос:\nКакая корпорация причастна к восстанию машин?") # доработать склонения
print("Варианты ответа:\n")
print("Амбрелла\n""Скайнет\n""Корпорация монстров\n")


max_attempts = 2
wrong_attempts = 0

while True:
    answer = input("Ответ: ").lower()


    if answer != "скайнет":
        wrong_attempts += 1
        print("Не верно, попробуй еще!")


        if wrong_attempts >= max_attempts:
            print("Кажется ты обманул меня с возростом!\nДавай до свидания!\nТеперь питание компьютера можно отключить.")
            break
    else:
        print("Молодец! Теперь я вижу что ты не наврал с возрастом.\n")
        break

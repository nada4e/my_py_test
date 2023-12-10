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
    print(f"Привет, {name}!")

greet("Нуб")

start = input("Готов начать? Да / Нет\n").lower()

while start != "да" and start != "нет":
    start = input("Что-то невнятное, так ДА или НЕТ?: ").lower()
if start == "да":
    print("Отлично! Ах да, чуть не забыл, тебе лет-то сколько?")
elif start == "нет":
    print("Давай до свидания!\nТеперь питание компьютера можно отключить.")
    exit()

age = int(input())
if age >= 18:
    print("Ok, хотя это мы ещё проверим.")
else:
    print("Ой! Кого-то мамочка спать зовёт((")
    exit()

name = input("Для начала давай познакомимся!\nКак тебя зовут юный хацкер?\n")
pc_name = ("PCдр04еR3000")

def say_hello(name):
    print(f"Рад тебя приветствовать ", name,"! Меня зовут - "+pc_name+"!")


say_hello(name)

location = input("Ты откуда к нам пожаловал?\n")
print(" ".join(location)+"!? Бывал я там! Дыра ещё та!")
print("ну что "+location+"ский житель - "+name+", для продолжения ответь на простой вопрос:\nКакая корпорация причастна к восстанию машин?") # доработать склонения
print("Варианты ответа:\n")
print("Амбрелла\n""Скайнет\n""Корпорация монстров\n")
x = input("Ответ: ").lower()
while x != "скайнет":
    x = input("попробуй снова: ").lower()
print("Молодец! Теперь я вижу что ты не наврал с возрастом.\n")

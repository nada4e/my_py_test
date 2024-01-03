import random

def main():
    print("Добро пожаловать в игру 21!")
    print("Цель игры - набрать сумму карт, близкую к 21, но не больше.")
    print("У вас и у компьютера будет по очереди возможность брать карты.")
    print("Удачи!\n")

    while True:
        player_total = 0
        computer_total = 0
        player_turn = True

        while player_turn:
            player_choice = input("Желаете взять карту? (Да/Нет): ").lower()
            if player_choice == "да":
                card = random.randint(1, 11)
                player_total += card
                print(f"Вы взяли карту на {card}. Ваш текущий счет: {player_total}")
                if player_total > 21:
                    print("Вы проиграли! Перебор.")
                    break
            elif player_choice == "нет":
                player_turn = False

        if player_total <= 21:
            while computer_total < 17:
                card = random.randint(1, 11)
                computer_total += card
                print(f"Компьютер взял карту на {card}. Текущий счет компьютера: {computer_total}")

            if computer_total > 21:
                print("Компьютер проиграл! Перебор.")
            else:
                print("Игра окончена!")
                if player_total > computer_total:
                    print("Вы выиграли!")
                elif player_total < computer_total:
                    print("Компьютер выиграл!")
                else:
                    print("Ничья!")

        play_again = input("Хотите сыграть еще раз? (Да/Нет): ").lower()
        if play_again != "да":
            break

    print("Спасибо за игру!")

if __name__ == "__main__":
    main()

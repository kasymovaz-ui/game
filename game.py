import random


def add_coins(coins, found):
    return coins + found


def check_result(coins):
   if coins >= 50:
        return "win"
   else:
        return "lose"


def validate_choice(choice):
    return choice in ["1", "2"]


def play_game():
    coins = 0

    print("СОБЕРИ 50 МОНЕТ!")
    print("У тебя 10 ходов.")

    for turn in range(1, 11):
        found = random.randint(1, 10)
        coins = add_coins(coins, found)

        print(f"Ход {turn}: ты нашёл {found} монет.")
        print(f"Всего монет: {coins}")

    print("\nИгра закончена!")

    result = check_result(coins)

    if result == "win":
        print("Ты победил!")
    else:
        print("Ты не собрал 50 монет.")

    return coins


if __name__ == "__main__":
    play_game()
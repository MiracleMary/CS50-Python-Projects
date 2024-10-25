import random

def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) > 0:
            return int(level)
        else:
            print("try again")

def get_guess():
    while True:
        guess = input("Guess: ")
        if guess.isdigit() and int(guess) > 0:
            return int(guess)
        else:
            print("try again")

def main():
    level = get_level()
    target = random.randint(1, level)


    while True:
        guess = get_guess()

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()

import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0

        while True:
            answer = input(f"{x} + {y} = ")
            if answer.isdigit():
                answer = int(answer)
                if answer == correct_answer:
                    score +=1
                    break
                else:
                    tries += 1
                    if tries == 3:
                        print("EEE")
                    else:
                        print("EEE")
            else:
                print("try again")
        print(f"Score: {score}/10")


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) in [1, 2, 3]:
            return int(level)
        else:
            print("try again")



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()

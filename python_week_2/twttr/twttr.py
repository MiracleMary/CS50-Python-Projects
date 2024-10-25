def main():
    user_input = input("Input: ")

    vowels = "aeiouAEIOU"

    result = ""
    for letter in user_input:
        if letter not in vowels:
            result += letter
    print ("output:", result)


if __name__ == "__main__":
        main()

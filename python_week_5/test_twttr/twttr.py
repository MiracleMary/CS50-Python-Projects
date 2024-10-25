def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print ("output:", result)

def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result



if __name__ == "__main__":
        main()

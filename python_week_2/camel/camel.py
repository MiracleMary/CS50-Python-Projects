def main():
    camel_case = input ("CamelCase: ")
    snake_case = convert(camel_case)
    print ("snake_case:", snake_case)

def convert(camel_case):
    snakecase = " "
    for case in camel_case:
        if case.isupper():
            snakecase += "_" + case.lower()
        else:
            snakecase += case
    return snakecase.lstrip("_")




if __name__ == "__main__":
     main()

def main():
    amount = 0

    while amount <50:
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            amount += coin
            print("Amount Due:", 50 - amount)
        else:
             print("Amount Due: 50")

    change = amount - 50
    print ("Change Owed:", change)


if __name__ == "__main__":
        main()


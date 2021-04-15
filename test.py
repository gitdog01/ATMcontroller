import ATMcontroller


class User:
    def __init__(self, PIN, balance) -> None:
        self.PIN = PIN
        self.balance = balance


def checkPIN(pin, user) -> bool:
    if pin == user.PIN:
        return True
    else:
        return False


def cardReader():
    return User("1111", 1000)


def bank():
    return


def test():
    cashBin = 3000

    print("Please insert your card")
    card = cardReader()
    if not card:
        print("Failed to read the card")
        return -1

    print("Please enter your PIN")
    pin = input()
    if not checkPIN(pin, card):
        print("incorrect PIN")
        return -2

    select = 0
    while True:
        print("Please choose menu\n1.Withdraw\n2.Deposit\n3.Balance\n4.End\n")
        select = int(input())

        if select == 1:
            print("Please enter the amount you want")
            cash = int(input())
            if cash > cashBin:
                print("Please ask the bank about ATM.")
                return -3
            status, money = ATMcontroller.Withdraw(cash, card)
            if status == 1:
                print(money, "$ has been withdrawn.")
                cashBin -= money
            elif status == -1:
                print("Not enough balance in your card")

        elif select == 2:
            print("Please put the money in the machine")
            cash = int(input())
            cashBin += cash
            status = ATMcontroller.Deposit(cash, card)
            if status == 1:
                print("Done")
            else:
                print("Fail")

        elif select == 3:
            print("your balance is", ATMcontroller.Balance(card))

        elif select == 4:
            print("goodbye")
            return 1

        else:
            print("wrong number")


test()

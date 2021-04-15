def Withdraw(cash, user):
    if user.balance >= cash:
        user.balance -= cash
        return [1, cash]
    else:
        return [-1, 0]


def Deposit(cash, user):
    user.balance += cash
    return 1


def Balance(user):
    return user.balance

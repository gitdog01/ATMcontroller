# ATMcontroller

1. clone this project
   `https://github.com/gitdog01/ATMcontroller.git`
2. run `test.py`

if you try to run it in a version older than Python 3.7.2
Temp PIN is "1111"
The test consider cash bin

### ATMcontroller.py

ATMcontroller has 3 methods

1. Withdraw(cash, user)

- This is a function that withdraw money.
- `cash` means the money put in the ATM.
- `user` means user information in card.
- The function return `[status,money]`
  - `status` means that it worked properly.
  - `money` means that if it worked, how much money should be withdrawn.

2. Deposit(cash, user)

- This is a function that deposits money.
- `cash` means the money put in the ATM.
- `user` means user information in card.
- The function return `status`
  - `status` means that it worked properly.

3. Balance(user)

- This is a function that check the money.
- `user` means user information in card.
- The function return `balance`
  - `balance` means that balance in your card

### test.py

This is the ATM situation using my ATMcontroller

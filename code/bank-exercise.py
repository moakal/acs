# bank exercise
# 15/06/2022

class bankAccount():
    def __init__(self, accountName = 'Current Account', balance = 200):
        self.__accountName = accountName
        self.__balance = balance

    def balanceGetter(self):
        print(self.__balance)

    def balanceSetterWithdraw(self, value):
        if value < self.__balance:
            self.__balance -= value
            print('New balance is ' + str(self.__balance))
        else:
            print('Not enough funds')

accountObject = bankAccount()

while True:
    menuOption = int(input('1. Check Account Balance\n2. Withdraw funds\n'))
    if menuOption == 1:
        accountObject.balanceGetter()
    elif menuOption == 2:
        value =  int(input('How much would you like to withdraw? '))
        accountObject.balanceSetterWithdraw(value)
    else:
        print('Wrong menu choice')
        

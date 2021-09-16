class Atms(object):
    def __init__(self,pinnumber,cardnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawl amount "+str(amount) +
        ". Your remaining balance is "+ str(new_amount))

def code():
    Cardnumber = input("insert your card number:-  ")
    Pinnumber = input("enter your pin number:-  ")

    new_user = Atms(Cardnumber ,Pinnumber)

    print("Choose your activity  ")
    print("1. BALANCE ENQUIRE    2.WITHDRAWL")
    activity = int(input("Enter activity number:-  "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input(" Enter the amount:-  "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")

code()
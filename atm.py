class atm(object):
   def __init__(self, cardNumber, pin):
       self.cardNumber = cardNumber
       self.pin = pin

   def checkBalance(self):
       print("You have 1 million dollars in your back account.")
        
   def withdraw(self, amount):
        newAmount = 1000000 - amount       
        print("Your have withdrawn " + str(amount) + " dollars from you bank account. Your remaining balance is $" + str(newAmount))

def main():
    cardNumber = input("Type your card number: ")
    pinNumber = input("Type your pin number: ")
    user = atm(cardNumber, pinNumber)
    act = int(input("What you want to do?\n1. Check Blance or 2. Withdraw money?\nType 1 or 2: "))

    if(act==1):
        user.checkBalance()

    elif (act==2):
        ammount = int(input("Enter amount to withdraw: "))
        user.withdraw(ammount)

    else:
        print("Enter a valid activity number")

if __name__ == "__main__":
    main() 
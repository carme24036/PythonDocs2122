#Carmen
#EZBank 1
import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000
app.balance = int(app.balance)

app.running = True

while app.running == True:
    userAnswer = input("1, 2, or 3?")
    userAnswer = int(userAnswer)
    if userAnswer == 1:
        userDeposit = input("How much would you like to deposit? ")
        userDeposit = int(userDeposit)
        app.balance = (app.balance + userDeposit)
        print(app.balance)
    elif userAnswer == 2:
        userWithdraw = input("How much would you like to withdraw? ")
        userWithdraw = int(userWithdraw)
        if userWithdraw > app.balance:
            print("You don't have enough money.")
        else:
            app.balance = (app.balance - userWithdraw)
            print(app.balance)
    elif userAnswer == 3:
        app.running = False
    else:
        print("Your choice was invalid.")

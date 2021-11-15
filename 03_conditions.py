#Carmen

# Practice using expressions and conditional statements

# An expression is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 5 + 5

# Functions/methods must be resolved as expressions as well
answer = input("What is your name?")

# Comparison expressions reslove as True/False
print ( 7 > 7 )
print (7 >= 7 )
print ( x == 10 )
print (x > 10 or x < 10 )

# A conditional statement runs if its condition is True / not False
if answer  == "Bob" :
    print ("Hello Bob! Welcome back.")
    print ("This line also prints if your name is Bob.")
elif answer == "Vadim" :
    print ("Hey! You still owe me money!")
else:
    print ("Sorry, I only talk to Bob.")
print ("This line isn't inside the if statement, and prints regardless.")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not True
# ^ You can have as many elif's as you want
# ^ Else runs if no prior conditions were True

age = input("What is your age?")
age = int(age)
if age >=10 :
    print ("Heres your license")
elif age == 9 :
    print ("You have one more year")
else :
    print ("You are too young")






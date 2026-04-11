

#! Snake water and gun

import random

"""
1 for snake
-1 for water
0 for gun
"""


computer = random.choice([1,-1,0])

youStr = input("Enter your choice -> ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}

you = youDict[youStr]

print(f"The chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(you == computer):
    print("draw")
else:
    if(computer == -1 and you == 1):
        print("you win")
    elif(computer== -1 and you == 0):
        print("you loose")
    elif(computer == 0 and you == -1):
        print("you win")
    elif(computer == 0 and you == 1):
        print("You Loose")
    elif(computer==1 and you ==-1):
        print("You Loose")
    elif(computer== 1 and you ==0):
        print("You Win")
    else:
        print("Something went wrong")

#! 05:46:00
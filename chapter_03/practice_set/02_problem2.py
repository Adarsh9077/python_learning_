
#! 02 Practice set____
from datetime import datetime
name = input("Enter your name --> ")

now =  datetime.now()

greeting = '''Dear <|name|>,
You are selected as a Ai Software Engineer.
You can join to <|date|>'''
day = 0
month = 0
year = 0
if(now.day+20> 30):
    day = 20-(30-now.day)
    month = now.month+1
    year = now.year
    print(f" ----> {day}")
    if (month> 12 ):
        month = 1
        year = year +1



joining_date = f"{now.day}"


print(greeting.replace("<|name|>",name).replace("<|date|>",f"{day}/{month}/{year}"))
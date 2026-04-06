
#! Greatest no. find using functions


def greatestNoFind():
    a = int(input("Enter a first no.:-> "))
    b = int(input("Enter a second no.:-> "))
    c = int(input("Enter a third no.:-> "))
    
    if(a> b and a>c):
        print(f"the greatest no. is : {a}")
        return a
    elif (b>a and b>c):
        print(f"the greatest no. is : {b}")
        return b
    elif (c>a and c>b):
        print(f"the greatest no. is : {c}")
        return c
        
        
        
greatestNoFind()
print("_______________________")
greatestNoFind()
print("_______________________")
greatestNoFind()
print("_______________________")
greatestNoFind()
print("_______________________")
greatestNoFind()


#! 05:19:15
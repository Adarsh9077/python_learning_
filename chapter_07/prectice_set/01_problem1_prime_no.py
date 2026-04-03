
#!  Find prime No.


n = int(input("Enter a Number -> "))

for i in range (2,n):
    if((n%i) == 0):
        print("This number is not prime")
        break
    
    else:
        print("This no. is prime")

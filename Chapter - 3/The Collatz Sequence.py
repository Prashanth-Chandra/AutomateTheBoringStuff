def collatz(num):
    if(num!=1):
        if(num%2==0):
            x=num//2
            print(x)
            collatz(x)
        else:
            x=3*num+1
            print(x)
            collatz(x)
    else:
        return 0
try:
    collatz(int(input('Enter Number : \n')))
except ValueError:
    print("Enter an Integer")

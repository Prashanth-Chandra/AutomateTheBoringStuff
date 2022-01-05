import pyinputplus as pyip
def fibbo(n,token):
    a=0
    b=1
    c=0
    if(token==1):
        print(a,end=' ')
    for i in range(0,n):
        a=b
        b=c
        c=a+b
        if(token==1):
            print(c,end=' ')
    if token==2:
        print(c)
n=pyip.inputNum("Enter the value of n : ",min=2)
print("\t=-=-=-=-=Options=-=-=-=-=")
print(" Enter 1 if you want to know the first %d fibbonaci numbers"%(n))
print(" Enter 2 if you want to know the %dth fibbonaci number"%(n))
token=pyip.inputNum("Enter your choice : ",min=1,max=2)
fibbo(n,token)



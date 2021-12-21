import re

date=re.compile(r'^([1-2][0-9]|3[0-1]|[0])\/(1[0-2]|0[1-9])\/([1-2][0-9][0-9][0-9])')
a=input()
store=date.search(a)
cont=0
isValid=True
try:
    day=int(store.group(1))
    month=int(store.group(2))
    year=int(store.group(3))
except:
    cont=1
    isValid=False
if(cont==0):
    if((month in [4,6,9,11]) and day>30):
        isValid=False
    if((year%4==0 or (year%100==0 and year%400==0) and month==2)):
        if(day>29):
            isValid=False
    if((year%4!=0 or year%100==0) and month==2):
        if(day>28):
            isValid=False
    if((month in [1,3,5,7,8,10,12]) and day>31):
        isValid=False

print(isValid)
    

import re
password=input()
c_lo=re.compile(r'[a-z]')
c_up=re.compile(r'[A-Z]')
c_di=re.compile(r'\d')
lo=len(c_lo.findall(password))
up=len(c_up.findall(password))
di=len(c_di.findall(password))
if(len(password)>=8 and lo>1 and up>1 and di>1):
    print("Strong Password")
else:
    print("Not a Strong Password")

import re,os
from pathlib import Path
p=Path('G:\Automate The Boring Stuff\Chapter - 1')
l=[]
string=input("Enter the text you want to search ")
for textfile in p.glob('*.txt'):
    x=open(textfile)
    c=x.read()
    if string in c:
        l.append(textfile)
print(l)
    
    

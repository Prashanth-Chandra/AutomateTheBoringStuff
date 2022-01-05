import os,re,shutil

date=re.compile(r"^(.*)?(\d\d)-(\d\d)-(\d\d\d\d)(.*)?$")
for fileName in os.listdir('.'):#'.' is for the current directory
    d=date.search(fileName)
    if(d==None):
        continue
    start=d.group(1)
    a=d.group(2)
    b=d.group(3)
    c=d.group(4)
    end=d.group(5)
    print(a,b,c)
    eurodate=start
    if(int(b)>12 and int(a)<32):
        eurodate+=b+'-'+a+'-'+c
    else:
        eurodate+=a+'-'+b+'-'+c
    eurodate+=end
    wkdir=os.path.abspath('.')
    originalFileName=os.path.join(wkdir,fileName)
    finalFileName=os.path.join(wkdir,eurodate)
    shutil.move(originalFileName,finalFileName)

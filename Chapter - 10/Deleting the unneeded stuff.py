import os
from pathlib import Path
cnt=0
for folder,subfolder,files in os.walk('C:\\Users\\SUREKHA\\Downloads'):
    for filenames in files:
        x=Path(folder)/filenames
        if(os.path.getsize(x)>100*1024*1024):
            print("File size : ",round((os.path.getsize(x))/(1024*1024),2)," MB")
            print('\t',x)
            cnt+=1
print("Total Number of Files Above 100MB : ",cnt)

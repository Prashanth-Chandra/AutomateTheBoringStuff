import zipfile,os
from pathlib import Path
#This program is to create a zip file and add all my screenshots( png files) form
#my Computer System Essentials Labsheet Folder to it.
path=Path.home()
zipf=zipfile.ZipFile('Labsheet_5_Screen_Shots.zip','w')
x=Path(r'C:\Users\SUREKHA\Desktop\Labsheet 5')
for folder,subfolder,files in os.walk("C:\\Users\\SUREKHA\\Desktop\\Labsheet 5"):
    for filenames in files:
        a=os.path.splitext(filenames)
        xf=x/filenames
        if(a[1].lower()=='.png'):
            zipf.write(xf,compress_type=zipfile.ZIP_DEFLATED)
            print("Added ",filenames," to the zip file")
zipf.close()

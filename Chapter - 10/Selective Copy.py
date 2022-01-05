import os,shutil,pathlib
ext=input("Enter the extension that you want to copy (without the '.') : ")
path=pathlib.Path('G:\\Automate The Boring Stuff')
cnt=0
os.mkdir(pathlib.Path('G:\\')/'CopiedItems')
for folder,subfolder,files in os.walk(path):
    for filenames in files:
        a=os.path.splitext(filenames)
        x=pathlib.Path(folder)/filenames
        if(a[1]=='.'+ext):
            shutil.copy(x,path/'CopiedItems')
            cnt+=1
            print("Copied ",filenames," to ",path)
print("Copies ",cnt," files with extension .",ext," to ",path,"\CopiedItems")

import os
for folder,subfolder,files in os.walk('G:\\Automate The Boring Stuff'):
    print("The current folder is ",folder)
    for subfoldernames in subfolder:
        print("Subfolder of ",folder," : ",subfoldernames)
    for filenames in files:
        print("File of ",folder," : ",filenames)
# forloop explanation for reference
# let there be 10 folders each having 10 subfolders and 10 files in each folder and subfolder
# => [0][0][0]
#[1][0][0]
#[2][0][0]
#...
#[10][0][0]
#[1][0][1]
#[1][0][2]
#[1][0][3]
#...
#[1][0][10]
#[1][1][0]
#[1][2][0]
#...
#[1][10][0]
#[1][1][0]
#[1][1][1]
#...
#...
#[10][9][0]
#[10][10][0]
#[

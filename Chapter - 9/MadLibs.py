import shelve, re
from os import read
from pathlib import Path
text = open(Path('G:\\Automate The Boring Stuff\\Chapter - 9')/'file.txt')
content = text.read()
text.close()
while True:
    items=re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    found=items.search(content)
    #print(found)
    if(found != None):
        x="Enter a/an "+str(found.group()+" : ")
        rep=input(x)
        content=content.replace(found.group(),rep,1)#(word to be replaced, the word that should replace, number of times should it be prelaced)
    else:
        break
text=open(Path('G:\\Automate The Boring Stuff\\Chapter - 9')/'file_ans.txt' , 'w')#file_ans can be changed to file to overwite the actual file
text.write(content)
text.close()

#print(content)

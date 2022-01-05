#downloading romeo and juliet
import requests
book=requests.get("https://automatetheboringstuff.com/files/rj.txt")
try:
    book.raise_for_status()
except:
    print("Error Has been found \nError",book.status_code)
    sys.exit()
savebook=open('Romeo and Juliet.txt','w')#to use the commented code change the 'w' to 'wb'(write binary)
text=book.text
print(text)
savebook.write(text)#even this works
#for chunk in book.iter_content(100000):
        #savebook.write(chunk)
savebook.close()

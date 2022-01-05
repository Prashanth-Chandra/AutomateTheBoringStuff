import requests,bs4,pprint
examplefile=open('example.html','r')
res=examplefile.read()
examplefile.close()

resSoup=bs4.BeautifulSoup(res,'html.parser')
author=resSoup.select('p')
print(len(author))
pprint.pprint(author)

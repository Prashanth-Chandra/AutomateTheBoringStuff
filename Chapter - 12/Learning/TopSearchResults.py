#to open top 5 search results
import webbrowser,bs4,requests
x=input("Enter your query : ")
x.replace(" ","+")
#open=webbrowser.open('https://google.com/search?q='+x)
res = requests.get('https://google.com/search?q='+x)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.href')
numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

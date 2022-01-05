import requests,bs4
link_input=input("Enter the website with the appropriate extension: ")
link_input=str("https://")+str(link_input)
res=requests.get(link_input)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')
links=soup.select('a')
for i in links:
    try:
        url=i['href']
        url_checker=requests.get(url)
        print("Checking url : ",url)
        if(url_checker.status_code==404):
            print("Broken url found : \n   ",url)
            print("\n")
    except:
        continue

import requests,bs4,os
url='https://xkcd.com/'
os.makedirs('xkcd',exist_ok=True)
while url[-1]!='#':
    print('Downloading the page :',url)
    res=requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    element=soup.select('#comic img')
    if element==[]:
        print("No image found")
    else:
        comicUrl='https:'+element[0].get('src')
        print("Downloading the image :",comicUrl)
        res1=requests.get(comicUrl)
        res.raise_for_status()
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prevLink=soup.select('a[rel="prev"]')[0]
        url='https://xkcd.com'+prevLink.get('href')
print("Done")

import requests as rq
from bs4 import BeautifulSoup
url = input("Enter the url: ")
if("http" or "https") in url:
    data = rq.get(url)
else:
    data = rq.get("https://"+url)
soup = BeautifulSoup(data.text,"html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))
    
    
with open("data.txt", 'a') as saved:
    print(links[:10],file=saved)
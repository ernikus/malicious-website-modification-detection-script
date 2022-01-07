# importing the libs
from bs4 import BeautifulSoup
import requests


# need the page's url
# returns file with page's HTML
def HTMLscrap(url):

    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    quotes = soup.find_all()
    
    
    file = open("outputHTML.txt", 'w', encoding="utf-8")
    for i in range(0, len(quotes)):
        
        # if data isn't string -> make that string
        if (type(quotes[i])!= str):
            quotes[i] = str(quotes[i])
    
        try:
            file.write(quotes[i])
            
        # if you can't write data to file -> change encoding
        except UnicodeEncodeError:
            quotes[i] = quotes[i].encode('UTF-8').decode('WINDOWS-1252')
            file.write(quotes[i])

    file.close()


# url="https://www.paniswojegoczasu.pl/blog/"

# HTMLscrap(url)

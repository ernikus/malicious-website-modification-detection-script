# importing the libraries
from bs4 import BeautifulSoup
import requests

def HTMLscrap(url):

    data = requests.get(url)
    #data = data.encode('UTF-8')#.decode('WINDOWS-1250')
    soup = BeautifulSoup(data.content, "html.parser")
    quotes = soup.find_all()
    
    f = open("outputHTML.txt", 'w', encoding="utf-8")
    for i in range(0, len(quotes)):
        if (type(quotes[i])!= str):
            quotes[i] = str(quotes[i])
        try:
            #print(quotes[i])
            f.write(quotes[i])
        except UnicodeEncodeError:
            quotes[i] = quotes[i].encode('UTF-8').decode('WINDOWS-1252')
            #print(quotes[i])
            f.write(quotes[i])
            
    # testing saving data to file
    #f = open("outputHTML.txt", 'w')
    #f.write(data.text)
    f.close()


url="https://www.paniswojegoczasu.pl/blog/"

HTMLscrap(url)

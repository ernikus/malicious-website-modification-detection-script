# importing the libraries
from bs4 import BeautifulSoup
import requests

def HTMLscrap(url):

    data = requests.get(url)

    # testing saving data to file
    f = open("outputHTML.txt", 'w')
    f.write(data.text)
    f.close()


url="https://htmlsave.com/"

HTMLscrap(url)

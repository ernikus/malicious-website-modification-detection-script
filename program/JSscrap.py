#importing the libs
from helium import *
import requests
from bs4 import BeautifulSoup

# need the page's url
# returns file with page's JS
def JSscrap(url):

    browser = start_firefox(url, headless=True)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    quotes = soup.find_all('script')

    file = open("outputJS.txt", 'w', encoding="utf-8")
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
    
    
# url = "https://www.paniswojegoczasu.pl/blog/"

# JSscrap(url)

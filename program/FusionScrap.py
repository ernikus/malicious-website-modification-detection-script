#importing the libs
from helium import *
from bs4 import BeautifulSoup
import requests


# need the page's url
# returns file with page's JS
def FusionScrap(url):

    browser = start_firefox(url, headless=True)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    # HTML Part ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    quotes = soup.find_all()
    
    file1 = open("outputHTML.txt", 'w', encoding="utf-8")
    for i in range(0, len(quotes)):
        
        # if data isn't string -> make that string
        if (type(quotes[i])!= str):
            quotes[i] = str(quotes[i])
            
        try:
            file1.write(quotes[i])
            
        # if you can't write data to file -> change encoding
        except UnicodeEncodeError:
            quotes[i] = quotes[i].encode('UTF-8').decode('WINDOWS-1252')
            file1.write(quotes[i])

    file1.close()
    
    # JS Part   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    quotes = soup.find_all('script')

    file2 = open("outputJS.txt", 'w', encoding="utf-8")
    for i in range(0, len(quotes)):
        
        # if data isn't string -> make that string
        if (type(quotes[i])!= str):
            quotes[i] = str(quotes[i])
            
        try:
            file2.write(quotes[i])
           
        # if you can't write data to file -> change encoding 
        except UnicodeEncodeError:
            quotes[i] = quotes[i].encode('UTF-8').decode('WINDOWS-1252')
            file2.write(quotes[i])
            
    file2.close()
    
    
url = "https://www.paniswojegoczasu.pl/blog/"

FusionScrap(url)

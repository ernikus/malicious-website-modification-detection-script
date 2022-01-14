#importing the libs
from bs4 import BeautifulSoup
import requests
from PathFinder import PathFinder
from hashowanie import hashowanie

# need the page's url
# returns file with page's JS
def FusionScrap(url):
    path = PathFinder()

    data = requests.get(url)
    soup = BeautifulSoup(data.content, features="lxml")
    
    # with open("out.txt", 'w', encoding="utf-8"):
    #     print(soup)

###DOBRE
    
    # HTML Part ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    quotes = str(soup)

    pathf1 = path + "outputHTML.txt"

    file1 = open(pathf1, 'w', encoding="utf-8")
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
    
    # trial_data = str(soup)
    quotes = soup.find_all('script')
    
    pathf2 = path + "outputJS.txt"
    pathf3 = path + "hash.txt"
    file2 = open(pathf2, 'w', encoding="utf-8")
    file3 = open(pathf3, 'w', encoding="utf-8")
    for i in range(0, len(quotes)):
        line_no = i+1
        # if data isn't string -> make that string
        if (type(quotes[i])!= str):
            quotes[i] = str(quotes[i])

        try:
            file2.write("hash nr %d:" % line_no)
            file2.write("\n")
            file2.write(quotes[i])
            file2.write("\n")
            file2.write("\n")
            file3.write(hashowanie(quotes[i]))
            file3.write("\n")

        # if you can't write data to file -> change encoding
        except UnicodeEncodeError:
            quotes[i] = quotes[i].encode('UTF-8').decode('WINDOWS-1252')
            file2.write("hash nr %d:" % line_no)
            file2.write("\n")
            file2.write(quotes[i])
            file2.write("\n")
            file2.write("\n")
            file3.write(hashowanie(quotes[i]))
            file3.write("\n")

    file2.close()
    file3.close()

    return(pathf1, pathf2)


# url = "http://127.0.0.1:8080/"

# path = PathFinder()
# print(path)

# FusionScrap(url)

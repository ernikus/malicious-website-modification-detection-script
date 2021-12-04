import requests
from bs4 import BeautifulSoup

URL = "https://www.paniswojegoczasu.pl/blog/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

quotes = soup.find_all('script')

result_file = open("strona.txt", 'w')
for i in range(0, len(quotes)):
    if (type(quotes[i])!= str):
        quotes[i] = str(quotes[i])
    try:
        result_file.write(quotes[i])
    except UnicodeEncodeError:
        quotes[i] = quotes[i].encode('UTF-8').decode('WINDOWS-1252')
        result_file.write(quotes[i])
result_file.close()

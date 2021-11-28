#JS znajduje sie w <script>...</script> w kodzie strony razem z kodem HTML

#tutaj mamy wyciac te fragmenty kodu

# zaczyna sie od <script
# konczy na </script>


from helium import *
from bs4 import BeautifulSoup

# print to file
import sys

url = "https://htmlsave.com/"

browser = start_firefox(url, headless=True)

soup = BeautifulSoup(browser.page_source, 'html.parser')


quotes = soup.find_all('script')

# print jest dobry
# tylko trzeba to jakos dobrze zapisac do pliku :/

# nie dziala
# with open("temsJS.txt", 'w') as output_file:

for item in quotes:
    print(item)


result_file = open("quotes.txt", 'w')
result_file.write(str(quotes))
result_file.close()
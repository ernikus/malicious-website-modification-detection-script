import urllib.request

pobrany_kodstrony = urllib.request.urlopen("https://google.com")

czysty_kod = data.read().decode('windows-1252') #ewentualnie utf-8, ale to bedzie wszystko tlumaczyc
print(czysty_kod)

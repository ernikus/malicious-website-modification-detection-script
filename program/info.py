#zmienna globalna 'tekst' przechowuje jako tabela wszystkie informacje jakie mają być przekazane
#zmienna globalna 'mail' aby wiedzieć na jaki email wysłać mail
#zmienna globalna 'password' hasło do poczty email z której email będzie wysłany (w ten sposób możnaby też samemu komuś wysyłać maile)

#email wysyła email do użytkownika, jednak zanim to to chcąc użyć skrzynke na google trzeba włączyć dostęp do mniej
#bezpiecznych aplikacji

#info pobiera dane do wyświetlenia na ekranie i je pokazuje. Po za tym dodaje też te elementy do zmiennej 'tekst'
#przez co można wywołać na końcu już tylko funkcje email

#na początku skryptu należy wyzerować zmienną tekst

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def email(plik, plik1, mail="", password=""):

    print(os.path.isfile(plik1))

    plik = open(plik, 'r')
    plik1 = open(plik1, 'r')
    inf = plik.readlines()
    inf1 = plik1.readlines()
    plik.close()
    plik1.close()
    tek = []; tek1=[]
    for line in inf:
        tek.append(line)
    for line in inf1:
        print(line)
        tek1.append(line+"\n")

    print(tek1)

    message = ''.join(tek)
    message1 = ''.join(tek1)
    msg = MIMEMultipart()
    msg['From'] = 'Skrypt wykrywający zmiany stron www'
    msg['To'] = mail
    msg['Subject'] = 'Możliwość ataku na twoją strone internetową!'
    message = "Na twojej stronie internetowej zostały znalezione poniższe zmiany:\
    \n" + message + "\n" + message1 +"\nW razie wątpliwości zaleca się sprawdzenie podanych elementów.\
    \n\nPozdrawia team ZiT"
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(mail, password)
    mailserver.sendmail(mail, mail, msg.as_string())
    mailserver.quit()

def info(plik):
    plik = open(plik, 'r')
    inf = plik.readlines()
    plik.close()
    tek = []
    for line in inf:
        tek.append(line)
    try:
        for line in tek:
            print(line)
        #else:
            #print("Brak zmian")
    except:
        print("Problem z zmienną do wysłania do administratora")


#mail = ""
#password = ""
#tekst = []  #zmienna globalna
#info()
#x="123"
#info(x)
#x=456
#info(x)
#email()

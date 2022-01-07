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

def email():
    global tekst
    global mail
    global password
    
    if(len(tekst)<1):
        print("Nie znaleziono żadnych zmian")
    else:
        message = ''.join(tekst)
        msg = MIMEMultipart()
        msg['From'] = 'Skrypt wykrywający zmiany stron www'
        msg['To'] = mail
        msg['Subject'] = 'Możliwość ataku na twoją strone internetową!'
        message = "Na twojej stronie internetowej zostały znalezione poniższe zmiany:\
        \n" + message + "\nW razie wątpliwości zaleca się sprawdzenie podanych elementów.\
        \n\nPozdrawia team ZiT"
        msg.attach(MIMEText(message))

        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(mail, password)
        mailserver.sendmail(mail, mail, msg.as_string())
        mailserver.quit()

def info(tek=""):
    global tekst
    tek=str(tek)
    try:
        if(len(tek)>1):
            print(tek)
            tekst.append(tek)
            tekst.append('\n')
        #else:
            #print("Brak zmian")
    except:
        print("Problem z zmienną do wysłania do administratora")

        

mail = ""
password = ""
tekst = []  #zmienna globalna
info()
x="123"
info(x)
x=456
info(x)
email()

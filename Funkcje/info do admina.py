#dać zmienną globalną która po porównaniu kodów html
#zmieni swoją wartość co spowoduje wysłanie że ponownie wywołana funkcja
#zamiast dopisać tekst wyświetli go/wyśle go jako mail do admina

#sprawdzić czy po wyjściu z funkcji tekst zapisany w zmiennej jest tam dalej
#czy po dopisaniu tekstu zostanie wyświetlony tylko ten nowy?
#jeśli nowy, to ustawić jako drugą zmienną globalną tekst do którego
#będzie zapisywany tekst do wyświetlenia

#Można zrobić że jeśli wgl nie będzie zmian czyli tek będzie pusty to wyświetlić
#tekst "brak zmian"

#a na początku skryptu obie zmienne będą zerowane
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(wiadomosc):
    msg = MIMEMultipart()
    msg['From'] = 'mail'
    msg['To'] = 'mail'
    msg['Subject'] = 'simple email in python'
    message = "Witam!\n Na twojej stronie internetowej zostały znalezione poniższe zmiany:\
    \n" + wiadomosc + "W razie wątpliwości zaleca się sprawdzenie podanych elementów."
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('mail', 'hasło')

    mailserver.sendmail('mail','mail',msg.as_string())

    mailserver.quit()

def info(tek=""):
    global tekst
    global mail
    if(len(tek)>1):
        print(tek)
        tekst.append(tek)
        tekst.append('\n')
    else:
        print("Brak zmian")
        
    if(mail==1):
        if(len(tekst)<2):
            print("Nie znaleziono żadnych zmian")
        else:
            tekst = tekst[0 : (len(tekst)-1)]
            mess = ''.join(tekst)
            mail(mess)

#tekst = []  #zmienna globalna
#mail=0      #zmienna globalna
#info()
#x="123"
#info(x)
#x="456"
#mail=1
#info(x)


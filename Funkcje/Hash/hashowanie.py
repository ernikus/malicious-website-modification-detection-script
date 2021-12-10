import hashlib

def hashowanie(tekst):
    encoded = tekst.encode()
    wynik = hashlib.sha512(encoded).hexdigest()
    return wynik

#print(hashowanie());
#print();
#print(hashowanie('kod zrodlowy strony http'));

#funkcja przyjmuje jako argument dowolny element.
#Zwraca natomiast wynik hashowania w postaci szesnastkowej

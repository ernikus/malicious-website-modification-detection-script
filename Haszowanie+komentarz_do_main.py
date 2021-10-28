import hashlib

#kod_zródłowy - kod obserwowanej strony
kod_zródłowy = "aerghbaerigu"

# stworzenie hasha  | możnaby to nawet dać po prostu jako funkcje czy fragment innego większego kody (niekoniecznie main)
Hash = hashlib.sha224(kod_zrodlowy).hexdigest()


#Ta pętla byłaby dobra żeby ją wykorzystać w main aby co jakiś odstęp czasu sprawdzała strone
#Tylko dać już tutaj wykorzystanie funkcji jak np tej do haszowania, porównania etc
#Możnaby wtedy rozbudować też Exceptions no i wiadomo też komunikacje z użytkownikiem

while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
          
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
          
        # wait for 30 seconds
        time.sleep(30)
          
        # perform the get request
        response = urlopen(url).read()
          
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
  
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
  
        # if something changed in the hashes
        else:
            # notify
            print("something changed")
  
            # again read the website
            response = urlopen(url).read()
  
            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()
  
            # wait for 30 seconds
            time.sleep(30)
            continue
              
    # To handle exceptions
    except Exception as e:
        print("error")

# Malicious Website Modification Detection Script

¯ \ _(ツ) _ /¯

## ❗❗❗ PRESENTATION INFO ❗❗❗
 - url:  http://127.0.0.1:8080/
 - mail:  ''
 - password:  ''
 - d: 0
 - h: 0.0042

## Requirements

 - OS: **Linux**
 - Language: **Python 3**
 - Installed Additional Library for Python 3: **Beautiful Soup**
 - Installed **Docker**
 - Installed **Nginx**
 - Installed **Firefox Browser** [installed by default in most Linux Distros]
 - Access to the **Internet** - Download Nginx Image for Docker
 - Access to **Administrator Account** for Setting Docker Containers and Right Privileges
 - Aby otrzymywać maile na skrzynke gmail - włączyć "Dostęp mniej bezpiecznych aplikacji

## Warning

**Powtarzające się linie w kodzie strony mogą powodować nieprawidłowe informacje dot. numeru linii, w której nastąpiła zmiana**

## Roadmap

 - [x] Basic Concept
 - [x] Research
 - [x] Brainstorm
 - [x] Control Meeting
 - [x] More Advanced Concept [with creating Roadmap]
 - [x] Create Script
	 - [x] Wprowadzenie URL
	 - [x] Odczyt ostatnich danych
	 - [x] Pobranie kodów HTML i .JS
	 - [x] Hashowanie .JS
	 - [x] Porównanie .JS
	 - [x] Porównanie HTML (w tym dalsza analiza)
	 - [x] Poinformaowanie tekstowe (ew. + mailowe) adminisitratora
	 - [x] Zapisanie wszystkich kodów do folderu
	 - [x] Pętla całego skryptu
 - [x] Create Test WebPage
	 - [x] Original Page (with more JS)
	 - [x] Small HTML Change Page
	 - [x] Big HTML Change Page
	 - [x] Small JS Change Page
	 - [x] Big JS Change Page
	 - [x] Hacker Rick Break Page
	 - [x] Create Quick Page Mount Scripts
 - [x] Script Testing
	 - [x] Save Logs and Outputs
	 - [x] Analyse Data
	 - [x] Correct Program
	 - [x] Prevent Errors
 - [x] Create Report
 - [ ] Send a Report
 - [ ] Celebrate 🎉🎉🎉

### ✅ Functions

 - [x] Odczyt Danych		***E***
 - [x] Pobranie HTML		***E***
 - [x] Pobranie JS			***E***
 - [x] Hashowanie JS		***A***
 - [x] Porównanie JS		***A***
 - [x] Porównanie HTML		***E***
 - [x] Info do Admina		***A***
 - [x] Zapis Danych		***A***

## Concept

 1. Wprowadzenie URL naszej strony
 2. Odczytanie poprzedniego zapisanego stanu dla podanej strony
 3. Pobranie kodów źródłowych dla podanej strony  - HTML oraz .JS
 4. Hashowanie każdego kodu .JS
 5. Porównanie hashy .JS
 6. Jeśli nie są równe - informacja do administratora, że plik nie odpowiada swojemu zapisowi
 7. Porównanie kodów HTML
 8. Jeśli nie są równe - dalsza analiza kodów (ignorowanie komentarzy, wykrycie czy zmiana występuje w części HEAD czy BODY), a następnie wysłanie tych informacji do administratora
 9. Jeśli wszystko jest równe - zapisanie wszystkich kodów do folderu
 10. <Program się zapętla>

## Related

Here are some helpfull links from other related projects

[Awesome README](https://github.com/ernikus/sus-changes-on-webpage-script/blob/main/help%20links.txt)


### BONUS

<img src="https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif" height="300"/>

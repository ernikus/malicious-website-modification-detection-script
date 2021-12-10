# Malicious Website Modification detection Script

¯ \ _(ツ) _ /¯


## Roadmap

 - [x] Basic Concept
 - [x] Research
 - [x] Brainstorm
 - [x] Control Meeting
 - [x] More Advanced Concept [with creating Roadmap]
 - [ ] Create Script
	 - [ ] Wprowadzenie URL
	 - [ ] Odczyt ostatnich danych
	 - [ ] Pobranie kodów HTML i .JS
	 - [ ] Hashowanie .JS
	 - [ ] Porównanie .JS
	 - [ ] Porównanie HTML (w tym dalsza analiza)
	 - [ ] Poinformaowanie tekstowe (ew. + mailowe) adminisitratora
	 - [ ] Zapisanie wszystkich kodów do folderu
	 - [ ] Pętla całego skryptu
 - [ ] Create Test WebPage
 - [ ] Script Testing
 - [ ] Create Documentation
 - [ ] Create Report
 - [ ] Send a Report
 - [ ] Celebrate 🎉🎉🎉

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

### ✅ Functions

 - [x] Odczyt Danych		***E***
 - [x] Pobranie HTML		***E***
 - [x] Pobranie JS			***E***
 - [x] Hashowanie JS		***A***
 - [x] Porównanie JS		***A***
 - [x] Porównanie HTML		***E***
 - [x] Info do Admina		***A***
 - [x] Zapis Danych		***A***

## Conversation Script (org.: "Co Trzeba Tak Wstępnie")

lyjnamur:

> *Tak czytając te strony to tak sobie pomyślałem co do tych właśnie
> plików wykorzystywanych przez strone a głównie .js że to raczej rzadko
> się zmienia bo to jest do różnych funkcjonalności strony, tak więc
> tutaj łatwo by było stwierdzić że zmiana/dodanie/usunięcie jakiegoś
> pliku jest dość sporym niebezpieczeństwem. I tak to po prostu by się
> przechowywało hashe tych plików, porównywało z tymi co są aktualnie na
> stronie.*

lyjnamur:

> *A tak jeszcze co do np wyszukiwania jakiś zmian na stronie to np biblioteka BeatifulSoup daje możliwość wyszukiwania każdej lini kodu z
> wyszukiwanym tagiem, co też mogłoby bardzo ułatwić szukanie jakiś
> niebezpieczeństw czy też zmian które np raczej miejsca mieć nie
> powinny.*

ernikus:

> *Ja proponuję poprzestać tylko na Pythonie właśnie z Biblioteką BeatifulSoup lub Requests. Nie rozdrabniajmy się i skupmy się na tylko
> jednym skrypcie - zapomnijmy o JS albo czymś innym. Najlepiej jeśli
> nasz skrypt będzie aż tak bardzo uniwersalny jak to możliwe - żeby
> działał w miarę na wszystkich stronach internetowych a nie tylko
> poszczególnych zrobionych w bazach pokrewnych SQLa.*

ernikus:

> *Musimy pamiętać też o **Stronie Testowej**, na której będziemy testować nasz skrypt!*

ernikus:

> *Dodatkowo do naszych bibliotek możemy opcjonalnie dołączyć PhantomJS (scrap .JS files) ale myślę że głównie sobie poradzimy z BeautifulSoup i Requests. Ogólnie koncept mamy spoko. Materiały i znajomość tego też spoko. Niepokoi jedynie ta autoryzacja - może na spotkaniu w środę coś uda się więcej dowiedzieć :)*



## Related

Here are some related projects

[Awesome README](https://github.com/ernikus/sus-changes-on-webpage-script/blob/main/help%20links.txt)



### BONUS


<img src="https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif" height="300"/>

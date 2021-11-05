
# Malicious Website Modification detection Script

¯ \ _(ツ) _ /¯


## Roadmap

 - [x] Basic Concept
 - [x] Research
 - [ ] Brainstorm
 - [ ] More Advanced Concept [with creating Roadmap]
 - [ ] Create Script
 - [ ] Create Test WebPage
 - [ ] Script Testing
 - [ ] Create Documentation
 - [ ] Create Report
 - [ ] Send a Report
 - [ ] Celebrate 🎉🎉🎉

## Concept
- pobieranie kodu źródłowego strony monitorowanej (tak myśle że dobrze będzie też od razu na tym etapie też usuwać linie które są jako komentarze)

- program do haszowania

- podział kodu na mniejsze części wg tagów


### W Głównym Pliku:
- podanie strony sprawdzanej przez program

- porównywanie hashy jako funkcja

- wczytywanie wcześniej zapisanego stanu strony

- podział kodu na head i body

- odpowiedź do użytkownika: brak zmian lub zmiana (jaka linia/e kodu jest/są inne, wypisać część zmienioną z poprzednią jeśli taka istenieje)

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

> *Ja proponuję poprzestać tylko na Pythonie własnie z Biblioteką BeatifulSoup lub Requests. Nie rozdrabniajmy sie i skupmy się na tylko
> jednym skrypcie - zapomnijmy o JS albo czymś innym. Najlepiej jeśli
> nasz skrypt będzie aż tak bardzo uniwersalny jak to możliwe - żeby
> działał w miarę na wszystkich stronach internetowych a nie tylko
> poszczególnych zrobionych w bazach pokrewnych SQLa.*

ernikus:

> *Musimy pamiętać też o **Stronie Testowej**, na której będziemy testować nasz skrypt!*

## Related

Here are some related projects

[Awesome README](https://github.com/ernikus/sus-changes-on-webpage-script/blob/main/help%20links.txt)

# Malicious Website Modification detection Script

¯ \ _(ツ) _ /¯


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

## Co Trzeba Tak Wstępnie

Tak czytając te strony to tak sobie pomyślałem co do tych właśnie plików wykorzystywanych przez strone a głównie .js że to raczej rzadko się zmienia bo to jest do różnych funkcjonalności strony, tak więc tutaj łatwo by było stwierdzić że zmiana/dodanie/usunięcie jakiegoś pliku jest dość sporym niebezpieczeństwem. I tak to po prostu by się przechowywało hashe tych plików, porównywało z tymi co są aktualnie na stronie.

A tak jeszcze co do np wyszukiwania jakiś zmian na stronie to np biblioteka BeatifulSoup daje możliwość wyszukiwania każdej lini kodu z wyszukiwanym tagiem, co też mogłoby bardzo ułatwić szukanie jakiś niebezpieczeństw czy też zmian które np raczej miejsca mieć nie powinny.

## Related

Here are some related projects

[Awesome README](https://github.com/ernikus/sus-changes-on-webpage-script/blob/main/help%20links.txt)

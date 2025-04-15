# Ohjelmistotekniikka, harjoitustyö
## Pokémon-korttien keräilysovellus

Sovelluksen avulla pystyt tarkkailemaan keräämiäsi Pokémon-kortteja ja lajittelemaan niitä erilaisten ominaisuuksien perusteella. 

## Dokumentaatio-linkit

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

## Käyttöohje
Ohjelma on tarkoitettu käytettäväksi Linux-järjestelmällä. 
Windows toimii myös mutta joudut asentamaan Tkinterin kanssa sopivan sovelluksen itse (esim. XMing)
1. Lataa sovelluksen viimeisin julkaisu
[Release](https://github.com/Karstonner/ot-harjoitustyo/releases/latest)
2. Asenna poetry-riippuvuudet juurihakemistossa:
```bash
poetry install
```
3. Käynnistä sovellus:
```bash
poetry run invoke start
```

## Komennot
1. Testauksen pystyy suorittamaan komennolla:
```bash
poetry run invoke test
```
2. Testikattavuusraportin saa komennolla:
```bash
poetry run invoke coverage-report
```
3. Pylint-tarkistukset suoritetaan komennolla:
```bash
poetry run invoke lint
```
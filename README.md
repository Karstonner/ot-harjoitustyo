# Ohjelmistotekniikka, harjoitustyö
## Pokémon-korttien keräilysovellus

Sovelluksen avulla pystyt tarkkailemaan keräämiäsi Pokémon-kortteja ja lajittelemaan niitä erilaisten ominaisuuksien perusteella. 

## Dokumentaatio-linkit

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

## Käyttöohje
1. Asenna poetry-riippuvuudet juurihakemistossa:
```bash
poetry install
```
2. Käynnistä sovellus:
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
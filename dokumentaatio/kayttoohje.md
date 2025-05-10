# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/Karstonner/ot-harjoitustyo/releases). Valitse **Assets** ja **Source code**.

## Konfiguraatio
Tietokantatiedoston ja csv-tiedoston nimet voi halutessaan vaihtaa **.env**-tiedostossa. Voit löytää ne **data**-hakemistosta. Oletusarvot ovat:
```bash
CARD_FILE=pokemon_cards.json
DB_NAME=pokemon_cards.sqlite
```

## Ohjelman käynnistäminen
Ennen käyttämistä, asenna ohjelman riippuvuudet komennolla:
```bash
poetry install
```
Sovelluksen voi käynnistää komennolla:
```bash
poetry run invoke start
```

## Kotisivu
Sovellus käynnistyy kotisivulle:
![](./kuvat/User_Interface.PNG)

## Uuden kortin luominen
**Add card** -nappula luo uuden näkymän:
![](./kuvat/New_Card.PNG)
Tekstikenttiin kirjoitetaan lisäämäsi kortin ominaisuudet. Kortin lisäämisen voi perua Cancel-napilla ja valmis kortti lähetetään Submit-napilla. Sovellus palauttaa käyttäjän kotisivulle.
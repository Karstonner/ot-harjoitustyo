## Käyttöliittymä
Käyttöliittymä sisältää vain yhden näkymän, johon lisätään sisältöä sen ilmestyessä. "Add Card" tuo esille tekstikentät, joiden sisällön perusteella luodaan uusi kortti. Omistettujen korttien määrä näkyy myös oikeasta yläkulmasta. Kortit tulevat automaattisesti näkyviin, jos niitä on olemassa. Jos niitä taas ei ole, korttilista poistuu näkyvistä. Alla kuva kortin lisäysnäkymästä:
![Käyttöliittymä](./kuvat/User_Interface.PNG)

## Luokkarakenne
Luokkarakenne selviää alla olevasta kuvasta. Config alustaa tietokantatiedoston, jolla on sitten DB_Connection-tiedoston kautta yhteys korttirepositorioon. Initialize vielä alustaa repositorion, jos tietokannassa ei ole mitään olemassa. Repositorio ja käyttöliittymä toisensa kanssa korttien lisäämisessä ja poistamisessa sekä käyttäjän näkymän muokkaamisessa.
![Luokkarakenne](./kuvat/Class_Diagram.PNG)

## Tietojen tallennus
Sovellus pitää yllä pysyvää tallennusta SQLite-tietokannassa, mikä on myös aina käytettävässä muodossa korttirepositoriossa. Tietokannan määrittelee .env-tiedosto, mikä myös mahdollistaa sovelluksen myöhemmän muuttamisen json-tiedostojen lukemiseen. Tietokanta alustetaan aina sovelluksen käynnistyessä, jotta se on aina olemassa muttei olemassa olevaa tietoa korvata. 

## Sekvenssikaavio
Alla on sekvenssikaavio, joka esittelee kortin lisäämistä ja poistamista. (Muokkaan tätä vielä lopulliseen palautukseen, koska tämä on vanhentunut. Lisään tällöin myös muita kaavioita). Sovelluksen käyttöliittymä ottaa yhteyden tietokantaan ja tuo käytettäväksi korttirepositorion. Korttilistan saa get_cards-komennolla, uuden kortin saa lisättyä add_new-komennolla ja kortin saa poistettua remove_card-komennolla. Muutokset voidaan huomata joka kerta, kun get_cards-komentoa kutsutaan, mikä taas näyttäytyy käyttöliittymässä automaattisesti.
![Sekvenssikaavio](./kuvat/SequenceDiagram.PNG)
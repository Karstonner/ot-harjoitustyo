classDiagram
	Monopolipeli "1" -- "2" Noppa
	Monopolipeli "1" -- "1" Pelilauta
	Monopolipeli "1" -- "1" Ruutu : aloitusruutu
	Monopolipeli "1" -- "1" Ruutu : vankila
	Pelilauta "1" -- "40" Ruutu
	Ruutu "1" -- "1" Ruutu : seuraava
	Ruutu "1" -- "0..8" Pelinappula
	Pelinappula "1" -- "1" Pelaaja
	Pelaaja "2..8" -- "1" Monopolipeli
	Pelaaja "1" -- "1" Raha
	Ruutu <|-- Aloitusruutu
	Ruutu <|-- Vankila
	Ruutu <|-- Erityisruutu
	Erityisruutu <|-- Sattuma
	Erityisruutu <|-- Yhteismaa
	Ruutu <|-- OmistettavaRuutu
	OmistettavaRuutu <|-- Asema
	OmistettavaRuutu <|-- Laitos
	OmistettavaRuutu <|-- Katu
	OmistettavaRuutu "1" -- "0..1" Pelaaja : omistaja
	Katu "1" -- "0..4" Rakennus : talo
	Katu "1" -- "0..1" Rakennus : hotelli
	Sattuma "1" -- "1..`*`" Kortti
	Yhteismaa "1" -- "1..`*`" Kortti
	Kortti "1" -- "1" Toiminto
	
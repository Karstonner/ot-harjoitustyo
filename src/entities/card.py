class Card:
    """Luokka, joka tuo kortin käsiteltävään muotoon.

    Attributes:
        pokemon: pokemonin nimi
        pokedex_number: pokemonin dex-numero
        expansion: korttisetti / laajennus
        release_date: julkaisupäivä
        id: kortin id-numero tietokannassa
    """

    def __init__(self, pokemon, pokedex_number, expansion, release_date, id=None):
        """Luokan konstruktori, joka luo uuden kortin.

        Args:
            pokemon:
                Merkkijonoarvo, joka sisältää pokemonin nimen.
            pokedex_number:
                Lukuarvo, joka sisältää pokemonin dex-numeron.
            expansion:
                Merkkijonoarvo, joka sisältää korttisetin / laajennuksen.
            release_date:
                Päivämääräarvo, joka sisältää julkaisupäivämäärän.
            id:
                Lukuarvo, joka sisältää id-numeron tietokannassa
                Arvo on oletukseltaan None, koska arvo otetaan suoraan tietokannasta.
        """


        self.id = id
        self.pokemon = pokemon
        self.pokedex_number = pokedex_number
        self.expansion = expansion
        self.release_date = release_date

    def __repr__(self):
        """Palauttaa olion merkkijonomuodossa.
        """


        return (f"Card(id={self.id}, pokemon={self.pokemon}, "
                f"pokedex_number={self.pokedex_number}, expansion={self.expansion}, "
                f"release_date={self.release_date})")

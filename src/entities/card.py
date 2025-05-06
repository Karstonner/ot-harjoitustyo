class Card:
    def __init__(self, pokemon, pokedex_number, expansion, release_date, id=None):
        self.id = id
        self.pokemon = pokemon
        self.pokedex_number = pokedex_number
        self.expansion = expansion
        self.release_date = release_date
    
    def __repr__(self):
        return (f"Card(id={self.id}, pokemon={self.pokemon}, "
                f"pokedex_number={self.pokedex_number}, expansion={self.expansion}, "
                f"release_date={self.release_date}")
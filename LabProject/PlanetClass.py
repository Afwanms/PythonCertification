class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        for param in [name, planet_type, star]:
            if not isinstance(param, str):
                raise TypeError('name, planet type, and star must be strings')
        for param in [name, planet_type, star]:
            if param == '':
                raise ValueError ('name, planet_type, and star must be non-empty strings')
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('Earth', 'Inferior', 'Sun')
print(planet_1)
print(planet_1.orbit())
planet_2 = Planet('Neptune', 'Superior', 'Sun')
print(planet_2)
print(planet_2.orbit())
planet_3 = Planet('Mars', 'Inferior', 'Sun')
print(planet_3)
print(planet_3.orbit())
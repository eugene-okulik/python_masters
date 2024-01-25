class Flowers:

    def __init__(self, name: str, freshness: bool, color: str, stem_length: float, cost_rub: float, lifetime: int):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.cost = cost_rub
        self.lifetime = lifetime


class DomesticFlower(Flowers):
    def __init__(self, name: str, freshness: bool, color: str, stem_length: float, cost_rub: float, lifetime: int):
        super().__init__(name, freshness, color, stem_length, cost_rub, lifetime)
        self.exotic = False
        self.wild = False


class WildFlower(Flowers):
    def __init__(self, name: str, freshness: bool, color: str, stem_length: float, cost_rub: float, lifetime: int):
        super().__init__(name, freshness, color, stem_length, cost_rub, lifetime)
        self.wild = True
        self.exotic = False


class Bouquet:

    def __init__(self):
        self.bouquet = []

    def add_flower_to_bouquet(self, flower):
        self.bouquet.append(flower)

    def calculate_cost(self):
        total_cost = 0
        for flower in self.bouquet:
            total_cost += flower.cost
            return total_cost

    def calculate_wilting_time(self):
        total_lifetime = 0
        for flower in self.bouquet:
            total_lifetime += flower.lifetime
        return total_lifetime / len(self.bouquet)

    def sort_by_color(self):
        self.bouquet.sort(key=lambda x: x.color)


peony1 = DomesticFlower('Peony', False, 'pink', 0.5, 45, 2)
peony2 = DomesticFlower('Peony', True, 'sand', 0.5, 45, 7)
rose1 = DomesticFlower('Rose', False, 'white', 0.6, 100, 3)
rose2 = DomesticFlower('Rose', True, 'salmon', 0.6, 90, 5)
iberis = WildFlower('Iberis', True, 'navy blue', 0.4, 150, 10)
lupins = WildFlower('Lupins', True, 'lilac', 0.3, 200, 10)

new_bouquet = Bouquet()
new_bouquet.add_flower_to_bouquet(peony1)
new_bouquet.add_flower_to_bouquet(peony2)
new_bouquet.add_flower_to_bouquet(rose1)
new_bouquet.add_flower_to_bouquet(rose2)
new_bouquet.add_flower_to_bouquet(iberis)
new_bouquet.add_flower_to_bouquet(lupins)

print(new_bouquet.calculate_cost())
print(new_bouquet.sort_by_color())




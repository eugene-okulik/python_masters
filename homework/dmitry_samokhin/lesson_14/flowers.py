class Flower:
    def __init__(self, name, freshness, stem_length, price, lifespan):
        self.name = name
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, freshness, stem_length, price, lifespan):
        super().__init__("Rose", freshness, stem_length, price, lifespan)


class Lily(Flower):
    def __init__(self, freshness, stem_length, price, lifespan):
        super().__init__("Lily", freshness, stem_length, price, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_wilting_time(self):
        total_lifespan = sum([flower.lifespan for flower in self.flowers])
        return total_lifespan / len(self.flowers)

    def sort_by_parameter(self, parameter):
        return sorted(self.flowers, key=lambda x: getattr(x, parameter))

    def search_by_parameter(self, parameter, value):
        return [
            flower for flower in self.flowers if getattr(flower, parameter) == value
        ]


# Создаем цветы
rose1 = Rose(5, 30, 100, 7)
rose2 = Rose(4, 28, 90, 6)
lily1 = Lily(7, 25, 80, 5)
lily2 = Lily(6, 27, 85, 6)

# Создаем букет
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)
bouquet.add_flower(lily2)

# Печатаем время увядания букета
print("Среднее время увядания букета:", bouquet.calculate_wilting_time())

# Сортируем цветы по свежести
sorted_by_freshness = bouquet.sort_by_parameter("freshness")
print(
    "Цветы в букете, отсортированные по свежести:",
    [flower.name for flower in sorted_by_freshness],
)

# Ищем лилии в букете
lilies = bouquet.search_by_parameter("name", "Lily")
print("Найденные лилии в букете:", [flower.freshness for flower in lilies])

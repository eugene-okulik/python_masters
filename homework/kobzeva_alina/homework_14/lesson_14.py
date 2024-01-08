class Flower:
    def __init__(self, color, freshness, stem_length, cost):
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.cost = cost


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__(color, freshness, stem_length, cost)


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__(color, freshness, stem_length, cost)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        total_cost = 0
        for flower in self.flowers:
            total_cost += flower.cost
        return total_cost

    def calculate_average_lifespan(self):
        total_lifespan = 0
        for flower in self.flowers:
            total_lifespan += flower.freshness
        average_lifespan = total_lifespan / len(self.flowers)
        return average_lifespan

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length, reverse=True)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.cost, reverse=True)

    def search_by_lifespan(self, lifespan):
        result = []
        for flower in self.flowers:
            if flower.freshness == lifespan:
                result.append(flower)
        return result

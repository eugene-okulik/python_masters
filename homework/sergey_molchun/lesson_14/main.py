# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Flowers:
    def __init__(self, name: str, color: str, bud_size: str, petals_number: int, price_usd: float, life_time: int,
                 stem_length: int):
        self.__name = name
        self.__color = color
        self.bud_size = bud_size
        self.petals_number = petals_number
        self.__price_usd = price_usd
        self.__life_time = life_time
        self.stem_length = stem_length

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def price_usd(self):
        return self.__price_usd

    @property
    def life_time(self):
        return self.__life_time


class WildFlowers(Flowers):
    def __init__(self, name, color, bud_size, petals_number, price_usd, life_time, stem_length):
        super().__init__(name, color, bud_size, petals_number, price_usd, life_time, stem_length)
        self.wild = True
        self.exotic = False


class DomesticatedFlowers(Flowers):
    def __init__(self, name, color, bud_size, petals_number, price_usd, life_time, stem_length):
        super().__init__(name, color, bud_size, petals_number, price_usd, life_time, stem_length)
        self.wild = False
        self.exotic = False


class Bouquet:
    def __init__(self, *args):
        # self.flowers = {}
        self.flowers = []
        # for arg in args:
        #     print(vars(arg))
        #     self.flowers.update({str(vars(arg)['_Flowers__name']): vars(arg)})
        for i in range(len(args)):
            # print(vars(args[i]))
            # self.flowers.update({i: vars(args[i])})
            self.flowers.append(vars(args[i]))
        # print(self.flowers)
        self.price = self.calculate_price()
        self.avg_wilting = self.wilting_time()

    def calculate_price(self):
        price = 0
        # for flower in self.flowers:
        #     print(vars(flower))
        #     price += (vars(flower)["_Flowers__price_usd"])
        for i in range(len(self.flowers)):
            print(self.flowers[i])
            price += (self.flowers[i]["_Flowers__price_usd"])
        return f"Bouqet price: {price} $."

    def wilting_time(self):
        days = 0
        counter = 0
        # for flower in self.flowers:
        #     days += (vars(flower)["_Flowers__life_time"])
        #     counter += 1
        for i in range(len(self.flowers)):
            days += (self.flowers[i]["_Flowers__life_time"])
            counter += 1
        avg_wilting_time = days / counter
        return f"Bouquet average life: {avg_wilting_time} days."

    # (свежесть)
    def __sort_fresh(self, flower):
        return flower['_Flowers__life_time']

    @property
    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: self.__sort_fresh(flower), reverse=True)
        return self.flowers

    # (цвет)
    def __sort_color(self, flower):
        return flower['_Flowers__color']

    @property
    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: self.__sort_color(flower))
        return self.flowers

    # (длина стебля)
    def __sort_steam(self, flower):
        return flower['stem_length']

    @property
    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: self.__sort_steam(flower), reverse=True)
        return self.flowers

    # (стоимость)
    def __sort_price(self, flower):
        return flower['_Flowers__price_usd']

    @property
    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: self.__sort_price(flower))
        return self.flowers

    # Реализовать поиск цветов в букете по каким-нибудь параметрам
    # (например, по среднему времени жизни) (и это тоже метод).
    def __find_with_lifetime(self, flower):
        return flower['_Flowers__price_usd']

    def find_lifetime(self, lifetime: int):
        flowers_result = list(filter(lambda flower: flower['_Flowers__life_time'] >= lifetime, self.flowers))
        return flowers_result


ghost_orchid = WildFlowers("Ghost Orchid", "Beige", "Big", 5, 55,
                           15, 3)
ghost_orchid.exotic = True

carson_rose = DomesticatedFlowers("Scarlet Carson Rose", "Scarlet", "Big",
                                  35, 10, 7, 110)

pink_tulip = DomesticatedFlowers("Pink Tulip", "Pink", "Middle", 12, 2,
                                 5, 40)

french_lavender = DomesticatedFlowers("Lavender", "Violet", "Big", 5, 7,
                                      30, 55)

my_buquet = Bouquet(ghost_orchid, carson_rose, pink_tulip, french_lavender)

print(my_buquet.price)
print(my_buquet.avg_wilting)

print(my_buquet.sort_by_freshness)
print(my_buquet.sort_by_color)
print(my_buquet.sort_by_stem_length)
print(my_buquet.sort_by_price)
print(my_buquet.find_lifetime(10))

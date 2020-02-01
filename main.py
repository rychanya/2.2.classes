class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f'Feed {self.name}')

    def say(self):
        return 'I`m an animal.'

    def care(self):
        self.feed()


class Bird(Animal):

    def collect_egs(self):
        print(f'Eggs collected from {self.name}')

    def care(self):
        super().care()
        self.collect_egs()


class Animal_provide_milk(Animal):

    def milk(self):
        print(f'Milk {self.name}')

    def care(self):
        super().care()
        self.milk()


class Sheep(Animal):

    def shear(self):
        print(f'Shear {self.name}')

    def say(self):
        return 'Baa'

    def care(self):
        super().care()
        self.shear()


class Goat(Animal_provide_milk):

    def say(self):
        return 'Naa'


class Cow(Animal_provide_milk):

    def say(self):
        return 'Moo'


class Duck(Bird):

    def say(self):
        return 'Honks'


class Chicken(Bird):

    def say(self):
        return 'Cluck'


class Goose(Bird):

    def say(self):
        return 'Hhonk-honk'

if __name__ == '__main__':
    uncle_joe_farm = [
        Goose('Серый', 3.3),
        Goose('Белый', 2.7),
        Chicken('Ко-Ко', 0.6),
        Chicken('Кукареку', 0.8),
        Duck('Кряква', 1),
        Cow('Манька', 1080),
        Goat('Рога', 100),
        Goat('Копыта', 120),
        Sheep('Барашек', 140),
        Sheep('Кудрявый', 160)
    ]

    animals_weight = sum([animal.weight for animal in uncle_joe_farm])
    print(f'Общий вес всех животных: {animals_weight}')

    name, weight = max(
        [(animal.name, animal.weight) for animal in uncle_joe_farm],
        key=lambda name_and_weight: name_and_weight[1]
        )
    print(f'Больше всего весит {name}. Вес {weight}.')

    print('Нужно со всеми поздороваться и сделать все необходимое.')
    for animal in uncle_joe_farm:
        print()
        print(f'me: Hi, {animal.name}.\n{animal.name}: {animal.say()}')
        animal.care()


    
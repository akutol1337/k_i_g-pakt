#Po dwa zadania z polimorfizmu (duck typing oraz interfejs), hermetyzacji i obsługi wyjątków. Polecenia i implementacja w Pythonie.
#polimorfizm - duck typing
'''
class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('kot robi miau miau')

    def run(self):
        print('kot biega')

    def fly(self):
        print('kot nie lata')

class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('pies robi hau hau')

    def run(self):
        print('pies biega')

    def fly(self):
        print('pies nie lata')

class Bird:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('Ptak robi ćwir ćwir')

    def run(self):
        print('ptak biega')

    def fly(self):
        print('ptak lata')

cat = Cat('kot')
dog = Dog('pies')
bird = Bird('ptak')

cat.make_sound()
dog.make_sound()
bird.make_sound()

cat.run()
dog.run()
bird.run()

cat.fly()
dog.fly()
bird.fly()

#interfejsy
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('zwierzę robi dzwięk')

    def run(self):
        print('zwierzę biega')

    def fly(self):
        print('zwierzę lata')

    def swim(self):
        print('zwierzę pływa')

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print('ryba robi bul bul')

    def run(self):
        print('ryba nie biega')

    def fly(self):
        print('ryba nie lata')

    def swim(self):
        print('ryba pływa')

class Lizard(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print('jaszczurka robi ssssss')

    def run(self):
        print('jaszczurka biega')

    def fly(self):
        print('jaszczurka nie lata')

    def swim(self):
        print('jaszczurka pływa')

fish = Fish('ryba')
lizard = Lizard('jaszczurka')

fish.make_sound()
lizard.make_sound()

fish.run()
lizard.run()

fish.fly()
lizard.fly()

fish.swim()
lizard.swim()
'''
#hermetyzacja - sklep
'''
class Shop:
    def __init__(self, name, product, product_weight, money):
        self.name = name
        self.product = [product]
        self.product_weight = [product_weight]
        self.__money = money

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        self.__money = value

    def buy_product(self, product, product_weight, price, quantity):
        for each in range(quantity):
            if (self.money >= price):
                print(self.name, 'kupuje', product, 'za', price, 'zł.')
                self.product += [product]
                self.product_weight += [product_weight]
                self.money -= price
        print("")

    def sell_product(self, product, price, quantity):
        for each in range(quantity):
            i = 0
            for each in self.product:
                if each == product:
                    print(self.name, 'sprzedaje', product, 'za', price, 'zł.')
                    self.product.pop(i)
                    self.product_weight.pop(i)
                    self. money += price
                i += 1
        print("")

    def show_products(self):
        print('Oto produkty sklepu:')
        i = 0
        for each in self.product:
            if (i<=len(self.product)-2):
                print(each, str(self.product_weight[i])+'kg,')
            else:
                print(each, str(self.product_weight[i])+'kg')
            i += 1

    def show_money(self):
        print(self.name, 'ma:', round(self.money,2), 'zł.')

    def show_info(self):
        self.show_products()
        self.show_money()
        print("")

biedronka = Shop('biedronka', 'pomidor', 0.2, 1000)
biedronka.show_info()
biedronka.buy_product('pomidor', 0.2, 0.3, 3)
biedronka.buy_product('ogórek', 0.2, 0.3, 2)
biedronka.show_info()
biedronka.sell_product('pomidor', 1.6, 2)
biedronka.show_info()
lidl = Shop('lidl', 'pomidor', 0.2, 1000)
lidl.show_info()
lidl.buy_product('pomidor', 0.2, 0.3, 3)
lidl.buy_product('ogórek', 0.2, 0.3, 2)
lidl.show_info()
lidl.sell_product('pomidor', 1.2, 2)
lidl.show_info()
'''
#hermetyzacja - akwarium
fish_pl = []
ultraprefix_prefix_prefix = ["dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt"]
ultraprefix_prefix = ["dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć", "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
ultraprefix_suffix = ["tysiące", "tysięcy"]
ultraprefix = ["tysiąc"]
superprefix = ["sto", "dwieście", "trzysta", "czterysta", "pięcset", "sześćset", "siedemset", "osiemset", "dziewięćset"]
prefix = ["dwudziesta","trzydziesta","czterdziesta","pięćdziesiąta","sześćdziesiąta", "siedemdziesąta","osiemdziesiąta","dziewięćdziesiąta"]
suffix = ["pierwsza", "druga", "trzecia", "czwarta", "piąta", "szósta", "siódma", "ósma", "dziewiąta"]
mid = ["dziesiąta", "jedenasta", "dwunasta", "trzynasta", "czternasta", "piętnasta", "szesnasta", "siedemnasta", "osiemnasta", "dziewiętnasta"]
for each in suffix:
     fish_pl += [each]
for each in mid:
     fish_pl += [each]
for each in prefix:
    fish_pl += [each]
    for inner_each in suffix:
        supercombo = (each + " " + str(inner_each))
        fish_pl += [supercombo]
for each in superprefix:
    fish_pl += [each]
    for inner_each in suffix:
        supercombo = (each + " " + str(inner_each))
        fish_pl += [supercombo]
    for inner_each in mid:
        supercombo = (each + " " + str(inner_each))
        fish_pl += [supercombo]
    for inner_each in prefix:
        supercombo = (each + " " + str(inner_each))
        fish_pl += [supercombo]
        for inner_inner_each in suffix:
            supercombo = (each + " " + str(inner_each) + " " + str(inner_inner_each))
            fish_pl += [supercombo]
for each in ultraprefix_suffix:
    if (ultraprefix_suffix[0] == each):
        for inner_each in ultraprefix_prefix[:3]:
            supercombo = (inner_each + " " + each)
            ultraprefix += [supercombo]
    if (ultraprefix_suffix[1] == each):
        for inner_each in ultraprefix_prefix[3:]:
            supercombo = (inner_each + " " + each)
            ultraprefix += [supercombo]
        for inner_each in 
    
class Aquarium:
    def __init__(self, size, fish_name, fish_species):
        self.size = size
        self.fish_name = [fish_name]
        self.fish_species = [fish_species]

    def show_fish(self):
        print('\nOto ryby w akwarium:')
        i = 0
        for each in self.fish_name:
            #print("\nTa ryba nazywa się:", each, "\nGatunek tej ryby to:", str(self.fish_species[i]))
            print("\n"+fish_pl[i].capitalize(),"ryba nazywa się:", each, "\nGatunek tej ryby to:", str(self.fish_species[i]))
            i += 1

    def add_fish(self, fish_name, fish_species):
        self.fish_name += [fish_name]
        self.fish_species += [fish_species]


aquarium = Aquarium(7 ,'Darek', 'sum')
aquarium.show_fish()
aquarium.add_fish('Marek', 'szczupak')
aquarium.show_fish()
#print(fish_pl)
print(ultraprefix)
#obsługa wyjątków - liczby
'''
print("Ile przeczytałeś książek w ostatnim roku?")
while True:
    try:
        amount = int(input())
        break
    except ValueError:
        print("To nie jest liczba")
'''
#obsługa wyjątków - dzielenie przez zero
'''
print("Symulator dzielenia")
while True:
    try:
        print("Podaj pierwszą liczbę")
        num_one = float(input())
        print("Podaj drugą liczbę")
        num_two = float(input())
        result = num_one/num_two
        print("Wynik wynosi: " + str(result))
        break
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
'''
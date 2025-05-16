class Auto:

    def __init__(self, name="A8", age=2010, manufacturer="AUDI", power=200, color="white", price=200000):
        self.__name = name
        self.__age = age
        self.__manufacturer = manufacturer
        self.__power = power
        self.__color = color
        self.__price = price

    def info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.__name}\nГод выпуска: {self.__age}\nПроизводитель: {self.__manufacturer}\n"
              f"Мощность двигателя: {self.__power} л.с.\nЦвет машины: {self.__color}\nЦена: {self.__price}")
        print("=" * 40)

    def sname(self, sname):
        self.__name = sname

    def gname(self):
        return self.__name

    def sage(self, sage):
        if isinstance(sage, int):
            self.__age = sage
        else:
            print("Год выпуска должен быть целым числом")

    def gage(self):
        return self.__age

    def smanufacturer(self, smanufacturer):
        self.__manufacturer = smanufacturer

    def gmanufacturer(self):
        return self.__manufacturer

    def spower(self, spower):
        if isinstance(spower, int):
            self.__power = spower
        else:
            print("мощность двигателя должен быть целым числом")

    def gpower(self):
        return self.__power

    def scolor(self, scolor):
        if isinstance(scolor, str):
            self.__color = scolor
        else:
            print("Цвет машины должен быть строкой")

    def gcolor(self):
        return self.__color

    def sprice(self, sprice):
        if isinstance(sprice, (int, float)):
            self.__price = sprice
        else:
            print("Цена должна быть числом")

    def gprice(self):
        return self.__price


car = Auto()
car.info()
car.sname("X7 M50i")
car.sage(2021)
car.smanufacturer("BMW")
car.spower(530)
car.scolor("white")
car.sprice(10790000)
car.info()
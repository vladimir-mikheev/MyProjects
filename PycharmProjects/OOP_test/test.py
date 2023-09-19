class Phone:
    def __init__(self, screen, price, cpu, ram, memory):
        self.screen = screen
        self.price = price
        self.cpu = cpu
        self.ram = ram
        self.memory = memory

    def screen(self):
        print("Разрешение экрана: %sp" % self.screen)

    def price(self):
        print("Цена %s рублей" % self.price)

    def cpu(self):
        print("Процессор: %s" % self.cpu)

    def ram(self):
        print("Оперативная память: %sGb" % self.ram)

    def memory(self):
        print("Количество встроенной память: %s Gb" % self.memory)

    def general(self):
        print("Общие характиристики:")
        print("")
        print("Разрешение экрана: %sp" % self.screen)
        print("Процессор: %s" % self.cpu)
        print("Оперативная память: %sGb" % self.ram)
        print("Количество встроенной память: %s Gb" % self.memory)
        print("Цена %s рублей" % self.price)
    pass


class Android(Phone):
    @staticmethod
    def model():
        print("Samsung Galaxy")
    pass


class Apple(Phone):
    @staticmethod
    def model():
        print("Apple iPhone")
    pass


iphone_13 = Apple(1080, 60000, "M1", 8, 256)
iphone_13.model()
iphone_13.general()
print("")

Samsung_Galaxy = Android(720, 10000, "MediaTek", 4, 32)
Samsung_Galaxy.model()
Samsung_Galaxy.general()

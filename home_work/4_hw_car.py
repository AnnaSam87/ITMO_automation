class Car:
    def __init__(self, color, type, year):
        self.color=color
        self.type=type
        self.year=year

    def launch_car(self):
        print('Автомобиль {self.} заведен')

    def shutdown_car(self):
        print('Автомобиль заглушен')

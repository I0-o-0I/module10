from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100 - self.power
        day = 1
        while enemy > 0:
            print(f'{self.name} сражается {day}(дня)..., осталось {enemy} воинов')
            enemy = enemy - self.power
            day += 1
            sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней (дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
for i in (first_knight, second_knight):
    i.start()
for i in (first_knight, second_knight):
    i.join()
print('Все битвы закончились!')
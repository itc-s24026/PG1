class Car:
    weight = 4000
    num_wheels = 4

    def __init__(self, car_name='NoName'):
        self.name = car_name

    def calc_weight_per_wheel(self):
        return self.weight / self.num_wheels

default_car = Car()

print(default_car.name)

my_car = Car('DeLorean')
print(my_car.name)


class Cat:
    cry = "miao"
    legs = "4"
    is_animal = True

tama = Cat()
print("叫声:{},脚的数量:{},动物:{}".format(tama.cry, tama.legs, tama.is_animal))













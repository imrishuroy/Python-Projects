def add(*args):
    s = 0
    for n in args:
        s += n
    return s


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.model = kwargs.get("model")


my_car = Car(name="Tesla", model="BT-101")
print(my_car.model)

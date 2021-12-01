class MyDog:

    def __init__(self, name, age, color, isAsleep=False):
        self.name = name
        self.age = age
        self.color = color

    def walk(self):
        return print("{} is walking".format(self.name))

    def eat(self):
        return print("{} is eating food".format(self.name))

    def sleep(self):
        self.isAsleep = True
        return print("{} is sleeping".format(self.name))

    def wake_up(self):
        self.isAsleep = False
        return print("{} is waking up".format(self.name))

    def info(self):
        return print(self.name,
                     self.age,
                     self.color)


walk_and_sleep = MyDog("billy", 12, False)
walk_and_sleep.walk()
walk_and_sleep.sleep()
walk_and_sleep.wake_up()
walk_and_sleep.eat()

eat_and_sleep = MyDog("billy", 12, False)
eat_and_sleep.eat()
eat_and_sleep.sleep()

print(dir(MyDog))

class Animal:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def speak(self):
        raise NotImplementedError("Метод 'speak' повинен бути реалізований у підкласі")

    def move(self):
        print(f"{self.name} рухається.")

    def sleep(self):
        print(f"{self.name} спить.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  
        self.breed = breed  

    def speak(self):
        print(f"{self.name} каже: Гав-гав!")

    def fetch(self):
        print(f"{self.name} приносить м'ячик.")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  
        self.color = color  

    def speak(self):
        print(f"{self.name} каже: Мяу!")

    def purr(self):
        print(f"{self.name} муркоче.")

dog = Dog(name="Рекс", age=5, breed="Німецька вівчарка")
cat = Cat(name="Мурчик", age=3, color="Чорний")

dog.speak()
dog.move()
dog.fetch()
dog.sleep()

print("\n")

cat.speak()
cat.move()
cat.purr()
cat.sleep()

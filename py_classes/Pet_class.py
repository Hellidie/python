class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_info(self):
        print(f"Hello, i {self.name}, me {self.age} years old and I am {self.color}")


class Cat(Pet):
    def __init__(self, name, age, color, size):
        super().__init__(name, age, color)
        self.size = size

    def get_cat_info(self):
        print(f"Hello, i {self.name}, me {self.age} years old, i am {self.color} and i am {self.size} cat!")

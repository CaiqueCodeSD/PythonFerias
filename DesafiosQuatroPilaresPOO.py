class Shape():
    def __init__(self, color = "undefined"):
        self.color = color

    def what_am_i(self):
        return f"I am a shape and my color is {self.color}"

class Rectangle(Shape):
    def __init__(self, height, width, color="undefined"):
        super().__init__(color)
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Shape):
    def __init__(self, side, color="undefined"):
        super().__init__(color)
        self.side = side

    def change_size(self, valor):
        self.side += valor

    def calculate_perimeter(self):
        return self.side * 4
    
    def __str__(self):
        return f"Square(side={self.side})"
    


rectangle = Rectangle(10,10, "blue")
print(rectangle.calculate_perimeter())

square = Square(15, "green")
print(square.calculate_perimeter())

square.change_size(-4)
print(square.calculate_perimeter())

print(rectangle.what_am_i())
print(square.what_am_i())

'''
Desafio 04
'''

class Horse():
    def __init__(self, race, weight, color, mood, knight):
        self.race = race
        self.weight = weight
        self.color = color
        self.mood = mood
        self.knight = knight

class Rider():
    def __init__(self, name):
        self.name = name

cavaleiro = Rider("Arthur Morgan")
cavalo = Horse("Arabian","Perfect","Orange","Calm", cavaleiro)

print(cavalo.knight.name)


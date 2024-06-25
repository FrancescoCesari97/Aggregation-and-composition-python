
# * Aggregation = represents a relationship where one object (The whole)
#  *              contains references to one or more INDEPENDENT object (the parts)



# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
    
#     def add_book(self, book):
#         self.books.append(book)
    
#     def list_books(self):
#         return [f"{book.title} by {book.author}"for book in self.books]

# class Book:
#     def __init__(self, title, author):
#         self.title = title 
#         self.author = author

# library = Library(" Biblioteca comunale")


# book1 = Book("Rashmon", "Akutagawa")
# book2 = Book("the hobbit", "J. R. R. Tolkien")


# library.add_book(book1)

# library.add_book(book2)

# print(library.name)
# # print(library.list_books())

# for book in library.list_books():
#     print(book)


# * Composition = The composed object directly owns it's components, which cannot exists independently "owns-a" relationship


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):

        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    
    def display_car(self):
        return f"brand {self.make} model {self.model} horse power {self.engine.horse_power} wheels size {self.wheels[0].size}"

car = Car("Fiat", "Panda", 100, 18 )

print(car.display_car())



# YAGNI (You aren't gonna need it)

class Report:
    def __init__(self, title):
        self.title = title
        self.subtitle = None  # Not required yet

    def add_subtitle(self, subtitle):
        self.subtitle = subtitle




#########################################




# DRY (Don't repeat yourself)

def pi():
    return 3.14

def calculate_circle_area(radius):
    return pi() * radius * radius

def calculate_sphere_volume(radius):
    return 4 / 3 * pi() * radius ** 3




# SOLID 

# S – Single Responsibility Principle (SRP)
# Class to represent a Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Class to represent a database that saves books
class BookDatabase:
    def save(self, book: Book):
        print(f"Saving '{book.title}' by {book.author} to database")

# Driver code to test the classes

# Creating a Book object
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Creating a BookDatabase object
db = BookDatabase()

# Saving the book to the database
db.save(book1)










# O – Open/Closed Principle (OCP)

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class PercentageDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9

class FixedDiscount(Discount):
    def apply_discount(self, price):
        return price - 10
    

# Creating instances of the discount classes
percentage_discount = PercentageDiscount()
fixed_discount = FixedDiscount()

# Testing the discounts
price = 100

# Applying percentage discount (10% off)
discounted_price_percentage = percentage_discount.apply_discount(price)
print(f"Price after percentage discount: {discounted_price_percentage}")

# Applying fixed discount (subtracting 10)
discounted_price_fixed = fixed_discount.apply_discount(price)
print(f"Price after fixed discount: {discounted_price_fixed}")









# L (Liskov substitution princple)

# Base class Bird
class Bird:
    def make_sound(self):
        print("Chirp")

# Derived class FlyingBird that adds a fly method
class FlyingBird(Bird):
    def fly(self):
        print("Flying")

# Derived class Penguin that overrides the make_sound method
class Penguin(Bird):
    def make_sound(self):
        print("Honk")

# Driver code to test the functionality

# Creating an instance of FlyingBird
sparrow = FlyingBird()
sparrow.make_sound()  # Output: Chirp (inherited from Bird)
sparrow.fly()         # Output: Flying (defined in FlyingBird)

# Creating an instance of Penguin
penguin = Penguin()
penguin.make_sound()  # Output: Honk (overridden in Penguin)






# I – Interface Segregation Principle (ISP)

class Printer:
    def print_document(self):
        pass

class Scanner:
    def scan_document(self):
        pass

# Concrete class for a basic printer that implements print functionality
class BasicPrinter(Printer):
    def print_document(self):
        print("Printing document")

# Concrete class for a multi-function printer that can print and scan
class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

# Driver code to test the functionality
basic_printer = BasicPrinter()
basic_printer.print_document()  # Output: Printing document

multi_function_printer = MultiFunctionPrinter()
multi_function_printer.print_document()  # Output: Printing document
multi_function_printer.scan_document()   # Output: Scanning document









# D – Dependency Inversion Principle (DIP) 

from abc import ABC, abstractmethod

# Abstract class for Keyboard
class Keyboard(ABC):
    @abstractmethod
    def connect(self):
        pass

# Concrete class for Wired Keyboard
class WiredKeyboard(Keyboard):
    def connect(self):
        print("Wired keyboard connected")

# Concrete class for Wireless Keyboard
class WirelessKeyboard(Keyboard):
    def connect(self):
        print("Wireless keyboard connected")

# Computer class which accepts any type of Keyboard (Wired or Wireless)
class Computer:
    def __init__(self, keyboard: Keyboard):
        self.keyboard = keyboard

    def connect_keyboard(self):
        self.keyboard.connect()

# Driver code to test
wired_keyboard = WiredKeyboard()  # Create instance of WiredKeyboard
computer1 = Computer(wired_keyboard)  # Pass the wired keyboard to computer
computer1.connect_keyboard()  # Output: Wired keyboard connected

wireless_keyboard = WirelessKeyboard()  # Create instance of WirelessKeyboard
computer2 = Computer(wireless_keyboard)  # Pass the wireless keyboard to computer
computer2.connect_keyboard()  # Output: Wireless keyboard connected


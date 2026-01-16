import math

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(self.name, self.salary)


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(self.title, self.author, self.price)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)


class Flight:
    def __init__(self, flight_number, seats):
        self.flight_number = flight_number
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked")
        else:
            print("No seats available")


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product)

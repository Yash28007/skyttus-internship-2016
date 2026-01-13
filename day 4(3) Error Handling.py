import re
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

class InvalidAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero error.")
except ValueError:
    print("Invalid integer input.")
except Exception as e:
    print("Error:", e)

try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found error.")
finally:
    try:
        file.close()
    except:
        pass

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Division by zero error.")

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Invalid age")
    print("Valid age")
except InvalidAgeError as e:
    print(e)

numbers = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print("Index error.")
except ValueError:
    print("Invalid index input.")

try:
    p = int(input("Enter first number: "))
    q = int(input("Enter second number: "))
    print(p / q)
except Exception as e:
    logging.error("Error occurred", exc_info=True)

try:
    email = input("Enter email: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format")
    print("Valid email")
except InvalidEmailError as e:
    print(e)

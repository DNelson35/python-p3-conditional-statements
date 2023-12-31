#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    # using lambda functions
    # ops = {
    #     "+": lambda x, y: x + y,
    #     "-": lambda x, y: x - y,
    #     "*": lambda x, y: x * y,
    #     "/": lambda x, y: x / y,
    # }

    # if operation in ops:
    #     return ops[operation](num1, num2)
    # else:
    #     return "Invalid operation"

    # using eval
    ops = ["+", "*", "-", "/"]

    if operation in ops:
        return eval(str(num1) + operation + str(num2))
    else:
       print("Invalid operation!")
       return None


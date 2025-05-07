'''
Simple calculater that takes two number as input and take one mathmatical operater and perform the calculation and display output:
'''

import time
import random
import os

from Animation.ClearScreen import screenCleaner


def main():
    value()
    recheck()

def timer():
    a = 0
    random_number = random.randint(2, 4)
    while not a == random_number:
        print("processing.....")
        time.sleep(0.8)
        a += 1

def recheck():
    a = True
    while a:
        recheck = input("\nDo you want to calculate another number: ")
        if recheck.lower() == "yes":
            timer()
            value()
        elif recheck.lower() == "no":
            timer()
            print("Have a Good Day\n")
            time.sleep(0.8)
            print("Clearing....")
            time.sleep(0.8)
            print("Clearing....")
            time.sleep(0.8)
            print("Clearing....")
            screenCleaner()
            a = False
        else:
            timer()
            print("Invalid input")

def value():
    a = True
    while a:
        operator = input("\nEnter the operator you want to do (+, -, *, /): ")
        if operator == "+" or operator.lower() == "addition" or operator.lower() == "add":
            print(add_operation())
            a = False
        elif operator == "-" or operator.lower() == "subtraction" or operator.lower() == "subtract":
            print(subtract_operation())
            a = False
        elif operator == "*" or operator.lower() == "multiplification" or operator.lower() == "multiply":
            print(multiply_operation())
            a = False
        elif operator == "/" or operator.lower() == "divide":
            print(divide_operation())
            a = False
        else:
            print("Invalid input. Try again: \n")


def asking_validity_input():
    timer()
    num1 = input("\nEnter the first number: ")
    num2 = input("Enter the second numner: ")
    a = True
    while a:
        if num1 == "" or not num1.isdigit():
            timer()
            print("Invalid first value")
            num1 = input("\nEnter the first number: ")
        elif num2 == "" or not num2.isdigit():
            timer()
            print("Invalid second value")
            num2 = input("\nEnter the second number: ")
        else:
            a = False
    return float(num1), float(num2)


def add_operation():
    num1, num2 =asking_validity_input()
    timer()
    return num1 + num2

def subtract_operation():
    num1, num2 =asking_validity_input()
    timer()
    return num1 - num2

def multiply_operation():
    num1, num2 =asking_validity_input()
    timer()
    return num1 * num2

def divide_operation():
    num1, num2 = asking_validity_input()
    while num2 == 0:
        num2 = float(input("\nNumber cannot be divide by zero. Please input anothe number: "))
    timer()
    return num1 / num2


if __name__ == "__main__":
    main()

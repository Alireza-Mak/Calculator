import os
from calculator_art import logo, creator
operations = ["+","-","*","/"]

def is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False


def is_item_in_array (operation,array):
  if operation in array:
    return True
  else:
    return False

def sum(num1, num2):
  return float(num1) + float(num2)

def subtract(num1, num2):
  return float(num1) - float(num2)

def multiply(num1, num2):
  return float(num1) * float(num2)

def divide(num1, num2):
  return float(num1) / float(num2)


def calculate():
  print (logo)
  end_of_calc = False
  answer = 0
  num1 = input("What's the first number? ")

  while not (num1.isnumeric() or is_float(num1)):
    num1 = input("Wrong input, please enter the first number: ")

  while not end_of_calc:
    for operator in operations:
      print(operator)
    operation = input("pick an operation: ")


    while not is_item_in_array(operation, operations):
      operation = input("wrong operation, please pick a coorectoperation: ")

    num2 = input("What's the next number? ")

    while not (num2.isnumeric() or is_float(num2)):
        num2 = input("Wrong input, please enter the next number: ")

    if operation == "+":
      answer = sum(num1, num2)
    elif operation == "-":
      answer = subtract(num1, num2)
    elif operation == "*":
      answer = multiply(num1, num2)
    else:
      answer = divide(num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")
    continue_game = input(f"'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

    while not (continue_game == "y" or continue_game == "n"):
      continue_game = input(f"Wrong input, please enter'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

    if continue_game =="n":
      end_of_calc = True
      os.system("clear")
      os.system("CLS")
      print(logo)
      print(f"\nCreated by:\n{creator}")
    else:
      os.system("clear")
      os.system("CLS")
      print(logo)
      print(f"Your prvious answer is: {answer}")
      num1 = answer

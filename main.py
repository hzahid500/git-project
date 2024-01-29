#!/bin/bash
num1 = float(input("ENTER YOUR FIRST NUMBER: "))
op = input("ENTER OPERATOR: ")
num2 = float(input("ENTER YOUR SECOND NUMBER: "))

if op == "+":
  print("The sum is: " + str(num1 + num2))
elif op == "-":
  print("The substraction is: " + str(num1 - num2))
elif op == "*":
  print("The multiplication is: " + str(num1 * num2))
elif op == "/":
  print("The division is: " + str(num1 / num2))
else:
  print("INVALID OPERATOR")

"""
Write a program bmi.py that calculates the user's BMI (body mass index). 

The formula is:
BMI = weight in kilograms / (height in meters * height in meters)
The program takes in a weight and a height from stdin and produces an output.
For example
What is your weight in kg? 70
What is your height in m? 1.82
Your BMI is 21.1
"""

print("What is your weight in kg?", end = " ")
weight = float(input())
print("What is your height in m?", end = " ")
height = float(input())
BMI = weight / (height ** 2)
print(f"Your BMI is {BMI:.1f}")
import random


answer = False

while (answer == False):
    first_number = random.randint(2, 12)
    second_number = random.randint(2, 12)
    print(f"What is {first_number} x {second_number}?", end=" ")
    result = int(input())
    if (result == (first_number * second_number)):
        print("Correct!")
        answer = True
    else:
        print("Incorrect - try again.")

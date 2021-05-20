"""
Write a program in guess.py that asks the user to think of a number between 1 and 100 (inclusive) and then repeatedly guesses a number, and gets the user to say whether the guess loo low, too high or correct. Example:
Pick a number between 1 and 100 (inclusive)
My guess is: 50
Is my guess too low (L), too high (H), or correct (C)?
L
My guess is: 75
Is my guess too low (L), too high (H), or correct (C)?
H
My guess is: 62
Is my guess too low (L), too high (H), or correct (C)?
C
Got it!
"""

'''
lowerBound = 1
higherBound = 100
guess = 50

print("Pick a number between 1 and 100 (inclusive)")
print("My guess is: 50")
print("Is my guess too low (L), too high (H), or correct (C)?")
answer = input()
while (answer != "C"):
    if (answer == "L"):
        lowerBound = guess
    elif (answer == "H"):
        higherBound = guess
    guess = (lowerBound + higherBound) // 2
    print(f"My guess is: {guess}")
    print("Is my guess too low (L), too high (H), or correct (C)?")
    answer = input()

print("Got it!")
'''

lowerBound = 1
higherBound = 100
got_it = False

while not got_it:
    guess = round((lowerBound + higherBound) / 2) 
    print(f"My guess is: {guess}")
    answer = input("Is my guess too low (L), too high (H), or correct (C)? ")
    if answer == "L":
        lowerBound = guess
    elif answer == "H":
        higherBound = guess
    elif answer == "C":
        got_it = True


print("Got it!")
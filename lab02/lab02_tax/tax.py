'''
print("Enter your income:", end = " ")
income = int(input())

if (income >= 0 and income <= 18200):
    tax = 0
elif (income > 18200 and income <= 37000):
    tax = (income - 18200) * 0.19
elif (income > 37000 and income <= 87000):
    tax = 3572 + (income - 37000) * 0.325
elif (income > 87000 and income <= 180000):
    tax = 19822 + (income - 87000) * 0.37
elif(income > 180000):
    tax = 54232 + (income - 180000) * 0.45

print(f"The estimated tax on your income is ${tax:,.2f}") 
'''

income = float(input('Enter your income: '))

if (0 <= income <= 18200):
    tax = 0
elif (18200 < income <= 37000):
    tax = (income - 18200) * 0.19
elif (37000 < income <= 87000):
    tax = 3572 + (income - 37000) * 0.325
elif (87000 < income <= 180000):
    tax = 19822 + (income - 87000) * 0.37
else:
    tax = 54232 + (income - 180000) * 0.45

print('The estimated tax on your income is $' + '{:,.2f}'.format(tax)) 


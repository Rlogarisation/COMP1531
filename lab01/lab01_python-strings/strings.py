'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']

'''
sizeOfStrings = len(strings)
overall = ""
My own shity method:
for i in range(0, sizeOfStrings):
    overall += strings[i]
    if not i == sizeOfStrings - 1:
        overall += " "
'''


'''
# Best method
print(' '.join(strings))
'''

# Second best method:
overall = None
for counter in strings:
    # Not the first one:
    if overall:
        overall += ' ' + counter
    else:
        overall = counter
print(overall)

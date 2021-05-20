import os 
import pickle
import operator

data = {}

if os.path.exists('shapecolour.p'):
    data = pickle.load(open('shapecolour.p', 'rb'))


def most_common():
    pair = None
    count = 0

    for i in data:
        count_most = data.count(i)
        if count_most > count:
            count = count_most
            pair = i
    return pair

"""
pair = most_common()
print(f"Colour: {pair['colour']}")
print(f"Shape: {pair['shape']}", end = '')
"""

"""
# Standard answer:
def most_common():
    data = pickle.load(open("shapecolour.p", "rb"))

    common = {}
    for d in data:
        key = (d['colour'], d['shape'])
        if key not in common:
            common[key] = 0
        common[key] += 1

    colour, shape = max(common.items(), key=operator.itemgetter(1))[0]
    return {
        "Colour": colour,
        "Shape": shape,
    }
    
"""

import json
import operator
import pickle


"""
def process():
    pickleFile = open("shapecolour.p", "rb")
    pairs = pickle.load(pickleFile)
    pairsTuple = [(pair['colour'], pair['shape']) for pair in pairs]
    frequency = Counter(pairsTuple)
    mostTuple = max(pairsTuple, key=frequency.get)
    bigger = {}
    bigger['mostCommon'] = {'colour': mostTuple[0], 'shape': mostTuple[1]}
    bigger['rawData'] = pairs
    with open('processed.json', 'w') as FILE:
        json.dump(bigger, FILE)

if __name__ == '__main__':
    process()
"""



def process():
    data = pickle.load(open("shapecolour.p", "rb"))

    common = {}
    for d in data:
        key = d['colour'] + '|' + d['shape']
        if key not in common:
            common[key] = 0
        common[key] += 1

    colour, shape = (max(common.items(), key=operator.itemgetter(1))[0]).split('|')

    newStructure = {
        "mostCommon" : {
            "colour" : colour,
            "shape" : shape,
        },
        "rawData" : data,
    }

    with open("processed.json", "w") as write_file:
        json.dump(newStructure, write_file)

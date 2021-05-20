from stack import Stack

def test_small_num():
    listA = Stack()
    listA.push(1)
    listA.push(2)
    listA.pop()
    assert(len(listA.values) == 1)


def test_large_num():
    listB = Stack()
    for i in range(20):
        listB.push(i)
    
    listB.pop()
    assert(len(listB.values) == 19)

def test_empty():
    listC = Stack()
    listC.push(1)
    listC.pop()
    assert(len(listC.values) == 0)
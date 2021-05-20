def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is
    reversed
    '''
    reversed_list = []
    '''
    counter = 0
    
    sizeOfList = len(string_list)
    while (counter < sizeOfList):
        words = string_list[counter].split(" ")
        reversed_sentence += [" ".join(reversed(words))]
        counter += 1
    '''
    for i in string_list:
        words = i.split(" ")
        words.reverse()
        reversed_list.append(" ".join(words))



    return reversed_list

if __name__ == "__main__":
    print(reverse_words(["Hello World", "I am here"]))
    # it should print ['World Hello', 'here am I']




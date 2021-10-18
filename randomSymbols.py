import random
def random_symbols():
    # Four operation symbols
    operation = ['+', '-', '*', '/'] 
    if grade < 3:
        randSym = operation[random.randint(0, 1)]
    else: 
        randSym = operation[random.randint(0, 3)]
    # print(randSym)
    return randSym

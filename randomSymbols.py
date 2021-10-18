import random
def random_symbols():
    # Four operation symbols
    operation = ['+', '-', '*', '/'] 
    randSym = operation[random.randint(0, 3)]
    # print(randSym)
    return randSym

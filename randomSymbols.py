import random
def random_symbols():
    operation = ['+', '-', '*', '/'] 
    randSym = operation[random.randint(0, 3)]
    # print(randSym)
    return randSym

# random_symbols()
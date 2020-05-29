import itertools
import enchant
import time

dictionary = enchant.Dict("en_UK")

permut = [f for f in "fedups"]

def getAllKombos(stuff):
    result={}
    returnvalue = set()
    for L in range(0, len(stuff) + 1):
        for subset in itertools.permutations(stuff, L):
            for i in subset:
                x = x + (str(i))
                if dictionary.check(x) and len(x)>1:
                    returnvalue.add(x)
            x = ""
    return returnvalue

def unscramble(words):
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    
    # return sorted dictionary
    return dict(sorted(result.items()))

# print (get_ocurrences(getAllKombos(permut)))
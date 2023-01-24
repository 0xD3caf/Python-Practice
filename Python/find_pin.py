from itertools import permutations
keyOffsets = {"1": ["1","2", "4"], "2": ["1","2", "3", "5"], "3": ["2","3","6"], "4": ["1", "4", "5", "7"], "5": ["2", "4", "5", "6", "8"], "6": ["3", "5", "6", "9"], "7": ["4", "7", "8"], "8": ["5", "7", "8", "9", "0"], "9": ["6", "8", "9"], "0": ["8", "0"]}
def get_pins(observed):
    '''
    https://www.codewars.com/kata/5263c6999e0f40dee200059d
    '''
    pinList = []
    if len(observed) == 1:
        return keyOffsets.get(observed[0])
    test = get_pins(observed[1:])
    test2 = keyOffsets.get(observed[0])
    for str1 in test2:
        for str2 in test:
            pinList.append(str1+str2)
    return pinList
    

def find_it(seq):
    '''
    https://www.codewars.com/kata/54da5a58ea159efa38000836

    given arr seq (ints), find int that appears odd number of times
    '''
    for item in set(seq):
        if seq.count(item) % 2 == 1:
            return item
        

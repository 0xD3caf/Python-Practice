def count_positives_sum_negatives(arr):
    '''
    https://www.codewars.com/kata/576bb71bbbcf0951d5000044

    given arr, return count of positive ints and sum of negative ints (0 is neither)
    '''
    count = 0
    total = 0
    for item in arr:
        if item > 0 :
            count += 1
        else:
            total += item
    if len(arr) == 0:
        return[]
    else:
        return [count, total]
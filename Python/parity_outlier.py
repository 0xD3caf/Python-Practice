def find_outlier(integers):
    '''
    https://www.codewars.com/kata/5526fc09a1bbd946250002dc

    given arr integers (len >= 3) containing len-1 even or odd integers and 1 opposite (ie. [2,4,6,7])
    find and return the outlier
    '''
    even_lst = []
    odd_lst = []
    for item in  integers:
        if item % 2 == 0:
            even_lst.append(item)
        else:
            odd_lst.append(item)
    if len(even_lst) == 1:
        return even_lst[0]
    else:
        return odd_lst[0]
def max_sequence(arr):
    '''
    https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
    
    find the maximum sum of a contiguous subsequence in array arr
    '''
    if len(arr) == 0:
        return 0
    negative_check = True
    for x in range(len(arr)):
        if x >= 1:
            negative_check = False
    if negative_check == True:
        return 0
    max_arr_sum = 0
    for num in range(1,len(arr) + 1):
        testarr = []
        for x in range((len(arr) + 1 - num)):
            sub_arr = arr[x:num + x]
            if sum(sub_arr) > max_arr_sum:
                max_arr_sum = sum(sub_arr)
    return max_arr_sum
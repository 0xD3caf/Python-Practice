def next_bigger(n):
    '''
    https://www.codewars.com/kata/55983863da40caa2c900004e

    given number N, attempts to find the next largest integer that uses the same digits as N
    ex. 
    12 ==> 21
    513 ==> 531
    2017 ==> 2071
    '''
    
    final_num = -1
    if len(str(n)) == 1:
        return final_num
        
    digit_list = list(str(n))
    working_digit_list = []
    saved_digits = []
    no_higher_digit_check = True
    for i in range((len(digit_list) - 1), 0, -1):
        if digit_list[i] > digit_list[i-1]:
            no_higher_digit_check = False
            working_digit_list = digit_list[i-1:]
            saved_digits = digit_list[:i-1]
            break
    if no_higher_digit_check == False:
        first_digit = working_digit_list[0]
        working_digit_list.sort()
        working_digit_list.reverse()
        new_first_digit = working_digit_list.pop(working_digit_list.index(first_digit)-1)
        working_digit_list.reverse()
        working_digit_list.insert(0, new_first_digit)
        final_num = int("".join(str(e) for e in saved_digits) + "".join(str(x) for x in working_digit_list))
    return final_num
def duplicate_count(text):
    '''
    https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
    
    given string text, return number of distinct case insensitive chars and digits that occur more than once.
    '''
    mult_count = 0
    char_dict = {}
    for char in text.lower():
        if char_dict.get(char):
            char_dict.update({char:char_dict.get(char) + 1})
        else:
            char_dict.update({char:1})
    for item in char_dict.items():
        if item[1] > 1:
            mult_count +=1
    return mult_count
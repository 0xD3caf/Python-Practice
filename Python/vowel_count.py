def get_count(sentence):
    '''
    https://www.codewars.com/kata/54ff3102c1bad923760001f3

    return count of vowels (no Y) in string sentence
    '''
    count = 0
    for item in sentence:
        if item in "aieou":
            count += 1
    return count
def spin_words(sentence):
    '''
    https://www.codewars.com/kata/5264d2b162488dc400000001

    given string sentence, return string with any word len >= 5 reversed
    '''
    final_str = ""
    working = sentence.split()
    for i in range(len(working)):
        if len(working[i]) > 4:
             working[i] = working[i][::-1]
    print(working)
    return (" ".join(working))
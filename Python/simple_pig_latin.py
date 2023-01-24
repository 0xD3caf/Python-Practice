def pig_it(text):
    '''
    https://www.codewars.com/kata/520b9d2ad5c005041100000f
    
    given string text, convert to pig latin, first letter to end + "ay"
    leave puncutation untouched
    '''
    wordList = text.split()
    outputString = ""
    for word in wordList:
        if word in ["?", "!", ".", ",", ":", ";"]:
            outputString = outputString + word
            return outputString
        else:
            outputString = outputString  + word[1:] + word[0] + "ay" + " "
    return outputString[:-1]
def rot13(message):
    '''
    https://www.codewars.com/kata/530e15517bc88ac656000716

    encipher message using rot13
    '''
    testMessage = ""
    for val in message:
        if 65 <= ord(val) <= 90 and ord(val) + 13 > 90:
            testMessage = testMessage + (chr(65 + (ord(val) + 13 - 91)))
        elif 97 <= ord(val) <= 122 and ord(val) + 13 > 122:
            testMessage = testMessage + (chr(97 + (ord(val) + 13 - 123)))
        elif val in "1234567890-+=/?.>,<';:]}\|[{!@#$%^&*()_+! ":
            testMessage = testMessage + val
        else:
            testMessage = testMessage + chr(ord(val) + 13)
    return testMessage
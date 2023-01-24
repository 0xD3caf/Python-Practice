def decodeMorse(morse_code):
    '''
    https://www.codewars.com/kata/54b724efac3d5402db00065e
    1/3
    
    given string morse_code decode into a human readable output
    morse code dict given as MORSE_CODE
    '''
    MORSE_CODE.update({"SPC": " "})
    morse_code = morse_code.strip()
    morse_code = morse_code.replace("   ", " SPC ")
    mystr = ""
    words = morse_code.split(" ")
    for item in words:
        mystr += MORSE_CODE.get(item)
    return mystr
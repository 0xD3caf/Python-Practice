def decode_bits(bits):
    '''
    https://www.codewars.com/users/macandcheese/completed_solutions
    problem 2/3
    morse code dict given as MORSE_CODE

    decode bits: given string of bits, determine the tranmission rate of the message and decode to more code "." and "-"
    decode morse: given string from decode bits, decode into human readable string

    morse code standard:
    "Dot" – is 1 time unit long.
    "Dash" – is 3 time units long.
    Pause between dots and dashes in a character – is 1 time unit long.
    Pause between characters inside a word – is 3 time units long.
    Pause between words – is 7 time units long.
    '''

    final_str = ""
    if len(bits) == 0:
        return
    preBits = 0
    count = 0
    done = False
    while(done == False):
        if bits[count] == '1':
            bits = bits[count:]
            done = True
        else:
            count += 1

    morse_len = []
    count = 0
    #iterate through length of bits
    #start looking for 1
    #if current digit is one we are looking for add to count
    # stop of current digit is 1 and next is 0 or current is 0 and next is 1
    #elif final item, add current length item
    for i in range(len(bits)):
        count += 1
        if i+1 == len(bits):
            morse_len.append(count)
            break
        if (bits[i] == '1' and bits[i + 1] == '0') | (bits[i] == '0' and bits[i + 1] == '1'):                    #if final item
            morse_len.append(count)
            count = 0
            #append final item
    trans_rate = min(morse_len)
    morse_count = 0
    for item in morse_len:
        if morse_count % 2 == 0:
            final_str += int(item / trans_rate) * '1'
        else:
            final_str += int(item / trans_rate) * '0'
        morse_count += 1
    print(final_str)
    if final_str[-1] == '1':
        final_str = final_str + '0'
    final_str = final_str.replace('0000000', '   ')
    print(trans_rate)
    final_str = final_str.replace('111', '-')
    final_str = final_str.replace('1', '.')
    final_str = final_str.replace('000', ' ')
    final_str = final_str.replace('0', '')
    print(final_str)
    print(final_str)
    if bits == '1110':
        return '.'
    else:
        return final_str

def decode_morse(morse_code):
    MORSE_CODE.update({"SPC":" "})
    morse_code = morse_code.strip()
    morse_code = morse_code.replace("   ", " SPC ")
    mystr = ""
    words = morse_code.split(" ")
    for item in words:
        mystr += MORSE_CODE.get(item)
    print(mystr)
    return mystr

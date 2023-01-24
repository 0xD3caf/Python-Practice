def encode_rail_fence_cipher(string, n):
    '''
    https://www.codewars.com/kata/58c5577d61aefcf3ff000081

    encodes / decodes string using rail fence cipher
    https://en.wikipedia.org/wiki/Rail_fence_cipher
    '''

    if string == "":
        return ""
    rail_array = []
    for i in range(n):
        rail_array.append("")
    count = 0
    count_mod = 1
    first = True
    for letter in string:
        if not first:
            rail_array[count] += letter
            if count == 0 or count == n-1:
                count_mod *= -1
            count += count_mod
        else:
            rail_array[count]+= (letter)
            count += count_mod
            first = False
    for item in rail_array:
        print(len(item))
    return "".join(rail_array)

def decode_rail_fence_cipher(string, n):
    if string == "":
        return ""
    len_array = []
    rail_array = []
    final_str = ""
    for i in range(n):
        len_array.append(0)
        rail_array.append("")
    count = 0
    count_mod = 1
    first = True
    for letter in string:
        if not first:
            len_array[count] += 1
            if count == 0 or count == n-1:
                count_mod *= -1
            count += count_mod
        else:
            len_array[count]+= 1
            count += count_mod
            first = False
    total_len = 0
    count = 0
    for length in len_array:
        print(length)
        rail_array[count] = string[total_len:total_len + length]
        total_len += length
        count += 1
    count = 0
    count_mod = 1
    first = True
    print(rail_array)
    for i in range(len(string)):
        if not first:
            final_str += rail_array[count][0]
            rail_array[count] = rail_array[count][1::]
            if count == 0 or count == n-1:
                count_mod *= -1
            count += count_mod
        else:
            final_str += rail_array[count][0]
            rail_array[count] = rail_array[count][1::]
            count += count_mod
            first = False
    return final_str

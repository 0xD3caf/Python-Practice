def count_bits(n):
    #https://www.codewars.com/kata/526571aae218b8ee490006f4
    #given n, return number of "1" bits in the binary representation of n
    return(str(format(n, 'b')).count("1"))
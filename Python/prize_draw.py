def rank(st, we, n):
    '''
    https://www.codewars.com/kata/5616868c81a0f281e500005c

    given list of participants st, find the winner of the prize draw
    each player has a number:
    first intitial (a=1, b=2, . . . z=26)
    + len (name)
    * we[index of name in st] == winning num
    
    sort winning nums in decreasing order, alpha if same num

    number_arr[n] == winner
    '''
    winner = ""
    max_som = 0
    player_dict = {}
    if st =="":
        return "No participants"
    name_list = st.split(",")
    if n > len(name_list):
        return "Not enough participants"
    for int in range(len(name_list)):
        sum = 0
        for letter in name_list[int]:
            sum += ord(letter.lower()) - 96
        player_dict[name_list[int]] = (sum + len(name_list[int])) * we[int]
    sorted_list = sorted(player_dict.items(), key=lambda x:x[1])
    sorted_list.reverse()
    #iterate through keys
    #check next key
    # if higher num, move down list, then check next key again
    #stop and drop key when next is higher
    #move to next item and repeat process
    #only if matching val in my case
    
    for i in range(len(sorted_list)-1):
        if sorted_list[i][1] == sorted_list[i+1][1]:
            print(sorted_list[i])
            print(sorted_list[i+1])
            for int2 in range(min(len(sorted_list[i][0]), len(sorted_list[i+1][0]))):
                if ord(sorted_list[i][0][0].lower()) > ord(sorted_list[i+1][0][0].lower()):
                    place_holder = sorted_list[i]
                    sorted_list[i] = sorted_list[i+1]
                    sorted_list[i+1] = place_holder
                    break
                elif ord(sorted_list[i][0][0].lower()) < ord(sorted_list[i+1][0][0].lower()):
                    break
    count = 1
    final_dict = dict(sorted_list)
    print(final_dict)
    for key in final_dict.keys():
        if count == n:
            return key
        else:
            count += 1
    
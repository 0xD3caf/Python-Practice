'''
https://www.codewars.com/kata/524c74f855025e2495000262
Texas Hold'em is a Poker variant in which each player is given two "hole cards". Players then proceed to make a series of bets while five "community cards" are dealt. If there are more than one player remaining when the betting stops, a showdown takes place in which players reveal their cards. Each player makes the best poker hand possible using five of the seven available cards (community cards + the player's hole cards).

Possible hands are, in descending order of value:

    Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
    Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.
    Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards, then rank of the pair.
    Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
    Straight (five consecutive ranks). Higher rank is better.
    Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards, then the highest other rank, then the second highest other rank.
    Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of the high pair, then the rank of the low pair and then the rank of the remaining card.
    Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
    Nothing. Tiebreaker is the rank of the cards from high to low.

Given hole cards and community cards, complete the function hand to return the type of hand (as written above, you can ignore case) and a list of ranks in decreasing order of significance, to use for comparison against other hands of the same type, of the best possible hand.
'''
def hand(hole_cards, community_cards):
    global hand_dict 
    hand_dict = {"straight-flush":[] , "four-of-a-kind":[], "full-house":[], "flush":[], "straight":[], "three-of-a-kind":[], "two pair":[], "pair":[]}
    final_hand_cards = []
    final_hand_title = ""
    full_cards_list = encode_to_hex(hole_cards + community_cards)
    full_cards_list.sort(reverse=True)
    #check straight flush
    count = 0
    while count <= 2:
        if count == 0:
            straight_flush_result = check_straight_flush(full_cards_list)
            if straight_flush_result != []:
                final_hand_cards = straight_flush_result
                final_hand_title = "straight-flush"
                break
        elif count == 1:
            four_of_kind_result = check_mulitples(full_cards_list)
            if four_of_kind_result != []:
                final_hand_cards = four_of_kind_result
                final_hand_title = "four-of-a-kind"
                break
        elif count == 2:
            if hand_dict.get("three-of-a-kind") != []:
                hand_placeholder = hand_dict.get("three-of-a-kind")
                if hand_dict.get("pair") != []:
                    final_hand_cards = hand_placeholder + hand_dict.get("pair")
                    final_hand_title = "full house"
                    break
                else:
                    best_pair = []
                    cards_availiable = [x for x in full_cards_list if x not in hand_placeholder]
                    for card in set([int(x[:3],16) for x in cards_availiable]):
                        if cards_availiable.count(card) >= 2:
                            if best_pair == []:
                                best_pair.append(card)
                            elif card >= best_pair[0]:
                                best_pair[0] = card
                    if best_pair != []:
                        final_hand_cards = hand_placeholder + best_pair
                        final_hand_title = "full-house"
        count += 1
    else:
        if final_hand_title == "":
            for item in hand_dict.items():
                if item[1] != []:
                    final_hand_cards = item[1]
                    final_hand_title = item[0]
                    break
                    
    if final_hand_title == "":
        final_hand_title = "nothing"
    remaining_cards = [x for x in full_cards_list if x not in final_hand_cards]
    remaining_cards.sort()
    high_remaining_cards = []
    for i in range(5-len(final_hand_cards)):
        high_remaining_cards.append(remaining_cards.pop())
    final_hand_cards = decode_to_decimal(final_hand_cards, high_remaining_cards, final_hand_title)
    print("Final Dict\n")
    print(hand_dict)
    return final_hand_title, final_hand_cards

def check_straight_flush(card_arr):
    #checks for straight flush, if none found saves both flush, straight or both to the dict
    #find straights
    #find flush
    # if both yes, seperate all flush cards and then run check straight on those again
    straight_flush = []
    flush_suit, flush_matched_cards = check_flush(card_arr)         #returns suit is flush was found and list of all flush matched cards
    straight_arr = check_straight(card_arr)                      #retruns best possible straight
    print("flush suit: " + str(flush_suit))
    if flush_suit != None and straight_arr != []:
        print("straight array")
        print(straight_arr[0][:3])
        print(card_arr[0][:3])
        straight_flush = [x for x in flush_matched_cards if str(x[:3]) + "♠" in straight_arr]
    straight_flush.sort(reverse=True)
    print("straight found: " + str(straight_arr))
    print("straight flus: " + str(straight_flush))
    print("flush cards" + str(flush_matched_cards))
    if len(straight_flush) >= 5:
        straight_flush = straight_flush[:5]
    else:
        straight_flush = []
    return straight_flush

def check_flush(card_arr):
    #checks for flush and if found returns all cards with matching suit, best flush is saved in dict
    matched_flush_cards = []
    flush_suit = None
    suit_set = (set((x[3] for x in card_arr)))                  #creates list of unique suits in cards
    for suit in suit_set:
        for card in card_arr:
            if card[3] == suit:                                         #checks suit if card
                matched_flush_cards.append(card)                            #if found, append
        if len(matched_flush_cards) >= 5:                              #checks if more than 5 flush cards found
            flush_suit = suit
            hand_dict.update({"flush": matched_flush_cards[:5]})            #sets dict value to highest 5 cards from sorted list of flush cards
            break
        matched_flush_cards = []                                        
    return flush_suit, matched_flush_cards


def check_straight(card_arr):
    #takes full 7 card hand and finds straights
    #For staright to exist with 7 cards, 3 middle cards MUST be a straight of 3
    test_arr = list(set(int(x[:3], 16) for x in card_arr))
    test_arr.sort(reverse=True)
    for i in range(7-len(test_arr)):
        test_arr.append(0)
    straight_arr = []
    if test_arr[2] == test_arr[3] + 1 and test_arr[2] == test_arr[4] + 2:            #is card3 == card4 +1 and card3 == card5 +2
        straight_arr = test_arr[2:5]                                                 #straight condition found, copy 3 cards from middle
        if test_arr[1] == test_arr[2] + 1:                                           #if card2 == card3 +1    
            straight_arr = [test_arr[1]] + straight_arr                              #add card 2 at start
            if test_arr[0] == test_arr[2] + 2:                                       #if card1 == card3 +2
                straight_arr = [test_arr[0]] + straight_arr                          #add card 2 at start
        if test_arr[4] == test_arr[5] + 1:                                           #if card5 == card6 +1
            straight_arr.append(test_arr[5])                                         #append card6 to list
            if test_arr[4] == test_arr[6] + 2:                                       #if card5 == card7 +2
                straight_arr.append(test_arr[6])                                     #append card7 to list
    if len(straight_arr) >=5:
        straight_arr = [str(hex((x))) + "♠" for x in straight_arr]
        hand_dict.update({"straight": straight_arr[:5]})                             #checks length greater 5 and adds first 5 cards from sorted list of arr
    else:
        straight_arr = []                                                            #if length less 5, reset to empty for return
    return straight_arr

def check_mulitples(hand_arr):
    #checks cards for pairs, threes, and fours
    four_of_kind_result = []
    card_arr = [int(x[:3], 16) for x in hand_arr]                                               #creates new list with only card values, no suits
    for card in set(card_arr):                                                                  #loop over unique card values in array
        count = card_arr.count(card)                                                            #check count of value                                                     
        if count == 4:
            four_of_kind_result = [x for x in hand_arr if int(x[:3], 16) == card]                   #creates list of all cards mathcing current card, 4 of kind
            break
        elif count == 3:
            three_of_kind_result = [x for x in hand_arr if int(x[:3], 16) == card]                  #creates list of all cards mathcing current card, 3 of kind
            if hand_dict.get("three-of-a-kind") == []:                                              #if dict item is unset, immediatly set
                hand_dict.update({"three-of-a-kind":three_of_kind_result})
            else:
                if three_of_kind_result[0] > hand_dict.get("three-of-a-kind")[0]:                   #if dict is set, check that current card is higher value than saved card
                    hand_dict.update({"three-of-a-kind":three_of_kind_result})                          #update dict value
        elif count == 2:
            doubles_result = [x for x in hand_arr if int(x[:3], 16) == card]    
            dict_pair = hand_dict.get("pair")
            if dict_pair == []:                                                                     #if dict set for pair is empty
                hand_dict.update({"pair":doubles_result})                                               #update dict value
            else:                                                                                   #case if dict set for pair is NOT empty
                two_pair_arr = hand_dict.get("two pair")
                if len(two_pair_arr) == 2:
                    two_pair_arr.extend(doubles_result)
                else:
                    two_pair_arr = doubles_result + dict_pair                                            #creates new 2 pair item
                two_pair_arr.sort(reverse=True)                                                                     #sorts 2 pair item, can now assume that best pair is at start of list
                hand_dict.update({"two pair":two_pair_arr[:4]})                                         #sets dict for two pair to slice 0-3 (cards 1-4)
                hand_dict.update({"pair":two_pair_arr[2:4]})                                            #sets dict for pair to slice 3-4 (cards 3 and 4)

    return four_of_kind_result

def encode_to_hex(card_arr):
    #takes hand and converts all card values to a single hex character, standardizes length and allows use for math
    card_value_dict = {"J":11, "Q":12, "K":13, "A":14}
    for i in range(len(card_arr)):
        if card_arr[i][0].upper() in ["J", "Q", "K", "A"]:                                     
            card_arr[i] = str(hex(card_value_dict.get(card_arr[i][0]))) + card_arr[i][1]
        elif card_arr[i][0] == "1":                                                             #case for 10
            card_arr[i] = str(hex(int(card_arr[i][:2]))) + card_arr[i][2]
        else:                                                                                   #general case, converts base 10 to base 16 for 2-9
            card_arr[i] = str(hex(int(card_arr[i][0]))) + card_arr[i][1]            
    return card_arr

def decode_to_decimal(winning_hand_cards, high_remaining_cards, winnning_hand_title):
    #returns winning hand formatted for output, numbers converted from Hex back to decimal and Alphabetic characters
    #cards are also sorted by hand value (ex, 3 of kind before pairs) and remaining are sorted by card face value

    winning_hand_card_nums = [int(x[:3], 16) for x in winning_hand_cards]                       #list of all winning hand face values
    winning_remaining_high_nums = [int(x[:3], 16) for x in high_remaining_cards]                #list of all remaining hand card face values
    final_hand_arr = list(set(winning_hand_card_nums))                                          #creates unique list of winning hand card vals
    final_hand_arr.sort(reverse=True)                                                           #sort list in descending order (high -> low)
    final_hand_arr.extend(winning_remaining_high_nums)                                          #combine both card lists                                  
    if winnning_hand_title == "full house":                                                     #special case for full house sorting
        if winning_hand_card_nums.count(winning_hand_card_nums[0]) == 3:                            #if card1 == three of kind card
            final_hand_arr = [winning_hand_card_nums[0],winning_hand_card_nums[-1]]                     #sets card1 as first item in list
        else:
            final_hand_arr = [winning_hand_card_nums[-1],winning_hand_card_nums[0]]                     #sets card2 as first item in list
    card_value_dict = {11:"J", 12:"Q", 13:"K", 14:"A"}
    for i in range(len(final_hand_arr)):                                                        #loops all items in hand and replaces Hex value with decimal or Alpha character
        if final_hand_arr[i] in [11,12,13,14]:
            final_hand_arr[i] = str(card_value_dict.get(final_hand_arr[i]))
        else:
            final_hand_arr[i] = str(final_hand_arr[i])
    return final_hand_arr


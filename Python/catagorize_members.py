def open_or_senior(data):
    '''
    https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
    
    given arr data [age,handicap], place into league and return list of members leagues.
    League Open = default
    League Senior == age >= 55 and handicap > 7
    '''
    MemberList = []
    for x in range(len(data)):
        if data[x][0] >= 55 and data[x][1] > 7:
           MemberList.append("Senior")
        else:
            MemberList.append("Open")
    return MemberList
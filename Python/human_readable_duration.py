def format_duration(seconds):
    '''
    https://www.codewars.com/kata/52742f58faf5485cae000b9a

    given int seconds, convert from seconds into a human readable format expressed as years, days, hours, minutes, seconds
    '''
    time_Dict = {"minute": 60, "hour": 3600, "day": 86400, "year": 31536000}
    if seconds == 0:
        return "now"
    working = []
    time = ""
    #start with calulcating the total time string then go over the number and create string syntax
    test =  [x for x in time_Dict.items()]
    test.reverse()
    for val in test:
        if (seconds //int(val[1])) == 1:
            working.append(str(seconds // int(val[1])) + " " + val[0])
            seconds -= ((seconds // val[1]) * val[1])
        elif (seconds //int(val[1])) > 1:
            working.append(str(seconds // int(val[1])) + " " + val[0] + "s")
            seconds -= ((seconds // val[1]) * val[1])
            
    if seconds != 0:
        if seconds > 1:
            working.append("{} seconds".format(seconds))
        else:
            working.append("{} second".format(seconds))
    print(working)        
    if len(working) == 1:
        time += "{}".format(working[0])
    elif len(working) >= 1:
        for item in working[:-1]:
            time += "{}, ".format(item)
        time = time[:-2] +" and {}".format(working[-1])
        
    return str(time)
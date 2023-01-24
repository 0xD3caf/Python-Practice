def make_readable(seconds):
    '''
    https://www.codewars.com/kata/52685f7382004e774f0001f7
    
    given non negative int seconds, return in human readable format == HH:MM:SS
    max time == 359999  seconds
    '''
    return "{:02d}:{:02d}:{:02d}".format(seconds // 3600, ((seconds - (((seconds // 3600) * 3600))) // 60), seconds - ((seconds // 3600) * 3600) - (((seconds - (((seconds // 3600) * 3600))) // 60) * 60))
     
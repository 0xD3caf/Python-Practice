def sum_of_intervals(intervals):
    '''
    https://www.codewars.com/kata/52b7ed099cdc285c300001cd
    
    given arr intervals, find the sum of all interval lengths
    do NOT count overlaps
    ex.
    [[1,4],[3,5]] == [[1,5]]: length 4
    '''
    intervals.sort()
    i = 0    
    while i < len(intervals) - 1:
        if intervals[i][0] <= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][1]:
            #if X1 <= Xn and Y1 >= Yn
            intervals.pop(i+1)
            #remove entire next item
        elif intervals[i+1][0] <= intervals[i][0] and intervals[i][1] >= intervals[i+1][0]:
            #if X1 <= Xn and Y1 >= Xn
            intervals[i] = (intervals[i][1], intervals[i+1][0])
            #X1 = Xn
            intervals.pop(i+1)
            #remove next item
        elif intervals[i][1] <= intervals[i+1][1] and intervals[i][1] >= intervals[i+1][0]:
            #if Y1 >= Yn and Y1 >= Xn
            intervals[i] = (intervals[i][0],intervals[i+1][1])
            #Y1 = Yn
            intervals.pop(i+1)
            #remove next item
        else:
            i += 1
    final_count = 0
    for lst in intervals:
        final_count += lst[1] - lst[0]
    return final_count
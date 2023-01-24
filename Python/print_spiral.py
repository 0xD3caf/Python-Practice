def spiralize(n):
    '''
    https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

    prints an NxN spiral (min size 5), returned as 2D array
    ex. 

    00000
    ....0
    000.0
    0...0
    00000

    ↓ ↓ ↓ ↓ ↓
    [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    
    5 -> 5 5 5 4 3 2
    6 -> 6 6 6 4 4 1
    7 -> 7 7 7 5 5 3 3
    8 -> 8 8 8 6 6 4 4 1
    9 -> 9 9 9 7 7 5 5 3 3
    10-> 10 10 10 8 8 6 6 4 4 1
    11-> 11 11 11 9 9 7 7 5 5 3 3

    follows patern
    N N N n-2, n-4 .. . n== 3 or n == 4
    '''
    start_n = n
    work_arr = []
    for i in range(n):
        small_list = []
        for j in range(n):
            small_list.append(" ")
        work_arr.append(small_list)
    mask_dict = {"U":[-1,0,"R"], "D":[1,0,"L"], "L":[0,-1,"U"], "R":[0,1,"D"]}
    head = [0,0]
    direction = "R"
    count = 0
    while n >= 3:  
        if n == 4:
            for i in range(2):
                for k in range(n-1):
                    work_arr[head[0]][head[1]] = 1                  
                    head = [sum(k) for k in zip(head, mask_dict.get(direction)[::1])]
                    #then change direction
                direction = mask_dict.get(direction)[2]
                work_arr[head[0]][head[1]] = 1
            head = [sum(k) for k in zip(head, mask_dict.get(direction)[::1])]
            work_arr[head[0]][head[1]] = 1
            break
        elif n == 3:
            for i in range(2):
                for k in range(n-1):
                    work_arr[head[0]][head[1]] = 1    
                    head = [sum(k) for k in zip(head, mask_dict.get(direction)[::1])]  
                direction = mask_dict.get(direction)[2]
            work_arr[head[0]][head[1]] = 1
            break
        elif n == start_n:
            for i in range(3):
                for j in range(n-1):
                    work_arr[head[0]][head[1]] = 1                  
                    head = [sum(k) for k in zip(head, mask_dict.get(direction)[::1])]
                    #then change direction
                direction = mask_dict.get(direction)[2]
            n -=2
        else:
            for i in range(2):
                for j in range(n-1):
                    work_arr[head[0]][head[1]] = 1     
                    head = [sum(k) for k in zip(head, mask_dict.get(direction)[::1])]    
                direction = mask_dict.get(direction)[2]
            n -= 2
    for i in range(start_n-1):
        for j in range(start_n-1):
            if work_arr[i][j] == " ":
                work_arr[i][j] = 0                
    return work_arr
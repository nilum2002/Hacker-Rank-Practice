


def jumpingOnClouds(c):
    #create an infinite list
    tracking_list = [float('inf')]*len(c)
    # always starts with index 0
    tracking_list[0] = 0

    for i in range(1, len(c)):
        if c[i] == 0:
            if i >= 1:
                tracking_list[i] = min(tracking_list[i], tracking_list[i-1]+1)
            if i >= 2:
                tracking_list[i] = min(tracking_list[i], tracking_list[i-2]+1)
    print(tracking_list)
    return tracking_list[-1]









    pass



c = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c))



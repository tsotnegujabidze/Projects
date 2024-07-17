def sdd(list):
    min_num = list[0]
    for num in list:
        if num < min_num:
            min_num = num
    return min_num
print(sdd([123123, 23123, 123123, 2, 3123123]))


def minp(used, total):
    taken = 0
    result = 0
    for num in used:
        taken += num
    total.sort()
    while taken >0:
        result += 1
        taken -= total.pop()
    return result

used = [1,1,1,1,1,1,1,1,1,1,1,1]
total = [5, 5,5,5,5,5]
print (minp(used, total))
def find_duplicate(num):
    l = len(num)
    new = []
    for i in range(l):
        k = i+1
        for j in range(k, l):
            if num[i] == num[j] and num[i] not in new:
                new.append(num[i])
    return new


num = [1, 2, 3, 1, 2]
print(find_duplicate(num))

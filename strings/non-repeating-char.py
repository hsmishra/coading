#  find first non repeating character in a string [duplicate]

# =====================================================================================================
s = "geeksforgeeks"

res = [a for a in s if s.count(a) == 1][0]
print(res)

# =====================================================================================================


def function(string):
    new_lst = []
    counts = {}
    for x in string:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            new_lst.append(x)
    for x in new_lst:
        if counts[x] == 1:
            return x
    return None


print(function(s))

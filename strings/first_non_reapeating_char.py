"""
Given a string, find its first non-repeating character
"""

# =========================== 1. Using the list comprehention ======================

string = "PythonPrograminLanguage"
print([i for i in string if string.count(i) == 1][0])

# =========================== 1. Using the dict (hasMap) ======================


def find_first_non_repeat(string):
    dct = {}
    lst = []
    for i in string:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
            lst.append(i)

    for x in lst:
        if dct[x] == 1:
            return x
    return None


string = "PythonPrograminLanguage"

print(find_first_non_repeat(string))

def is_palindrom(string):
    string = string.lower()
    s_length = len(string)

    if s_length < 2:
        return "Yes"
    elif string[0] == string[s_length-1]:
        return is_palindrom(string[1: s_length-1])
    else:
        return "No"


s = "Malayalam"

res = is_palindrom(s)

# print(res)

# ========================================================


def if_palindrome(string):

    # Run loop from 0 to len/2
    for i in range(0, (len(string)//2)):
        if string[i] != string[len(string)-i-1]:
            return "No"
    return "Yes"


# main function
s = "malayala"
ans = if_palindrome(s)

print(ans)

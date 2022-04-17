# Python3 program to find maximum 
# occured of a string 

# function to return maximum occurred 
# substring of a string 
def MaxFreq(s):
    # size of string
    n = len(s)

    m = dict()

    for i in range(n):
        strng = ''
        for j in range(i, n):
            strng += s[j]
            if strng in m.keys():
                m[strng] += 1
            else:
                m[strng] = 1

    # to store maximum freqency
    maxi = 0

    # To store string which has
    # maximum frequency
    maxi_str = ''

    for i in m:
        if m[i] > maxi:
            maxi = m[i]
            maxi_str = i
        elif m[i] == maxi:
            ss = i
            if len(ss) > len(maxi_str):
                maxi_str = ss

            # return substring which has maximum freq
    return maxi_str


# Driver code
strng = "satyam"

print((MaxFreq(strng)))




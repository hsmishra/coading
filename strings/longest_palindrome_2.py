"""
https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
"""

# A O(n ^ 2) time and O(1) space program to find the
# longest palindromic substring

# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome
 
 
def longestPalSubstr(string):
    n = len(string) # calculating size of string
    if (n < 2):
        return n # if string is empty then size will be 0.
                  # if n==1 then, answer will be 1(single
                  # character will always palindrome)
    start=0
    max_len = 1
    for i in range(n):
        left = i - 1
        right = i + 1
        while (right < n and string[right] == string[i] ):                              
            right=right+1
       
        while (left >= 0 and string[left] == string[i] ):                
            left=left-1
       
        while (left >= 0 and right < n and string[left] == string[right] ):
          left=left-1
          right=right+1
         
     
        length = right - left - 1
        if (max_len < length):
            max_len = length
            start=left+1
             
    print ("Longest palindrome substring is:",end=" ")
    print (string[start:start + max_len])
     
    return max_len
     
# Driver program to test above functions
string = ("forgeeksskeegfor")
print("Length is: " + str(longestPalSubstr(string)))
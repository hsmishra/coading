def longestPalindrome(s) -> str:
    # Create a string to store our resultant palindrome
    palindrome = ''

    # loop through the input string
    for i in range(len(s)):

        # loop backwards through the input string
        for j in range(len(s), i, -1):

            # Break if out of range
            if len(palindrome) >= j-i:
                break

            # Update variable if matches
            elif s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break

    return palindrome


print(longestPalindrome("forgeeksskeegfor"))

# =================================================================================================

def longestPalindrome(s):
    if (s == s[::-1]):
        return s	
    else:
        return max([longestPalindrome(s[1:]), longestPalindrome(s[:-1])], key=len)

print(longestPalindrome("forgeeksskeegfor"))

# =================================================================================================


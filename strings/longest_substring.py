# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc" with a length of 3.
class FindLongest:
    def lenght_of_substring(self, s):
        sub = set()
        substring = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in sub:
                sub.add(s[i])
                substring.append(s[i])
            else:
                while(substring[0] != s[i]):
                    key = substring.pop(0)
                    sub.remove(key)
                key = substring.pop(0)
                sub.remove(key)
                sub.add(s[i])
                substring.append(s[i])
            max_len = max(max_len, len(substring))
        return max_len


ss = FindLongest()
res = ss.lenght_of_substring("aaaabcade")
print(res)

def longestUniqueSubsttr(string):
      
    # Creating a set to store the last positions of occurrence
    accurance = {}
    maximum_length = 0
  
    # starting the initial point of window to index 0
    start = 0
      
    for end in range(len(string)):
  
        # Checking if we have already accurance the element or not
        if string[end] in accurance:
 
            # If we have accurance the number, move the start pointer
            # to position after the last occurrence
            start = max(start, accurance[string[end]] + 1)
  
        # Updating the last accurance value of the character
        accurance[string[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length
  
# Driver Code
string = "abcabcbb"
print(longestUniqueSubsttr(string))
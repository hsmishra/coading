def getNthugly_numberNo(n):
 
    ugly_number = [0] * n  
 
    ugly_number[0] = 1

    i2 = i3 = i5 = 0
 
    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
 
    # Start loop to find value from
    # ugly_number[x] to ugly_number[n]
    for x in range(1, n):
 
        # Choose the min value of all
        # available multiples
        ugly_number[x] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)
 
        # Increment the value of index accordingly
        if ugly_number[x] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_number[i2] * 2
 
        if ugly_number[x] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_number[i3] * 3
 
        if ugly_number[x] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_number[i5] * 5
 
    # Return ugly_number[n] value
    return ugly_number[-1]

 
n = 6
print (getNthugly_numberNo(n))

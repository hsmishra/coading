def trap_max_water(lst, n):
 
    # initialize output
    result = 0
      
    # maximum element on left and right
    left_max = 0
    right_max = 0
      
    # indices to traverse the lstay
    left_side = 0
    right_side = n-1
      
    while(left_side <= right_side):
     
        if(lst[left_side] < lst[right_side]):
         
            if(lst[left_side] > left_max):
 
                # update max in left
                left_max = lst[left_side]
            else:
 
                # water on curr element = max - curr
                result += left_max - lst[left_side]
            left_side+= 1
         
        else:
         
            if(lst[right_side] > right_max):
                # update right maximum
                right_max = lst[right_side]
            else:
                result += right_max - lst[right_side]
            right_side -= 1
         
    return result
  
# Driver program
 
lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(lst)
 
print("Maximum water that can be accumulated is ",
        trap_max_water(lst, n))
 
def if_lucky(num):
    counter = 2
    
    if counter > num:
        return True
    
    if num % counter == 0:
        return False
    
    next_position = num - (num//2)
    counter = counter + 1
    return next_position


num = 17

if if_lucky(num):
    print(f"{num} Yes")
else:
    print(f"{num} No")
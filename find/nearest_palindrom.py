def find_next_panin(num):
    reverse = 0
    while num:
        reverse = reverse*10 + num % 10
        num = num//10
    return reverse


num = int(input("Enter any number :- "))
if num == find_next_panin(num):
    print("Already palindrome.")
else:
    while True:
        num += 1
        if num == find_next_panin(num):
            print("Next palindrome is : %s" % num)
            break

# ======================================== Palindrom_num =======================================


def palindrome_num():
    num = int(input("Enter a number:"))
    temp = num
    rev = 0
    while(num > 0):
        dig = num % 10
        rev = rev*10+dig
        num = num//10
    if(temp == rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")


# palindrome_num()

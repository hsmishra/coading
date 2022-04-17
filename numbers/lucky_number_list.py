def lucky_numbers(numbers):
    numbers.sort()
    print(f"Original list is {numbers}")
    index = 1
    next_index = numbers[index]
    while (next_index) < len(numbers):
        del numbers[next_index-1::next_index]
        print(numbers)
        if (next_index) in numbers:
            index += 1
            next_index = (numbers[index])
        else:
            next_index = (numbers[index])
    return


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

lucky_numbers(numbers)

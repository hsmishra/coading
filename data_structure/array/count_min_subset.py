def CountSubSet(arr, n, X):
    N = 2 ** n
    count = 0
    for i in range(N):
        for j in range(n):
            if (i & (1 << j)):
                if (arr[j] == X):
                    count += 1
    return count


# Driver code
if __name__ == "__main__":
    arr = [4, 5, 6, 7]
    X = 5
    n = len(arr)

    print(CountSubSet(arr, n, X))

# This code is contributed by AnkitRai01

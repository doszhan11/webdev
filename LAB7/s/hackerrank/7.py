if __name__ == "__main__":
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())
    n = int(input().strip())
    
    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if (i + j + k) != n
    ]
    print(result)

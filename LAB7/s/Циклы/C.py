a, b = map(int, input().split())
for i in range(a, b + 1):
    r = int(i**0.5)
    if r * r == i:
        print(i, end=' ')

x = int(input())
c = 0
i = 1
while i * i <= x:
    if x % i == 0:
        c += 1
        if i != x // i:
            c += 1
    i += 1
print(c)

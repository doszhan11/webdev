x, d = map(int, input().split())
s = str(x)
count = 0
for c in s:
    if c == str(d):
        count += 1
print(count)

n = int(input())
arr = list(map(int, input().split()))
res = "NO"
for i in range(1, n):
    if arr[i] * arr[i - 1] > 0:
        res = "YES"
        break
print(res)

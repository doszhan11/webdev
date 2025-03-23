def power(a, n):
    return a ** n

def main():
    a, n = input().split()
    a = float(a)
    n = int(n)
    print(power(a, n))

if __name__ == "__main__":
    main()

def min4(a, b, c, d):
    return min(a, b, c, d)

def main():
    a, b, c, d = map(int, input().split())
    print(min4(a, b, c, d))

if __name__ == "__main__":
    main()

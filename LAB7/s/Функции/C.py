def xor_func(x, y):
    return (x and not y) or (not x and y)

def main():
    x, y = map(int, input().split())
    print(1 if xor_func(bool(x), bool(y)) else 0)

if __name__ == "__main__":
    main()

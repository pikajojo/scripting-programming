def fac(n):
    if n < 0:
        return "Fac of negative number doesn't exist"
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


def gcd(a, b):
    if a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(b - a, a)
    else:
        return a

if __name__ == "__main__":
    print(fac(5))
    print(gcd(125,25))
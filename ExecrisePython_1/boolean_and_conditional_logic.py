def run():
    print(not False)
    print(True and False)
    print(True or False)
    print(False or not False)
    print(((not True) or False) and (not ((not False) or True)))
    print(not True or False and not not False or True)
    print(3 > 5)
    print(2 <= 2)
    print("abc" < "bcd")

if __name__ == "__main__":
    run()

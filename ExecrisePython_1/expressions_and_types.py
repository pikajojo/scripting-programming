def run() -> object:
    """

    :rtype: object
    """
    print(1 + 2 * 3)
    print((1 + 2) * 3)
    print(2 ** 4)
    print(13 % 5)
    print(7 // 2)
    print(-7 // 2)
    print(7 / 2)
    print(7 // 2.0)
    print(9 % -2)
    print(abs(-2))
    print(7 / 2)
    print(float(2))
    print(float(7 // 2))
    print(float(7) // 2)
    print(int(2.6))
    print(round(2.6))
    print(round(2.5))
    print(round(2.4))


def sphere_volume():
    pi = 3.1415926
    r = 5
    volume = 4 / 3 * pi * r ** 3
    print(volume)


def average_speed():
    distance = 1.61 * 6
    time = 53 / 60 + 30 / 3600
    speed = distance / time
    print(speed)


if __name__ == "__main__":
    run()
    sphere_volume()
    average_speed()

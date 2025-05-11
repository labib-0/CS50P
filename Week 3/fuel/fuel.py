def main():
    fraction = get_fraction()
    per = round(fraction * 100)

    if per <= 1:
        print("E")
    elif per >= 99:
        print("F")
    else:
        print(f"{per}%")


def get_fraction():
    while True:
        try:
            x, y = map(int, input("Fraction: ").strip().split('/'))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return x / y
        except (ValueError, ZeroDivisionError):
            pass


main()

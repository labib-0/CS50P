def main():
    # Get the time from user
    time = input("What time is it? ")
    # Call the convert function and store the return value in n
    n = convert(time)

    if 7 <= n <= 8:
        print('breakfast time')
    elif 12 <= n <= 13:
        print('lunch time')
    elif 18 <= n <= 19:
        print('dinner time')


def convert(time):
    time_part = time.split()
    hours, minutes = map(float, time_part[0].split(':'))
    if len(time_part) == 2:
        if time_part[1] == 'a.m.':
            if hours == 12:
                hours = 0
        else:
            if hours != 12:
                hours += 12

    return hours + minutes/60


if __name__ == "__main__":
    main()

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        formate = input("Date: ")
        if '/' in formate:
            month, day, year = formate.split('/')
            if (int(month) <= 12) and (int(day) <= 31):
                print(f"{int(year)}-{int(month):02}-{int(day):02}")
                break
        else:
            month, day, year = formate.split()
            if  ',' in day:
                day = day.replace(',', '')
                if (int(day) <= 31):
                    print(f"{int(year)}-{(months.index(month) + 1):02}-{int(day):02}")
                    break
    except ValueError:
        pass

get = []
printed_get = set()
while True:
    try:
        get.append(input().upper())
    except EOFError:
        for data in sorted(get):
            if data not in printed_get:
                print(f"{get.count(data)} {data}")
                printed_get.add(data)
        break

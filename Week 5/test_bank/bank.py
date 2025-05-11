def main():
    ask = input('Greeting: ')
    print(f"${value(ask)}")

def value(greeting):
    andd  = greeting.strip().lower()
    if andd.startswith("hello"):
        return 0
    elif andd.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

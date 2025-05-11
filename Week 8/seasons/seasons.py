from datetime import date
from inflect import engine
import sys

def main():
    try:
        time = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        print("Invalid Input")
        sys.exit(1)
    diff = date.today() - time
    Mins = diff.days * 24 * 60
    print(convert_inflect(Mins))

def convert_inflect(Mins):
    p = engine()
    p = p.number_to_words(Mins, andword="")
    return f"{p.capitalize()} minutes"

if __name__ == "__main__":
    main()

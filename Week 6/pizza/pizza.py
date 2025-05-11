import sys
import csv
from tabulate import tabulate
def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many commend-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv") :
        print("Not a CSV file")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            file = csv.reader(file)
            data = list(file)
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()

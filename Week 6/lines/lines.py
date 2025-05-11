import sys
def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many commend-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".py") :
        print("Not a python file")
        sys.exit(1)
    try:
        with open(sys.argv[1],"r") as file:
            file = file.readlines()
            lineOfcode = [line for line in file if line.strip() and not line.strip().startswith("#")]

            print(len(lineOfcode))
    except FileNotFoundError:
        print("File dose not exist")
        sys.exit(1)

main()





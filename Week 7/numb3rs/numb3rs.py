import re
import sys

def main():
    try:
        ip = input("IPv4 Address: ")
    except EOFError:
        sys.exit(0)
    print(validate(ip))

def validate(ip):
    pattern = r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$"
    return bool(re.fullmatch(pattern, ip))

if __name__ == "__main__":
    main()

def main():
    # Get input from user
    msg = input("Input: ")
    new = shorten(msg)
    print(new)
def shorten(msg):
     return "".join(char for char in msg if char.lower() not in "aeiou")
if __name__ == "__main__":
    main()

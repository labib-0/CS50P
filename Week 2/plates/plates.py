def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (2 <= len(s) <= 6) and s[0].isalpha() and s[1].isalpha() and s.isalnum():
        num_started = False  # Flag to track if a number has started
        for i in range(2, len(s)):
            if s[i].isdigit():
                if s[i] == '0' and num_started is False:  # First digit is not zero
                    return False
                num_started = True  # A number has started
            elif num_started == True:  #Its invalid if a letter appears after a number
                return False
        return True


main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if not (2 <= len(s) <= 6):
            return False
    if s[0].isalpha() and s[1].isalpha() and s.isalnum():
        num_started = False
        for i in range(2, len(s)):
            if s[i].isdigit():
                if s[i] == '0' and num_started is False:
                    return False
                num_started = True
            elif num_started == True:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()

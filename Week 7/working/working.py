import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(?P<hour1>0?[1-9]|1[0-2])(:(?P<mint1>([0-5][\d])))? (?P<medi1>AM|PM) to (?P<hour2>0?[1-9]|1[0-2])(:(?P<mint2>([0-5][\d])))? (?P<medi2>AM|PM)", s)
    if match:
        nhour1 = int(match.group('hour1'))
        nhour2 = int(match.group('hour2'))
        mint1 = match.group('mint1') or '00'
        mint2 = match.group('mint2') or '00'
        if match.group('medi1') == "PM":
            if nhour1 != 12:
                nhour1 += 12
        else:
            if nhour1 == 12:
                nhour1 = 0
        if match.group('medi2') == "PM":
            if nhour2 != 12:
                nhour2 += 12
        else:
            if nhour2 == 12:
                nhour2 = 0
    else:
        raise ValueError
    return f"{nhour1:02}:{mint1} to {nhour2:02}:{mint2}"


if __name__ == "__main__":
    main()

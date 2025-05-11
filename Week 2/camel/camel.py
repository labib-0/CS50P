def main():
    # Get camelCase input from user
    cc = input("camelCase: ")
    pc = convert(cc)
    print(f"snake_case: {pc}")


def convert(n):
    p_c = ""
    for char in n:
        if char.islower():
            p_c += char
        else:
            p_c += '_' + char.lower()
    return p_c


main()

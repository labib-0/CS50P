import inflect
p = inflect.engine()

name = []
while True:
    try:
        name.append(input("Name: "))
    except EOFError:
        break
print(f"\nAdieu, adieu, to {p.join(name)}")

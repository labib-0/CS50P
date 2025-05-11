# Initialize and get input
need = 50
while need > 0:
    insert = int(input(f"Amount Due: {need}\nInsert Coin: "))
    if insert in (5, 10, 25):
        need -= insert
print(f"Change Owed: {-need}")

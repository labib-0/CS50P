import random

def main():
    score = 0
    level = get_level()

    for _ in range(10):  # Loop for 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        n = 0

        while n < 3:  # Allow 3 attempts
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == x + y:
                    score += 1
                    break  # Exit retry loop
                else:
                    print("EEE")
            except ValueError:
                print("EEE")  # Invalid input also counts as an error

            n += 1  # Increment attempts

            if n == 3:
                print(f"{x} + {y} = {x + y}")  # Show correct answer

    print("Score:", score)  # Display final score

def get_level():
    """Prompt user for level (1, 2, or 3)"""
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass  # Ignore invalid input and prompt again

def generate_integer(n):
    if n == 1:
        return random.randint(0,9)
    else:
        return random.randint(10**(n-1), 10**n - 1)

if __name__ == "__main__":
    main()

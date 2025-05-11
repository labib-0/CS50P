
# Take input from the user
ask = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
# Check if the input is 42, forty two, forty-two are or not
if ask == "42":
    print("Yes")
elif ask == "forty-two":
    print("Yes")
elif ask == "forty two":
    print("Yes")
else:
    print("No")

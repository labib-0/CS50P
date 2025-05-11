# Get input from user
exp = input('Expression: ').strip().split()
if exp[1] == '+':
    print(float(int(exp[0]) + int(exp[2])))
elif exp[1] == '-':
    print(float(int(exp[0]) - int(exp[2])))
elif exp[1] == '*':
    print(float(int(exp[0]) * int(exp[2])))
elif exp[1] == '/':
    print(int(exp[0]) / int(exp[2]))

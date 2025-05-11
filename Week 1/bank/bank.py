# Ask the user for greetings
ask = input('Greeting: ').strip().lower().split()
f_word = ask[0]
if f_word[0:5] == 'hello':
    print('$0')
elif f_word[0] == 'h':
    print('$20')
else:
    print('$100')

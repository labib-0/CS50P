import random
import sys
from pyfiglet import Figlet

fonts = Figlet()
list = fonts.getFonts()

if len(sys.argv) == 1 :
    msg = input("Input: ")
    fonts.setFont(font=random.choice(list))
    print(fonts.renderText(msg))

elif len(sys.argv) == 3 and sys.argv[2] in list and sys.argv[1] in ('-f','--font'):
    msg = input("Input: ")
    fonts.setFont(font=sys.argv[2])
    print(fonts.renderText(msg))
else:
    sys.exit(1)


import sys
import os
from PIL import Image, ImageOps
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith((".jpeg", ".png", "jpg")):
        sys.exit("Invalid input")
    if not sys.argv[2].endswith((".jpeg", ".png", "jpg")):
        sys.exit("Invalid output")
    if not os.path.splitext(sys.argv[1])[1] == os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")
    if not os.path.exists(sys.argv[1]):
        sys.exit("Input does not exist")

    muppet = Image.open(sys.argv[1])
    shirtFile = Image.open("shirt.png")

    size = shirtFile.size
    muppet = ImageOps.fit(muppet,size)
    muppet.paste(shirtFile, shirtFile)
    muppet.save(sys.argv[2])

if __name__ == "__main__":
    main()

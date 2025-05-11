def main():
    # Get user input
    msg = input("What's your massege? ")

    # Call convert function
    convert(msg)

def convert(msg):
    # Replace :) to happy emoji
    msg = msg.replace(':)', '🙂')

    # Replace :( to sad emoji
    msg = msg.replace(':(', '🙁')

    # Print string
    print(msg)

main()

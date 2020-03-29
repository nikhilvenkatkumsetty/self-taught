import cubed
def num():
    while True:
        x=input("Enter the number: (or q to quit)")
        if x == 'q':
            break
        try:
            x=int(x)
            print(cubed.cube(x))
            break
        except ValueError:
            print("Please give a valid input!")
num()
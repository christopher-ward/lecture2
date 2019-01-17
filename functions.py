def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i))) #this syntax is more common in older python. Good to know if encounter code older than 3.6. This is instead of using just the letter (f"")in a previous example.

if __name__ == "__main__":
    main()
    #this if statement and the "def main():" line were added after creating modules.py and see that the entire functions.py program was run before the square of 10 was computed. This addition and tweak of code allows for this function file to work properly when called alone, but also for modules.py to be able to call just the function square().

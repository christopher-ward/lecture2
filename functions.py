def square(x):
    return x * x

for i in range(10):
    print("{} squared is {}".format(i, square(i)))
    #this syntax is more common in older python. Good to know if encounter code older than 3.6. This is instead of using just the letter (f"")in a previous example.

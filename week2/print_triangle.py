def triangle(height):

    for x in range(0, height, 2):
        space = " " * ((height - x)/2)
        print space + "*" * (x + 1)

user_input = int(raw_input("What's the height of your triangle?"))
triangle (user_input)

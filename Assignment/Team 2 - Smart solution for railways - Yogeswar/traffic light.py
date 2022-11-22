x = input("Enter value: ")
stop_light = int(x)
while True:
    if stop_light >= 1 and stop_light < 10:
        print('Green light')
        stop_light += 1
    elif stop_light < 20:
        print('Yellow light')
        stop_light += 1
    elif stop_light < 30:
        print("Red light")
        stop_light += 1
    else:
        stop_light = 0
    break
while True:
    x = input("Enter value: ")
    stop_light = int(x)
    if stop_light == 30:
        break
    elif stop_light >= 1 and stop_light < 10:
        print('Green light')
        stop_light += 1
    elif stop_light < 20:
        print('Yellow light')
        stop_light += 1
    elif stop_light < 30:
        print("Red light")
        stop_light += 1
    else:
        stop_light = 0
        while True:
try:
        x = input("Enter value: ")
        stop_light = int(x)
    except ValueError:
        print("Try Again")
    else:
        break

while stop_light <= 30:
    if stop_light >= 1 and stop_light < 10:
        print('Green light')
    elif stop_light < 20:
        print('Yellow light')
    elif stop_light < 30:
        print("Red light")
    stop_light += 1
    Enter value: asdf
Try Again
Enter value: 27
Red light
Red light
Red light
# Breaks and closes the code.

Enter value: 5
Green light
Green light
Green light
Green light
Green light
Yellow light
Yellow light
Yellow light
Yellow light
Yellow light
Yellow light
Yellow light
Yellow light
Yellow light
Yellow light
Red light
Red light
Red light
Red light
Red light
Red light
Red light
Red light
Red light
Red light
# Breaks and closes the code.
else:
    stop_light = 0
    while True:
    try:
        x = input("Enter value: ")
        stop_light = int(x)
    except ValueError:
        print("Try Again")
    else:
        while stop_light < 30:
            if stop_light >= 1 and stop_light < 10:
                print('Green light')
            elif stop_light < 20:
                print('Yellow light')
            elif stop_light < 30:
                print("Red light")
            stop_light += 1
        if stop_light > 30:
            break

Output:

Enter value: asdf
Try Again
Enter value: 27
Red light
Red light
Red light
Enter value: 31
# Breaks and closes the code.
elif stop_light < 30:
    print("Red light")
    stop_light += 1

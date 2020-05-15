while True:
    try:
        x=int(input("Enter a number"))
        y=int(input("Enter an another number"))
        avg = (x+y)/2
        print(avg)
    except:
        print("Not an integer")
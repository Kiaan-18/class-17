for i in range(15):
    if i%20==0:
        print("Twist")
    elif i%15==0:
        pass
    elif i%10==0:
        print("buzz")
    elif i%5==0:
        print("fizz")
    else:
        print(i)
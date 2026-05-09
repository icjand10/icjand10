def prime(x):
    d = 2
    z = 0
    if isinstance(x, float):
        print("Please put in an integer, not a decimal.")
        return


    for i in range(x - 2):
        if x % d == 0:
            z = z + 1
        else:
            d = d + 1
    if z > 1:
        print("Your number is not a prime.")

    elif x <= 1:
        print("Your number is not a prime.")
    else:
        print("Your number is a prime!")
print(prime(1.5))

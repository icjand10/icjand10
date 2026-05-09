def palindrome(x):

    x = x.replace(" ", "")
    x = list(x)
    regx = x

    left = 0
    right = len(x) - 1

    while left < right:
        x[left], x[right] = x[right], x[left]
        left += 1
        right -= 1
    return x == regx

print(palindrome("7         7"))
print(palindrome("race car              "))
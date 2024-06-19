def getsum(n):
    sum = 0
    for digits in str(n):
        sum += int(digits)
    return sum

n = input("Enter the number:")
print(getsum(n))

x = int(input('Enter a number:'))
f = 1
if x < 0:
    print("Factorial is not defined for negative numbers")
elif x == 0 or x == 1:
    print('Factorial is 1')
else:
    while (x>0):
        f = f * (x)
        x = x-1
    print('the factorial is', f)

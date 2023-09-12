num1 = int(input())
num2 = int(input())

for x in range(1, 1001):
    for y in range (1, 1001):
        if x + y == num1 and x * y == num2:
            print (x, y)
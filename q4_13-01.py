import math

num = int(input("Enter the number: "))
a = int(input("Enter starting point: "))
b = int(input("Enter ending point: "))

x = int(math.log(num, 2.0) + 1)

for i in range (a,b):
    num = (num ^ (1 << i))

print(num)

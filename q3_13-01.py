num = int((input("enter number: ")))
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)
# print(str(num)[::-1])


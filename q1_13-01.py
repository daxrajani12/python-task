# num = input("enter number:")

# l = len(num)

# if (l == 0):
#     print("empty string")

# if (l > 4):
#     print("Length is more than 4 is not supported")

# single_digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] 
# tens_power = ["hundred", "thousand"]

# print(num, ":", end="")

# if (l == 1):
#     print(single_digit[ord(num[0]) - 48])

# x = 0
# while(x < len (num)):
#     if (l >=3):
#         if (ord(num[x]) - 48 != 0):
#             print(single_digit[ord(num[0]) - 48], end= " ")
#             print(tens_power[l-3], end = " ")
#         l -= 1
#     else:
#         if (ord(num[x]) - 48 ==1):
#             sum = (ord(num[x]) - 48 + ord(num[x+1]) - 48)
#             print(two_digits[sum])
#             break
            
#         elif (ord(num[x]) - 48 == 2 and ord(num[x+1]) - 48 == 0):
#             print("twenty")
#             break

#         else:
#             i = ord(num[x]) - 48
#             if (i > 0):
#                 print(tens_multiple[i], end=" ")
#             else:
#                 print("",end="")
#             x+=1
#             if(ord(num[x]) - 48 != 0):
#                 print(single_digit[ord(num[0]) - 48])

#     x += 1

number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n=int(input("Enter a number "))
if n>99999:
    print("Cant solve for more than 5 digits")
else:
    d=[0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
    num=""
    if d[4]!=0:
        if(d[4]==1):
            num+=tens[d[3]]+ " Thousand "
        else:
            num+=nty[d[4]]+" "+number[d[3]]+  " Thousand "
    else:
        if d[3]!=0:
            num+=number[d[3]]+ " Thousand "
    if d[2]!=0:
        num+=number[d[2]]+" Hundred "
    if d[1] != 0:
        if (d[1] == 1):
            num += tens[d[0]]
        else:
            num += nty[d[1]] + " " + number[d[0]]
    else:
        if d[0] != 0:
            num += number[d[0]]
    print(num)
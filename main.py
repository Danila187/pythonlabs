a = True
b = False

print(a and b)
print((a and b) or b)
print((a and b) or not (a and b))
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not (a or b))
print( 1 << 2)
print((1 and 0) or (1 >> 1))
print((1 and 0) or (1 >> 0))
print((5 and 7) ^ (7 or 2))


num1 = 4
num2 = 22
if (num1<num2):
    print(num1)
else:
    print(num2)



num3 = 41
num4 = 124
num5 = 456
if (num3>num4) and (num3>num5):
    print(num3)
elif (num4>num3) and (num4>num5):
    print(num4)
else:
    print(num5)


base = [3,5,58]
print(len(base))


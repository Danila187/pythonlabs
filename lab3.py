A = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
print(sum(A))

B = [1, 2, 0, 11, 13, 0]
print(B.count(0))

n = 9
for i in range(n):
    print("".join(map(str,range(1,i+2))))

n = 9

for i in range(1, n + 1):
    left = ''.join(map(str, range(1, i)))
    spaces = ' ' * (n - i)
    print(f'{spaces}{left}{i}{left[::-1]}')

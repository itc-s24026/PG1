a,b = 0, 1
while b < 20:
    print(b)
    a,b = b, a +b
    
a = 0

while a < 100:
    if a > 10:
        break
    a += 2
print(a)
print('在while里的print')

while a < 100:
    if a > 10:
        break
    a += 2
    print(a)
print('在if里的print')

while a < 100:
    if a > 10:
        break
        print(a)
    a += 2
print('在break下方的print')



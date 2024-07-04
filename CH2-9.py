my_str = 'This is a pen'
print('pen' in my_str)

my_list = [0,2,4,6,8,10]
print(3 not in my_list)

x = None
print(x is None)
print(x is not None)

x = True
y = False
z = None

print(x and z is None)
print(not x or not y)
print(x and not y and z is None)

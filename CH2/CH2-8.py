my_list = [0,1,2,3,4,5,6,7,8]
print(my_list)

print(my_list[2:7])
print(my_list[2:7:2])
print(my_list[6:1:-1])
print(my_list[:])
print(my_list[::-1])

my_list = [0,1,2,3,4,5,6,7,8]
my_list[0] = -1
print(my_list)

my_list[2:4] = [102,103]
print(my_list)

my_list[2:4] = [101,102,103,104]
print(my_list)

my_list[2:2] = [101,102]
print(my_list)

my_list[2:6] = [101,102]
print(my_list)

my_list[2:6] = []
print(my_list)

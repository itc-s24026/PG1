# 追加元素
my_list = [2,4,8,16]
my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)

# 追加列表
my_list.extend([12,15])
print(my_list)

# 进行升序
my_list.sort()
print(my_list)

# 进行倒序并降序
my_list.sort(reverse=True)
print(my_list)

# 只进行倒序
my_list.reverse()
print(my_list)

# 为了不使原有的数据被覆盖，可以赋予新值进行改变。
# 注意：这里是sorted,并不是sort函数。
my_list = [2,4,8,16,3,6,9,12]
new_list = sorted(my_list)
rev_list = sorted(my_list,reverse=True)

print(my_list)
print(new_list)
print(rev_list)

# 这个是单纯的将元素追加在列表的末尾
you_list = []
you_list.append('apple')
you_list.append('orange')
you_list.append('grape')
you_list.append('banana')

print(you_list)

# 这个是单纯的升序
you_list.sort()
print(you_list)

# 这个逆向数并降序
you_list.sort(reverse=True)
print(you_list)

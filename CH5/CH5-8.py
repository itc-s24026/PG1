prefectures = ['Hokkaido','Hokkaido','Tokyo','kanagawa']
cities = ['Sapporo','Hakodate','Minato','Yokohama']
populations = [100,200,300,400]
population_dict={(state,city):population for state,city,population in zip(prefectures,cities,populations)}
print(population_dict)

print({0:{0:1,0:2,0:3},1:{0:0,1:1,2:2},2:{0:0,1:2,2:4}})
print('用for文生成以上的答案')
multiplicated_xy_dict = {}
I = 3
J = 3
for i in range(I):
    multiplicated_xy_dict[i] = {}
    for j in range(J):
        multiplicated_xy_dict[i][j] = i*j
        print('用J来循环',multiplicated_xy_dict)
print(multiplicated_xy_dict)

print('用内包标记生成以上答案')
I = 3
J = 3
multiplicated_xy_dict = {i:{j:(i*j) for j in range(J)} for i in range(I)}
print(multiplicated_xy_dict)










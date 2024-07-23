prefecture_of_japan = {1:'Hokkaido',2:'Aomori',3:'Iwate'}
print(prefecture_of_japan)

print(prefecture_of_japan.get(0))
print(prefecture_of_japan.get(1))
print(prefecture_of_japan.get(0,'Not Found'))

prefecture_of_japan[4] = 'miyagi'
print(prefecture_of_japan)

#prefecture_of_japan.clear()
#print(prefecture_of_japan)

for x in prefecture_of_japan:
    print(x)

for x in prefecture_of_japan.keys():
    print(x)

for x in prefecture_of_japan.values():
    print(x)

print('以下是问题的演示答案')

data = [
    ['0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
    ['0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'],
    ['0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'],
    ['0004', 'Male', 'Suzuki', 'Ichirou', 35, 'Hokkaido']
]
print(data)

print('生成词典')

member_information= {}

for record in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info 

print('number','information',sep='/t')
for key,info in member_information.items():
    print(key,info)

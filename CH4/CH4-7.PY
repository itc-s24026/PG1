def make_circle_area_func(pi=3.14):
    '''制作计算圆面积的函数'''

    def circle_area(redius):
        '''计算圆的面积'''

        return redius*redius*pi

    return circle_area

#p的初始值是3.14
circle_area_default = make_circle_area_func()

#p的初始值是3.1415926535
circle_area_precise = make_circle_area_func(pi=3.1415926)

print(circle_area_default(2))
print(circle_area_precise(2))

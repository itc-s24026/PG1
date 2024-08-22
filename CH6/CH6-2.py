class Sample:
    def __init__(self):
        self.a = 1
        self._b = 1
        self.__c = 1
        self.__d = 1
        self.__e__ = 1

    def show_attribute(self):
        a = self.a
        b = self._b
        c = self.__c
        d = self.__d
        e = self.__e__
        print("a:{},b:{},c:{},d:{},e:{}".format(a,b,c,d,e))

s = Sample()
s.show_attribute()

print(s.a)


class Cylinder:
    '''圆柱'''
    pi = 3.14

    def __init__(self,radius=1,height=1):
        '''将圆柱体附上特征的属性'''
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        '''进行底面积的计算'''
        pi =Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        '''侧边面积的计算'''
        pi = Cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        '''表面积计算'''
        c = self.calc_base_area()
        s = self.calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        '''计算体积'''
        c = self.calc_base_area()
        h = self.height
        return c * h

    def show_results(self):
        '''展示属性和计算结果'''
        r = self.radius
        h = self.height
        S = self.calc_surface_area()
        V = self.calc_volume()
        print('半径:{},高度:{},表面积:{},体积:{}'.format(r,h,S,V))

c1 = Cylinder()
c1.show_results()
c2 = Cylinder(1.,3.)
c2.show_results()
c3 = Cylinder(2.,1.)
c3.show_results()
c4 = Cylinder(2.,3.)
c4.show_results()
















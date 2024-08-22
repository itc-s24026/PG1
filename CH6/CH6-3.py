class Nigiri:
    category = "饭团"
    top = "寿司材料"
    base = "握"

    def show_attributes(self):
        print('top:{},base:{},category:{}'.format(self.top, self.base, self.category))

n1 = Nigiri()
print(n1.show_attributes())
'''这里是作为父类的所有元素，以下开始用maguro来继承。'''

class Maguro(Nigiri):
    pass

m1 = Maguro()
print(m1.show_attributes())
'''继承了父类里面attributes的所有元素'''

'''接下来试着覆盖下之前父类里面的变量'''
class Maguro(Nigiri):
    top = "金枪鱼"

m3 = Maguro()
print(m3.show_attributes())

'''再追加类的变量'''
class Maguro(Nigiri):
    top = "金枪鱼"
    price = 100

m4 = Maguro()
print(m4.show_attributes())
'''这里显示的依旧是父类里面的元素'''

class Maguro(Nigiri):
    top = "金枪鱼"
    price = 100
    
    def show_attributes(self):
        super().show_attributes()
        print("price:{}元".format(self.price))

m5 = Maguro()
print(m5.show_attributes())
'''这里使用了可以调出父类的函数:super'''

'''显示一盘寿司的价格，一盘里面是两个饭团'''
class Maguro(Nigiri):
    top = "金枪鱼"
    price = 100

    def show_attributes(self):
        super().show_attributes()

    def show_one_dish_price(self,num_nigiri=2):
        result = self.price * num_nigiri
        print("一盘（{}个）的价格:{}元".format(num_nigiri,result))

m6 = Maguro()
print(m6.show_attributes())
print(m6.show_one_dish_price())
        
'''追加实例的变量，在继承父类的子类里面，可以选择金枪鱼饭团放芥末还是不放，默认不放芥末'''

class NigiriNew(Nigiri):

    def __init__(self,wasabi="去掉芥末"):
        self.wasabi = wasabi 

    def show_attributes(self):
        super().show_attributes()
        print("wasabi:{}".format(self.wasabi))

class Maguro(NigiriNew):
    top = "金枪鱼"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("price:{}".format(self.price))

m7 = Maguro("放芥末")
print(m7.show_attributes())







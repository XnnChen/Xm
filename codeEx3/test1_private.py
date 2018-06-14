class Women:

    def __init__(self, name):

        self.name = name
       
        self.__age = 18

    def __secret(self):
        print("我的年龄是 %d" % self.__age)


xiaofang = Women("小芳")

class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print(f"{self.name} 来了")

    def __del__(self):

        print(f"{self.name} 我去了")

# tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom

print("-" * 50)

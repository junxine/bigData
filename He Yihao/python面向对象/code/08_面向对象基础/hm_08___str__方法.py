class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print(f"{self.name} 来了")

    def __del__(self):

        print(f"{self.name} 我去了")

    def __str__(self):

        # 必须返回一个字符串
        return f"我是小猫[{self.name}]"

# tom 是一个全局变量
tom = Cat("Tom")
print(tom)

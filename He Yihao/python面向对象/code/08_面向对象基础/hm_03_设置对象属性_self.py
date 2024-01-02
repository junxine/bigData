class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print(f"{self.name} 爱吃鱼")

    def drink(self):
        print(f"{self.name} 要喝水")


# 创建猫对象
tom = Cat()

# 可以使用　.属性名　利用赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)
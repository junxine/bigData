# 1. 打开文件
with open("README") as file:
    # 2. 读取文件内容
    text = file.read()
    print(text)
    print(len(text))

    print("-" * 50)

    text = file.read()
    print(text)
    print(len(text))

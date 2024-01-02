# 1. 打开
with open("README") as file_read:
    file_write = open("REAMDE[复件]", "w")

    # 2. 读、写
    text = file_read.read()
    file_write.write(text)

file_write.close()

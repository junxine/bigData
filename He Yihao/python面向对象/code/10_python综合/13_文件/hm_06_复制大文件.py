# 1. 打开
with open("README") as file_read:
    file_write = open("REAMDE[复件]", "w")

    # 2. 读、写
    while True:
        if text := file_read.readline():
            file_write.write(text)

        else:
            break

file_write.close()

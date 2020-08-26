import re
# 1、打开文件
file = open('readme')
# 2、读取文件内容
while True:
    text = file.readline()
    if not text:
        break
    print(text)
# 3、关闭文件
file.close()
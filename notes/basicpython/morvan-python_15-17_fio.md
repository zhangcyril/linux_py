# 文件读写

### 写文件

text = 'xxxxxxx'

filevar_name = open('file_name.txt...','w/r')

filevar_name(text/'xxxxxxx')

filevar_name.close()



### 读文件 

filevar = open('file_name','r')

1. contentvar = filevar.read()

> 原格式

2. contentvar = filevar.readline()

> 读第一行，下一句readline读第二行

3. contentvar = filevar.readlines()

> contentvar 用 list 形式存储每一行，每个元素有'\n'符号

print(content)




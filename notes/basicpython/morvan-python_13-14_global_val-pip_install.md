# 全局变量&局部变量

> global var&local var



``` python
a = None

def func():

    global a

    a = 20

    return a+100

print(a)

print(func())

print(a)

```



> > out : None 120 20
>
> 函数内更改global加前缀



# 外部模块安装

sudo pip install numpy / sudo pip uninstall numpy

sudo pip install -U numpy




# try [错误处理]

``` python
try:
    file = open('eee','r')
except Exception as e:
    print(e)   
```

> 输出ERROR：...line...xxxx,(输出到e并打印)

```python
try:
    file = open('eee','r+w')
except Exception as e:
    print('thers is no file named as eee')
    response = input('do you want to create a new file')
    if response == 'y':
        file = open('eee','w')
    else:
        pass
else:
    file.write('ssss')
file.close()
```



# zip,lamda,map



### zip

``` python
a = [1,2,3]
b = [4,5,6]
```

> e.g.

```python
zip(a,b)
#out: zip object at 0x......
list(zip(a,b))
#out: [(1,4),(2,5),(3,6)]
for i,j in zip(a,b)
    print(i/2,j*2)
#out: 0.5 8
#	  1.0 10
#	  1.5 12
```

> e.g. 2

``` python
list(zip(a,a,b))
#out: [(1,1,4),(2,2,5),(3,3,6)]
```



### lambda

> 和def类似，用于定义比较简单的方程

``` python
#eg. 1
def fun1(x,y):
    return(x+y)

#eg. 2 
fun2 = lambda x,y:x+y

fun1(2,3)
#out: 5

fun2(2,3)
#out: 5
```



### map

> 参数输入要放在列表里，直接返回为object

``` python
map(fun1,[1],[2])
#out: map object at 0x......

list(map(fun1,[1],[2]))
#out: [3]

list(map(fun1,[1,3],[2,5]))
#out: [3.8]
```



# copy & deepcopy

> copy在python中是一个模块，使用前需import
>
> id(xxx) 索引

``` python
import copy
a = [1,2,3] 
b = a

print(id(a)==id(b))
#out: true
#a change -> b change 
#a,b指向同一个地址

c = copy.copy(a)
#a,b两块地址
#但有list(二层列表)时会共用一块空间

d = copy.deepcopy(a)
#a.b完全独立
```

> copy.copy: 如果copy对象里有list,list元素是同一个地址,一个改变另一个也改变,但其他元素不变
>
> copy.deepcopy: 独立
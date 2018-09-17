# tuple list [元组列表]

> tuple一旦初始化就不能修改
>
> 可变tuple : tuple 中的一个元素是 list

a_tuple = (1,2,3,4,5)

another_tuple = 1,2,3,4,5



a_list = [11,22,33,44,55]



```python
for index in range(len(a_list)):
    print('index=',index,'number in list = '
          ,a_list[index])
    
# out : index=0 number in list=11
#		index=1 number in list=22
#		...
```

> range 从 0 开始
>
> range(5) ------ 0,1,2,3,4



# list

> 1. list顺序从0开始
> 2. 最后一个值可用list(-1)取到,倒数第二个list(-2)....
> 3. list元素也可以是另一个list
> 4. list里面的元素的数据类型可以不同

* 长度 : 用`len()`函数可以获得list元素的个数

* 追加 : list.append(1,0) ---- 在位置1追加0

* 插入 : 把元素插入到指定的位置，比如索引号为`1`的位置

  ​	   list.insert(1,'xxx')

* 移除 : list.remove(x) ---- 移除list中出现的第一个x元素

* 删除list末尾的元素 : 用`pop()`方法

* 删除指定位置的元素 : 用`pop(i)`方法，其中`i`是索引位置

* 指定元素的第一个索引 : list.index(x)

* 指定元素出现的次数 : list.count(x)

* 排序 : 

  * list.sort()   默认从小到大排序
  * list.sort(reverse=True) 从大到小排序

* 多个元素 : 

  ``` python
  a = [1,2,3,4,5,6,7]

  print(a[0:3]) #print(a[:3])
  #out : [1,2,3]  //a[x:y] : 从x开始，输出y-x个元素
  print(a[-3:])
  #out : [5,6,7]
  ```




# 多维列表

> 常用附加模块 : numpy pandas
>
> >  import numpy

```python
list = [1,2,3,4,5]

multi_dim_list = [[1,2,3],
                  [2,3,4]
                  [3,4,5]]
```



# dictionary [字典]

> dict = {key:value,......}
>
> ***字典是没有顺序的容器* **
>
> 字典可嵌套

dict = {'apple':1,'pear':2,'orange':3}

dict2 = {1:'a','c':'b'}

* 删除字典元素 : del d[key]

* 添加字典元素 : dict[key] = value

  ​
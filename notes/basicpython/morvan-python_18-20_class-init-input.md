# class

> 类定义首字母大写

``` python
class Calculator:
    name = 'Good calculator'
    price = 17
    def add(self,x,y):
        print(self.name)

```



​	

```python
class Calculator:
    name = 'Good calculator'
    price = 17
    #调用类内定义参数用self.xxx
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

```

> self参数
>
> - 在Python中，类的方法与普通的函数有一个特别的区别——它们必须有一个额外的第一个参数名称，但是在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self。 
> - 虽然你可以给这个参数任何名称，但是强烈建议你使用self这个名称——其他名称都是不赞成你使用的。 
> - 使用一个标准的名称有很多优点——你的程序读者可以迅速识别它，如果使用self的话，还有些IDE（集成开发环境）也可以帮助你。 
> - 给C++/Java/C#程序员的注释Python中的self等价于C++中的self指针和Java、C#中的this参考。



# init

```python
class Calculator:
    name = 'Good calculator'
    price = 17
    
    def __init__(self,name,price,xxx,.....)
        self.name = name
        self.price = price
        sefl.xxx = xxxx
        .....
        
    #调用类内定义参数用self.xxx
    def add(self,x,y):
      ....

```

> use : c = Calculator('bad calculatro',18,xxx,...)
>
> > out : c.name = 'bad calcu...'
> >
> > 固有属性会被替换
>
> c = Calculator(xxx)
>
> > 定义参数不足时会报错



# input

* **input return a string!!**
* **use int() when want a num**
* if 判定可以用 x=='1' / x==str(2)


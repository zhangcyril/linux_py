# Python Threading



### create & start threading

> * import threading
>
> * threading.active_count() [当前线程数量]
>
> * threading.enumerate() [列举线程]
>
> * threading.current_thread() [查看运行此语句的为哪个线程]
>
> * [added_thread] = threading.Thread(target=[thread_job],name=xxx) 
>
>   [添加线程]
>
> * [added_thread].strat() [开始thread]
>
> * use:
>
>       t1 = threading.Thread(target=job1)
>       t2 = threading.Thread(target=job2)
>       t1.start()
>       t2.start()
>       t1.join()
>       t2.join()	





 ``` python
import threading

def thread_job():
    print("This is an added Thread,number is %s" % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == '__main__':
    main()
 ```



### join

> 使用join后，main等待所有thread结束

```python
import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10)
        time.sleep(0.1)
    print('T1 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job,name="T1")
    added_thread.start()
    added_thread.join()
    print('all done\n')

if __name__ == '__main__':
    main()
```



### Queue

> from queue import Queue
>
> 多线程涉及功能没有返回值，因此运算结果要放在queue中，在主线程中从queue取值

``` python
import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l))
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4)
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4)
        results.append(q.get())
    print(results)
    
if __name__ == '__main__':
    multithreading()
```

> xxx = threading.Thread(target=[函数名称不加括号],args=(参数,queue))



### 效率

GIL

大数据处理上多线程效率不明显[单核]   ----> multiprocessing效率提高



### lock

> lock = Threading.Lock()
>
> use: lock.acquire()
>
> ​	....
>
> ​	....
>
> ​	lock.release()

``` python
import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1',A)
    lock.release()
        
def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1=
        print('job2',A)
    lock.release()
        
if __name__=='__main__':
    lock = Threading.Lock()
    
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
```




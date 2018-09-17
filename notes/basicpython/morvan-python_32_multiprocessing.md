# Multiprocessing

> 创建、queue类似multithread 



### 进程池 pool

``` python
import multiprocessing as mp

def job(x)
    return x*x

def multicore():
    pool = mp.Pool()#(process=3)//会只用三个核 默认全部
    res = pool.map(job,range(10))
    print(res)
    
if __name__=='__main__'
    multicore()
```



### 共享内存 shared memory

``` python
import multiprocessing as mp

value = mp.Value('d',1)#i,d,b,B,f.....
array = mp.Array('i',[1,2,3])#只能是一维的


```



### Lock 

``` python
import multiprocessing as mp
import time

def job(v,num):
    l.acquire()
    for _ in range(10)
        time.sleep(0.1)
        v.value += num
        print(v,value)
    l.release()
    
def multicore()
    l = mp.Lock()
    v = mp.Value('i',0)
    p1 = mp.Process(target=job,args=(v,1))
    p2 = mp.Process(target=job,args=(v,3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```




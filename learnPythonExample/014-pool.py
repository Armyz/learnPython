#-*- coding:utf-8 -*-

from multiprocessing import Pool
import os
import time
import random

def worker(msg):
    t_start = time.time()
    print("%d号子进程开始执行,PID为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_end = time.time()
    print("%d号执行完毕,时间为%.4f"%(msg,t_end-t_start))


if __name__ == "__main__":
    pool_apply_async = Pool(3)
    for i in range(5):
        #使用apply_async为非阻塞形式执行,一次可执行进程池的三个任务
        pool_apply_async.apply_async(worker, (i,))
    
    print("---apply_async开始执行---")
    pool_apply_async.close()
    #主机进程阻塞,等待子进程执行完毕,必须放在close之后
    pool_apply_async.join()  
    print("---apply_async执行结束---")

    pool_apply = Pool(3)
    for i in range(5):
        #使用apply_为阻塞形式执行,一次只能执行一个任务,
        #上一个任务执行完毕后才能执行下一个任务
        pool_apply.apply(worker, (i,))
    
    print("---apply开始执行---")
    #pool_apply.close()  
    #pool_apply.join()
    print("---apply执行结束---")


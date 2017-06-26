#coding=utf-8

from multiprocessing import Process
import time
import os

#重写Process类
class process_class(Process):
    def __init__(self,interval):
        #让父类完成初始化工作,在此基础上再进行初始化的添加
        Process.__init__(self)
        self.interval=  interval

    def run(self):
        print("子进程(%s)开始执行,父进程(%s)"%(os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print("%s 执行结束,耗时%0.5f秒"%(os.getpid(),t_end - t_start))

if __name__=="__main__":
    print("当前进程%s"%(os.getpid()))
    
    t_start = time.time()
    p1 = process_class(2)
    p1.start()
    p1.join()
    t_end = time.time()
    
    print("%s 执行结束,耗时%0.5f秒"%(os.getpid(),t_end - t_start))

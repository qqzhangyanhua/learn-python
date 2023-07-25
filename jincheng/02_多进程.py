
import time
from multiprocessing import Process
def run():
    for i in range(3):
        print('run',i)
        time.sleep(1)
    # 当前代码阻滞1秒
def run2():
    for i in range(3):
        print('run2',i)
        time.sleep(1)
    # 当前代码阻滞1秒

if __name__ == '__main__':
    t1 = time.time()
    p = Process(target=run)  # 创建进程对象
    p2 = Process(target=run2)
    p.start() # 启动进程
    p2.start()
    # p.join() # 阻塞进程
    # p2.join()
    print('hello')
    print(time.time()-t1)
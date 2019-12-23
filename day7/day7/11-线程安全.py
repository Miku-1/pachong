import threading
#当次数较多时，出现问题，如何解决
#抢下   锁住     释放
#这种解决方式是牺牲线程的性能为前提的  GIL
count = 100
#创建锁
lock = threading.Lock()
def demo(num):
    global count
    for x in range(0,1000000):
        lock.acquire()
        count += num
        count -= num
        lock.release()
    print('count的值为%s'%count)

def main():
    t1 = threading.Thread(target=demo,args=(3,))
    t2 = threading.Thread(target=demo,args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
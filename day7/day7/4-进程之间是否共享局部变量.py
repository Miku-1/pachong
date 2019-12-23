from multiprocessing import Process
import time

def demo(name):
    count = 100
    if name == 'change':
        count += 50
        print('p1读取的值为%s'%count)
    else:
        time.sleep(2)
        #读取count的值
        print('p2读取的值为%s'%count)
def main():
    p1 = Process(target=demo,args=('change',))
    p2 = Process(target=demo,args=('read',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主线程-子线程全部运行结束")
if __name__ == '__main__':
    main()
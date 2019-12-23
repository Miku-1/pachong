import threading
import time

def sing():
    for x in range(1,6):
        print('sing线程的名字是%s'%threading.current_thread().name)
        print('我最喜欢唱山歌')
        time.sleep(1)

def dance(name):
    for x in range(1,6):
        print('dance线程的名字是%s' % threading.current_thread().name)
        print('%s最喜欢跳钢管舞'%name)
        time.sleep(1)

def main():
    print('main线程名字是%s' % threading.current_thread().name)
    name = '贾玲'
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance,args=(name,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
import time,threading

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
    t1 = threading.Thread(target=demo,args=('change',))
    t2 = threading.Thread(target=demo,args=('read',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程-子线程全部运行结束")
if __name__ == '__main__':
    main()
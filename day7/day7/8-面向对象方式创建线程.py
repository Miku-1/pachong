import threading
import time

class singThread(threading.Thread):
    def __init__(self,name1):
        super().__init__()
        self.name1 = name1
    def run(self):
        for x in range(1,6):
            print('sing线程的名字是%s'%threading.current_thread().name)
            print('%s最喜欢唱山歌'%self.name1)
            time.sleep(1)

class danceThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        for x in range(1,6):
            print('dance线程的名字是%s' % threading.current_thread().name)
            print('%s最喜欢跳disco'%self.name)
            time.sleep(1)

def main():
    name1 = '小沈阳'
    name = '宋小宝'
    t1 = singThread(name1)
    t2 = danceThread(name)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
from multiprocessing import Process
import time

class SingProcess(Process):

    #重写run方法，进程启动之后执行这个函数
    def run(self):
        for x in range(1,6):
            print('我在唱歌')
            time.sleep(1)

class DanceProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        for x in range(1,6):

            print('我在跳广场舞，和%s'%self.name)
            time.sleep(1)


def main():
    name = '刘亦菲'
    p_sing = SingProcess()
    p_dance = DanceProcess(name)

    p_sing.start()
    p_dance.start()

    p_sing.join()
    p_dance.join()
    print('主进程-子进程运行结束')


if __name__ == '__main__':
    main()
























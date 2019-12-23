from multiprocessing import Process
import time,os

def sing():
    for x in range(1,6):
        print('唱歌进程id为%s'%os.getpid())
        print("我在唱歌")
        time.sleep(1)


def dance(name):
    for x in range(1,6):
        print('跳舞进程id为%s'%os.getpid())
        print('跳舞传来的参数是%s'%name)
        print('我在跳舞')
        time.sleep(1)

def main():
    name = '如花'
    #创建进程
    p_sing = Process(target=sing)
    p_dance = Process(target=dance,args=(name,))
    #启动
    p_sing.start()
    p_dance.start()
    #主进程需要等待子进程运行结束之后在结束
    p_sing.join()
    p_dance.join()

if __name__ == '__main__':
    main()





















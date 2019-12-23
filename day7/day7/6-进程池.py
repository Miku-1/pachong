from multiprocessing import Pool
import os,time

def demo(name):
    print('当前任务的名字是%s'%name)
    print('当前任务的进程为%s'%os.getpid())
    time.sleep(2)

def main():
    #创建一个进程池
    pol = Pool(10)
    lt = ['关云长','张翼德','赵子龙','马孟起','黄汉升','张文远','乐文谦','张俊艾','徐公明','于文则']
    for name in lt:
        pol.apply_async(demo,args=(name,))
    #关闭进程池
    pol.close()
    #主进程等待子进程结束后关闭
    pol.join()
    print('主进程-子进程全部结束')
if __name__ == '__main__':
    main()
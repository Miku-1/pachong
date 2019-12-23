from multiprocessing import Process
name = '张敏'

def read():
    print('读取的name值为%s'%name)

def change():
    global name
    name = '朱茵'
    print('修改后的name值为%s'%name)

def main():
    p2 = Process(target=read)
    p1 = Process(target=change)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()






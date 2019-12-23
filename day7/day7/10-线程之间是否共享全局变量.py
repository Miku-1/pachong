import threading
name = '章泽天'

def read():
    print('读取的name值为%s'%name)

def change():
    global name
    name = '路人甲'
    print('修改后的name值为%s'%name)

def main():
    t1 = threading.Thread(target=change)
    t2 = threading.Thread(target=read)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

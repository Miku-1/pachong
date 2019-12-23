import time
def sing():
    for x in range(1,6):
        print('我在唱自由飞翔')
        time.sleep(1)
def dance():
    for x in range(1,6):
        print('我在跳广场舞')
        time.sleep(1)

def main():
    sing()
    dance()
if __name__ == '__main__':
    main()
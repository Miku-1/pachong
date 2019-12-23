from queue import Queue

#要建一个队列对象
q = Queue(5)

#添加元素
q.put('科比')
q.put('韦德')
q.put('詹姆斯')
q.put('库里')
q.put('保罗')
#阻塞，等待队列中有位置以后将字母哥添加进去
print(q.full())
print(q.empty())
print(q.qsize())

#设置过期时间
# q.put('字母哥',True,3)

#获取
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.full())   #判断队列是否满
print(q.empty())    #判断队列是否为空
print(q.qsize())    #判断队列里的元素个数


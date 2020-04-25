# coding:utf-8 
# author:james
# datetime:2020/4/25 17:16


# 1 最初的生成器变形yield/send
def gen():
    """
    生成器函数最大的特点是可以接受外部传入的一个变量
    :return:
    """
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = 'got: %s' % receive


g = gen()
print(g.send(None))  # 通过g.send(None)或者next(g)启动生成器函数，并执行到第一个yield语句结束的位置
print(g.send('hello'))
print(g.send(123456))
# print(g.send('e'))


# 2 yield from
def g1():
    yield range(5)


def g2():
    """
    yield from iterable本质上等于for item in iterable: yield item的缩写版
    :return:
    """
    yield from range(5)


it1 = g1()
it2 = g2()
for x in it1:
    print(x)

for x in it2:
    print(x)


# 3 asyncio.coroutine和yield from
import asyncio,random
@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [
#         smart_fib(10),
#         stupid_fib(10),
#     ]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print('All fib finished.')
#     loop.close()


# 4 async和await
import time,asyncio,random
async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1)
strlist = ["ss","dd","gg"]
intlist=[1,2,5,6]
c1=mygen(strlist)
c2=mygen(intlist)
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        tasks = [
        c1,
        c2
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        print('All fib finished.')
        loop.close()





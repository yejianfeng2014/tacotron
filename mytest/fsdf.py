import threading


# 定义一个普通的action函数，该函数准备作为线程执行体
def action(max, a, b, c, e):
    print(max)

    print(a)
    print(b)

    print(c)

    print(e)

    # for i in range(max):
    #     # 调用threading模块current_thread()函数获取当前线程
    #     # 线程对象的getName()方法获取当前线程的名字
    #     print(threading.current_thread().getName() +  " " + str(i))


# 下面是主程序（也就是主线程的执行体）
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        t1 = threading.Thread(target=action, args=(100, 1, 2, 3, 4,))
        t1.start()
        # 创建并启动第二个线程
        t2 = threading.Thread(target=action, args=(200, 1, 2, 3, 4,))
        t2.start()

        t2.join()

        t1.join()
print('主线程执行完成!')

import threading

def action(max):
    # 线程主体
    for i in range(max):
        print(threading.current_thread().getName() + ' ' + str(i))



for i in range(100):
    print(threading.current_thread().getName() + ' ' + str(i))
    if i == 20:
        # 创建并启用第一个线程
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()

        t2 = threading.Thread(target=action, args=(100,))
        t2.start()

print("主线程执行完毕")
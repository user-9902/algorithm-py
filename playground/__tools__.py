
import threading
import time

# 第一个线程，打印奇数


def threada():

    for i in range(1, 100+1):
        if i % 2 != 0:
            lockb.acquire()
            print(i),
            locka.release()

# 第二个线程，打印偶数


def threadb():
    for i in range(1, 100+1):
        if i % 2 == 0:
            locka.acquire()
            print(i),
            lockb.release()


if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()

    ta = threading.Thread(None, threada)
    tb = threading.Thread(None, threadb)

    locka.acquire()  # 保证a先执行

    ta.start()
    tb.start()

    ta.join()

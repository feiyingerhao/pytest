import multiprocessing as mp
import threading as td


def job(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)


if __name__ == '__main__':
    queue = mp.Queue()
    p1 = mp.Process(target=job, args=(queue,))
    p2 = mp.Process(target=job, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = queue.get()
    res2 = queue.get()
    print(res1 + res2)

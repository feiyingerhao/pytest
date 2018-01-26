import threading
import time


def thread_job():
    print('T1 start')
    for i in range(10):
        time.sleep(0.1)
    print('T1 stop!')


def T2_job():
    print('T2 start')
    print('T2 finish')


def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    added_thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    added_thread2.start()
    added_thread.join()  # join 必须要等上面的运行万，后面的才能执行
    print('all done')


if __name__ == "__main__":
    main()

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import datetime
import time


demo_list = []
from gevent import thread

from thread_class import AsyncPool

pool = AsyncPool(maxsize=100, pool_maxsize=30)

async def aa(m):
    start = time.time()
    print("\n开始时间为：：：：", time.time())
    for i in range(100000000):
        pass
    demo_list.remove(m)
    end = time.time()
    print("用时::::", end - start, "\n")


async def sleep_met(thread_name, thread_id, m):
    # Use a breakpoint in the code line below to debug your script.
    print("sleep_met::::::::::::::开始：：：：：：：：：：：：")
    await  asyncio.run(aa(m))
    await  asyncio.sleep(2)
    print(f'Hi, {thread_name}:::::::::{thread_id}')  # Press Ctrl+F8 to toggle the breakpoint.



def mian():
    while True:
        print(demo_list)
        for i in range(20):
            demo_list.append(i)
            if len(demo_list) > 6:
                time.sleep(1.5)
                continue
            pool.no_block_submit(sleep_met(i, i, i))
        pool.wait()
        print(demo_list)

        # print(i, "pool.running::::::::::", pool.running)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # pass
    # no_block_submit_args
    # sleep_met('PyCharm', 1)
    mian()
    # aa()
    # print(thread.getcurre)
    # pool.release()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

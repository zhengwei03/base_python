import asyncio
import datetime
import time

demo_list = []
loop = asyncio.get_event_loop()

async def aa(m):
    start = time.time()
    print("\n开始时间为：：：：", time.time())
    for i in range(100000000):
        pass
    demo_list.remove(m)
    end = time.time()
    print("用时::::", end - start, "\n")


async def sleep_met(thread_name, thread_id, m):
    print("sleep_met::::::::::::::开始：：：：：：：：：：：：")
    coroutine1 = aa(m)
    task = asyncio.ensure_future(coroutine1)
    loop.run_until_complete(task)
    print(f'Hi, {thread_name}:::::::::{thread_id}')


def main_process():

    while 1:
        tasks = []
        for i in range(10):
            tasks.append(asyncio.ensure_future(sleep_met(i, i, i)))
        print(tasks)
        loop.run_until_complete(asyncio.wait(tasks))

main_process()



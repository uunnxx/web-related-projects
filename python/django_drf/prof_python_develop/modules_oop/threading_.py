import time
import threading


def sleep_time(wait: int, name: str) -> None:
    print(f'Name: {name}, sleep time: {wait}')
    time.sleep(wait)
    print(f'Waited {wait} seconds')


# td0 = threading.Thread(target=sleep_time, name='SleepTime', args=(3, 'Job1'))
# td1 = threading.Thread(target=sleep_time, name='SleepTime', args=(4, 'Job2'))
# td2 = threading.Thread(target=sleep_time, name='SleepTime', args=(1, 'Job3'))

# td0.start()
# td1.start()
# td2.start()

start = time.perf_counter()
threads = [
    threading.Thread(target=sleep_time, name='SleepTime1', args=(3, 'Job1')),
    threading.Thread(target=sleep_time, name='SleepTime2', args=(4, 'Job2')),
    threading.Thread(target=sleep_time, name='SleepTime3', args=(1, 'Job3'))
]

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


print(f'Time to execute threads length of {len(threads)}')
print(f'{time.perf_counter() - start}')

print('text after thread')

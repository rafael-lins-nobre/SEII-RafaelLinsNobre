import time
import multiprocessing

start = time.perf_counter()


def do_something(seconds):
    print(f'Dormindo por {seconds} segundo(s)...')
    time.sleep(seconds)
    print('Terminei de dormir...')


processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Terminei em  {round(finish - start, 2)} segundos(s)')

import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Dormindo por 1 segundo...')
    time.sleep(1)
    print('Terminei de dormir...')


# do_something()

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Terminei em  {round(finish - start, 2)} segundos(s)')

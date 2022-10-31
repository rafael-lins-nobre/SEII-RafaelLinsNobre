import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Dormindo por {seconds} segundo(s)...')
    time.sleep(seconds)
    print('Terminei de dormir...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())

    # secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Terminei em  {round(finish - start, 2)} segundos(s)')
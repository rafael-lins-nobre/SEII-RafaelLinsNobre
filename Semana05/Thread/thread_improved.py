import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f'Dormindo por {seconds} segundo(s)...')
    time.sleep(seconds)
    print("Terminei de dormir...")


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Terminou em {round(finish - start, 2)} segundo(s).')

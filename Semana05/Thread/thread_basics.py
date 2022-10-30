import time
import threading
# import concurrent.futures

start = time.perf_counter()


def do_something():  # define a founção do_something() recebendo como argumento os segundos que irá dormir
    print("Dormindo por 1 segundo...")
    time.sleep(1)
    print("Terminei de dormir")


#do_something()
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Terminou em {round(finish - start, 2)} segundo(s).')

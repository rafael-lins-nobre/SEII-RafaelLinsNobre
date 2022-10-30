import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds):
    print(f'Dormindo por {seconds} segundo(s)...')
    time.sleep(seconds)

    return f"Terminei de dormir... {seconds} segundo(s)"


with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1) #criamos os executors passando o argumento 1, para 1 segundo
    # f2 = executor.submit(do_something, 1)
    # print(f1.result()) #rodando o método result, nos esperamos até a função se completar
    # print(f2.result())

    # secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
        # print(f.result())

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Terminou em {round(finish - start, 2)} segundo(s).')


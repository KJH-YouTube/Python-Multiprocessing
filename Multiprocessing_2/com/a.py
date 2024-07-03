from multiprocessing import Pool
import psutil
import os

def f(x):
    #print(psutil.Process().cpu_num())
    print(f'{x} / Sub-process: {os.getgid()}')
    return x*x

if __name__ == '__main__':
    print(f'Parent-process: {os.getpid()}')
    p = Pool(5)
    with p:
        res = p.map(f, range(8))
        print(res)

    
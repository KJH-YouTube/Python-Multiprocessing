from multiprocessing import Pool
import psutil
import os, time

"""
    - Pool could be more convenient to manage Processes.
    - However, it makes performance degradation between Processes.
    - WHY? ... It is related to GIL (Please refer to mp_lock_value.py file).
"""



def work(x):
    #print(psutil.Process().cpu_num())
    psp = psutil.Process()
    print(f'{x} / Sub-process: {os.getpid()} / CPU Core ID: {psp.cpu_num()}')
    time.sleep(2)
    return x*x


# [CAUTION]
# You should implement the process pool in the entry point
# , which means if __name__ == '__main__'
def main():
    p = Pool(5)
    
    if True:
        """
            Process.Pool.map Format
        """
        with p: # "with Pool(5) as p" also allowed
            res = p.map(work, range(8)) # The argument is longer than the pool size
            # return function's return value
            # args should be iterable


    if False:
        """
            Process.Pool.apply Format
            when you need to run a function in another process for some reason 
            (and you want to use a process pool instead of creating a new process to run the function).
            It is not better suited for performing work in parallel.
        """
        with p:
            res = []
            a = None
            for i in range(8):
                a = p.apply(work, (i, ))     # return function's return value
                res.append(a)                # args should be iterable
    
    # Then, when we need this?
    # Actually, you wouldn't face frequently cases, which use the apply() method.


    print(res)
    return


#
# main test
#
if __name__ == '__main__':
    print(f'CPU number: {psutil.Process().cpu_num()}')
    print(f'Parent-process: {os.getpid()}')
    main()
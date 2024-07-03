from multiprocessing import Pool
import psutil
import os, time


def work(x):
    #print(psutil.Process().cpu_num())
    psp = psutil.Process()
    print(f'{x} / Sub-process: {os.getpid()} / CPU Core ID: {psp.cpu_num()}')
    time.sleep(2)
    return x*x


def check_alive(prcs):
    for p in prcs:
        if not p.ready():
            return True
        else:
            continue
    return False



# [CAUTION]
# You should implement the process pool in the entry point
# , which means if __name__ == '__main__'
def main():
    p = Pool(5)
    
    with p: # "with Pool(5) as p" also allowed
        if True:
            """
                Process.Pool.map Format
            """
            res = p.map_async(work, range(8))  # The argument is longer than the pool size
            # return function's return value
            # args should be iterable

        if False:
            """
                Process.Pool.apply Format
                when you need to run a function in another process for some reason 
                (and you want to use a process pool instead of creating a new process to run the function).
                It is not better suited for performing work in parallel.
            """
            res = []
            for i in range(8):
                res.append(p.apply_async(f, (i, )))


        # [CAUTION]
        # If you implement your code out of 'with'
        # then, the variable 'res' could be shut down.
        # After using _async_ functionality, you should use .get() method for results.
        # The _async_ makes the returns to be managed as AsyncResult
        i = 0
        done = False
        while not done:
            if i == 4:  # re-initialization
                i = 0 

            print(f'\rLoading{"."*i}', end='')
            time.sleep(1.5)
            print(f'\r{" "*12}', end='')
            i += 1
            
            # Check whether processes are done
            try:
                done = res.ready()      # map-version 
                print(f'\n{res.get()}') # list does not have .ready method
            except:
                done = check_alive(res)                 # apply-version
                print(f'\n{[val.get() for val in res]}')   
    
    return


#
# main test
#
# [CAUTION]
# You should implement the process pool in the entry point
# , which means if __name__ == '__main__'
if __name__ == '__main__':
    print(f'CPU number: {psutil.Process().cpu_num()}')
    print(f'Parent-process: {os.getpid()}')
    main()
"""
[Please ReadMe]
* Method 1 or Method 2 is recommended.
* They are more efficient on the viewsight of 'spatial locality'.
* Plus, more efficient for memory management.
* But method 3 is also needed when a program requires multiple lock groups.
"""


import multiprocessing as mp
import time, os
import ctypes

from utils import log_cpu_pid


## Method 1
## Lock of the Variable Itself
def work1(sv, cnt):
    """
    The work function for lock of shared variable.
    
    Parameters
    ----------
    sv : shared variable object
    cnt : sum `cnt` times
    
    Return
    ------
    None
    """
    
    #print(os.getpid()) # to check pid
    for _ in range(cnt):
        sv.acquire()
        sv.value += 1
        sv.release()

## Method 2
## Automatic lock-aquire and lock-release
## Equivalent to Lock of the Variable Itself
def work2(sv, cnt):
    """
    The work function for lock of shared variable.
    
    Parameters
    ----------
    sv : shared variable object
    cnt : sum `cnt` times
    
    Return
    ------
    None
    """
    
    #print(os.getpid()) # to check pid
    for _ in range(cnt):
        with sv.get_lock(): 
            # sv.get_lock() = lock object
            # calls 'with' and enter a lock seesion
            # return a lock value [True or False]
            sv.value += 1
    return

## Method 3
## Independent Lock
def work3(sv, cnt, lock):
    """
    The work function for an independent lock object.
    
    Parameters
    ----------
    sv : shared variable object
    cnt : sum `cnt` times
    lock: lock object
    
    Return
    ------
    None
    """
    
    #print(os.getpid()) # to check pid
    for _ in range(cnt):
        lock.acquire()
        sv.value += 1
        lock.release()
    return

def main():
    """
    The main function. This function computes summation of `cnt`*`activated processor number` by incrementing 1 
    
    Parameters
    ----------
    None
    
    Return
    ------
    None
    """
    
    # Data Initialization for Shared Memory
    # multiprocessing.Value(typecode_or_type, *args, lock=True)
    # typecode_or_type: implemented in sharedctypes.py
    #shared_var = mp.Value(ctypes.c_int, 0)   #type
    shared_var = mp.Value('i', 0, lock=True)            #typecode

    # Variable Init
    cnt = 1000000
    sv_lock = mp.Lock()

    # Process Creation
    procs = []
    for _ in range(2):
        p = mp.Process(target=work2, args=(shared_var, cnt))
        #p = mp.Process(target=work3, args=(shared_var, cnt, sv_lock))
        procs.append(p)

    _TIME1 = time.time()
    for p in procs:
        p.daemon = True
        p.start()
 
    # just join() method
    while len(procs) != 0:
        for proc in procs:
            if not proc.is_alive(): # check processes' end
                proc.close()        # close process
                procs.remove(proc)  # remove process from tasks list
            # do something
    _TIME2 = time.time()

    print(f'Final value in shared memory: {shared_var.value} --- {_TIME2-_TIME1:.5} sec')


#
# main test
#
if __name__ == '__main__':
    log_cpu_pid(p_sec='Parent-process', c_sec='CPU Core ID')
    main()
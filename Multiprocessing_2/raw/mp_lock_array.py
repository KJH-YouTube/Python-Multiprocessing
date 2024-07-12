"""
* This file articulates the method to unlimit the waiting functionality, as known as .join().
* Commands for this file follows `~$ python3 <filename>`
* e.g. python3 mp_lock_array.py

* This file includes how to utilize Process.daemon and extra methods for multiprocessing.Process.
"""

import multiprocessing as mp

from utils import log_cpu_pid

## Method 1 applied from mp_lock_value.py
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
    for i in range(cnt):
        sv.acquire() # if sv's lock property is False, it throws exception
        sv[i%10] += 1
        sv.release() # if called any lock is not acquired, it throws exception


def main():
    """
    The main function. This function performs some operations to mp.Array objects. 
    
    Parameters
    ----------
    None
    
    Return
    ------
    None
    """
    # Data Initialization for Shared Memory
    # Array(typecode_or_type, size_or_initializer, *, lock=True)
    # typecode_or_type   : implemented in sharedctypes.py
    # size_or_initializer: 
    
    """ Here, Initialization is required """
    shared_arr = mp.Array('i', list(range(10)), lock=True)            #typecode
    shared_str = mp.Array('c', b'Hello, World') # bytearray only & bytearray can have two attributes: value and raw


    # Variable Init
    cnt = 100000


    # Process Creation
    procs = []
    for _ in range(2):
        p = mp.Process(target=work1, args=(shared_arr, cnt))
        procs.append(p)

    for p in procs:
        p.daemon = True
        p.start()
    
    # join()
    while len(procs) != 0:
        for proc in procs:
            if not proc.is_alive(): # check processes' end
                proc.close()        # close process
                procs.remove(proc)  # remove process from tasks list
            # do something
    print(f'Final Array in shared memory: {[ v for v in shared_arr ]}')
    print(shared_str.value)

#
# main test
#
if __name__ == '__main__':
    log_cpu_pid(p_sec='Parent-process', c_sec='CPU Core ID')
    main()
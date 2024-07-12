"""
* This file articulate the method to manage Processes at once altogether.
* Commands for this file follows `~$ python3 <filename>`
* e.g. python3 mp_pool.py

* This file explains two main functionality, which are map() and apply(), for Pool methods.

[Weakness]
* However, it makes performance degradation between Processes.
* WHY? ... It is related to GIL (Please refer to mp_lock_value.py file).
* and the versatile functionalities.
"""

from multiprocessing import Pool
import psutil
import os, time

from utils import log_cpu_pid

def work(x):
    """
    The work function to calculate a square number at each process.
    
    Parameters
    ----------
    x : is an `int` number
    
    Return
    ------
    return a squared number (x^2)
    """
    
    log_cpu_pid(p_sec='Sub-process', c_sec='CPU Core ID')
    # use this to visualize
    time.sleep(2)
    return x*x


# [CAUTION]
# You should implement the process pool in the entry point
# , which means if __name__ == '__main__'
def main():
    """
    The main function. This function utilizes non-daemon methods of multiprocessing.Pool class. 
    
    Parameters
    ----------
    None
    
    Return
    ------
    None
    """
    
    p = Pool(5)
    
    if True:
        """
            * Process.Pool.map Format
            this method has kinda good strength
            Most of people thinks that arguments could be only same data types because argument collection should be iterable
            If one given function could take many types, then argument could be '[int, str]'.
        """
        with p: # "with Pool(5) as p" also allowed
            """Here, pool.map is required"""
            pass
            # return function's return value
            # args should be iterable


    if False:
        """
            * Process.Pool.apply Format
            when you need to run a function in another process for some reason 
            (and you want to use a process pool instead of creating a new process to run the function).
            It is not better suited for performing work in parallel.
            It has a strength to customize the processes in the pool including functions and arguments.
        """
        with p:
            res = []
            a = None
            for i in range(8):
                """Here, pool.apply is required"""
                
    
    # Then, when we need this?
    # Actually, you wouldn't face frequently cases, which use the apply() method.


    print(res)
    return


#
# main test
#
if __name__ == '__main__':
    log_cpu_pid(p_sec='Parent-process', c_sec='CPU Core ID')
    main()
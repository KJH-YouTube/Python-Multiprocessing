"""
* This file articulates the method to unlimit the waiting functionality, as known as .join().
* Commands for this file follows `~$ python3 <filename>`
* e.g. python3 mp_pool.py

* This file includes how to utilize Process.daemon and extra methods for multiprocessing.Process.

[Strength]
* Pool has versatile functionalities also.

[Weakeness]
* However, this can make Pool slower.
"""

from multiprocessing import Pool
import psutil
import os, time

from utils import log_cpu_pid

def work(x):
    """
    The work function to compute a squared number and print simple cpu info.
    
    Parameters
    ----------
    x : an `int` number
    
    Return
    ------
    None
    """
    log_cpu_pid(p_sec='Sub-process', c_sec='CPU Core ID') # try on/off
    time.sleep(5)
    return x*x


def check_alive(prcs):
    """
    A function to check the given process are alive
    
    Parameters
    ----------
    prcs : iterable container wrapping process objects
    
    Return
    ------
    bool : return True when all process are done
    """
    for p in prcs:
        try:
            p.get(timeout=0) # if not get, it's not done
        except:
            return False
    return True



# [CAUTION]
# You should implement the process pool in the entry point
# , which means if __name__ == '__main__'
def main():
    """
    The main function. This function utilizes async methods of multiprocessing.Pool class. 
    
    Parameters
    ----------
    None
    
    Return
    ------
    None
    """
    
    p = Pool(5)
    
    with p: # "with Pool(5) as p" also allowed
        if True:
            """
                Process.Pool.map Format
            """
            
            """Here, implementation is required """

        if False:
            """
                Process.Pool.apply Format
                when you need to run a function in another process for some reason 
                (and you want to use a process pool instead of creating a new process to run the function).
                It is not better suited for performing work in parallel.
            """
            
            """Here, implementation is required """


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
            if type(res) != list:
                done = res.ready()                      # map-version 
            else:
                done = check_alive(res)                 # apply-version

 
        if type(res) != list:
            print(f'\n{res.get(timeout=0)}') # list does not have .ready method
        else:
            print(f'\n{[val.get(timeout=0) for val in res]}')   
    
    return


#
# main test
#
# [CAUTION]
# You should implement the process pool in the entry point
# , which means if __name__ == '__main__'
if __name__ == '__main__':
    #print(f'CPU number: {psutil.Process().cpu_num()}')
    log_cpu_pid(p_sec='Parent-process', c_sec='CPU Core ID')
    main()
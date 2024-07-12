"""
* This file articulates the method to data communication between threads using local.
* Commands for this file follows `~$ python3 <filename> <number>`
* e.g. python mt_thrd_local_adv.py 1000

* This is the advanced version.
"""

import threading as thrd
import sys, time, os
import ctypes

from utils import log_cpu_pid

class WrongAttributeException(Exception):
    # When the program is given a wrong command input
    pass


## This function was defined to handle the case
## that the input command is single.
def work1(num):
    summation = 0
    for i in range(1, num+1):
        summation += i
    return summation


## This function was defined to handle the case
## that the input command is multi.
def work2(id, result, start, end):
    mid = 0
    print(os.getpid()) # to check pid
    for i in range(start+1, end+1):
        mid += i
    result.append(mid)
    return


## C Data Types
## To Refer to Objects
## To Improve Speed  
def work3(id, result, start, end):
    for v in range(start+1, end+1):
        result.value += ctypes.c_int(v).value # ctype value
    print(f'{os.getpid()}: {result}')
    #print(f'{os.getpid()}: {result.value}') # if you want real values
    return

## Python Data Type
## General Approach Which People Could Do First
def work4(id, result, start, end):
    mid = 0
    for v in range(start+1, end+1):
        mid += v
    result += mid
    print(f'{os.getpid()}: {result}')
    return


## This Section was defined for main function
def main(args):
    """
    The main function. It includes a simple number using local.
    
    Parameters
    ----------
    args : the length should be 2. 2nd one is enough big number.
    ex) args would be ['mt_thrd_queue.py', '10000']
    
    Return
    ------
    Tuple : has two elements. (`result`, `execution time`)
    
    Exceptions
    -----------
    raise WrongAttributeException
    due to wrong numbers of command arguments
    due to wrong command options
    """
    
    print(f'Parent-process: {os.getpid()}')

    # The number of input command elements always
    # should be 2.
    if len(args) > 2: # ["mt_thrd_local_adv.py", "1000000"] (for example)
        raise WrongAttributeException("Too many arguments")
    
    else:
        tasks = []
        num = int(args[1])
        p_num = 8

        # If input number is under 8,
        # then it needs not to use multiprocessing
        # Actually, this number doesn't have to be 8
        # You can choose a number you want.
        if num < 8:
            _TIME1 = time.time()
            result = work1(int(args[2]))
            _TIME2 = time.time()
            return result, _TIME2 - _TIME1
        
        _TIME1 = time.time()

        # Here, local is required
        local = thrd.local()
        
        if False:
            """
                Method 1
                for work2 function
                a method from [mt_thrd_local.py]
            """
            
            local.result = [] # GIL affect ? -> mp(o) / mt(x)
                              # (if you don't know GIL, skip this and watch the YouTube lecture video.)
            for i in range(p_num):
                th = thrd.Thread(target=work2, args = (i, local.result, (num*i)//8, (num*(i+1))//8 ))
                # 100000
                # 0~12500, 12500 ~ 25000, ...
                tasks.append(th)
                th.start()

            for task in tasks:
                task.join()
        
            result = 0
            for n in local.result:
                result += n
        
            _TIME2 = time.time()

            return result, _TIME2 - _TIME1
        

        if True:
            """ 
                Method 2 
                for work3 & work4 function
            """

            """ Here, initialization is required! """
            for i in range(p_num):
                """ Here, functions are required! """
                th = thrd.Thread(target=work3, args = (i, local.result, (num*i)//8, (num*(i+1))//8 ))
                # How about args = (i, local, ...) ? Exceptional?
                tasks.append(th)
                th.start()

            for task in tasks:
                task.join()
        
            _TIME2 = time.time()
            return local.result, _TIME2 - _TIME1



#
# main test
#
if __name__ == '__main__':
    args = sys.argv
    #print(args)
    result, ex_time = main(args)
    try:
        # Method 2
        print(f"SUM of 0 ~ {args[1]} : {result.value} in {ex_time:.5f} sec")
    except:
        # Method 1
        print(f"SUM of 0 ~ {args[1]} : {result} in {ex_time:.5f} sec")
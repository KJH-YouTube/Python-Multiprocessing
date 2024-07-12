"""
* This file articulates the method to data-communicate within threads together.
* Commands for this file follows `~$ python3 <filename> <number>`
* e.g. python3 mt_thrd_local.py 10000

* This file explains data-communication example to use local object memory.
"""

import threading as thrd
import sys, time, os

from utils import log_cpu_pid

class WrongAttributeException(Exception):
    # When the program is given a wrong command input
    pass


## This function was defined to handle the case
## that the input command is single.
def work1(num):
    """
    The work function for single thread proessing.
    
    Parameters
    ----------
    num : is an `int` number
    
    Return
    ------
    return an `int` result from 1 to `num`
    """
    summation = 0
    for i in range(1, num+1):
        summation += i
    return summation


## This function was defined to handle the case
## that the input command is multi.
def work2(id, result, start, end):
    """
    The work function for multi-threaded processing.
    
    Parameters
    ----------
    id : `int` number for thread id to manage threads efficiently
    result : `Queue` to accumulate results (from `start` to `end`) of each threads
    start : an `int` number.
    end : an `int` number. 
    
    Return
    ------
    return None
    """
    mid = 0
    print(os.getpid()) # to check pid
    for i in range(start+1, end+1):
        mid += i
    result.append(mid)
    return


## This Section was defined for main function
def main(args):
    """
    The main function. It includes a list operation with local.
    
    Parameter
    ---------
    args : the length should be 2. 2nd one is an enough big number.
    ex) args would be ['mt_thrd_local.py', 10000']
    
    Return
    ------
    Tuple : has two elements. (`result`, `execution time`)
    
    Exceptions
    -----------
    raise WrongAttributeException
    due to wrong numbers of command arguments
    due to wrong command options
    """
    
    log_cpu_pid(p_sec='Parent-process', c_sec='CPU Core ID')

    # The number of input command elements always
    # should be 2.
    if len(args) > 2: # ["mt_thrd_local.py", "1000000"] (for example)
        raise WrongAttributeException("Too many arguments")
    
    else:
        tasks = []
        num = int(args[1])

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

        """Here, local is required"""
        


        for i in range(8):
            """Here, Thread function for local to be applied is required"""
            
            tasks.append(th)
            th.start()

        
        for task in tasks:          # Await
            task.join()
        

        result = 0                  # Assemble final results
        """Here, how to assemble final results?"""
        
        
        _TIME2 = time.time()

        return result, _TIME2 - _TIME1


#
# main test
#
if __name__ == '__main__':
    args = sys.argv
    #print(args)
    result, ex_time = main(args)
    print(f"SUM of 0 ~ {args[1]} : {result} in {ex_time:.5f} sec")
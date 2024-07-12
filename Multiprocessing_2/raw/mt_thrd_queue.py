"""
* This is very similar with the previous multiprocessing direcotry, which is Multiprocessing_1/multi.py
* Commands for this file is similar too.
* e.g. python3 mt_thrd_queue.py multi 10000

* Then, why does this file exist?
* It's because this is an example of using a Thread not a Process.
"""

import threading as thrd
from multiprocessing import Queue
import sys, time

from utils import log_cpu_pid


class WrongAttributeException(Exception):
    # When the program is given a wrong command input
    pass


## This function was defined to handle the case
## that the input command is single.
def work1(num):
    """
    The work function for single thread proessing.
    
    Parameter
    ---------
    * num: is an `int` number
    
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
    * id: `int` number for thread id to manage threads efficiently
    * result: `Queue` to accumulate results (from `start` to `end`) of each threads
    * start: an `int` number.
    * end: an `int` number. 
    
    Return
    ------
    return None
    """
    log_cpu_pid(p_sec='Sub-process', c_sec='CPU Core ID')
    mid = 0
    for i in range(start+1, end+1):
        mid += i
    result.put(mid)
    return


## This Section was defined for main function
def main(args):
    """
    The main function when the file is executed
    
    Parameters
    ----------
    args : the length should be 3. 2nd one is type and 3rd one is enough big number.
    ex) args would be ['mt_thrd_queue.py', 'multi', '10000']
    
    Return
    ------
    `Tuple` : has two elements. (`result`, `execution time`)
    
    Exceptions
    -----------
    raise WrongAttributeException
    due to wrong numbers of command arguments
    due to wrong command options
    """
    
    
    # The number of input command elements always
    # should be 3.
    if len(args) > 3: # ["mt_thrd_queue.py", "single", "1000000"] (for example)
        raise WrongAttributeException("Given 2 more arguments. Expected is 2 arguments.")
    
    # For Single Processing
    elif args[1].lower() == "single":
        _TIME1 = time.time()
        result = work1(int(args[2]))
        _TIME2 = time.time()
        return result, _TIME2 - _TIME1
    
    # For Multi Processing
    elif args[1].lower() == "multi":
        queue = Queue()
        tasks = []
        num = int(args[2])

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

        for i in range(8):
            th = thrd.Thread(target=work2, args = (i, queue, (num*i)//8, (num*(i+1))//8 ))
            # 100000
            # 0~12500, 12500 ~ 25000, ...
            tasks.append(th)
            th.start()

        for task in tasks:
            task.join()

        # To imprint the end sign at last cell
        queue.put("END")
        result = 0
        
        # Join the results computed by the threads
        while True:
            mid = queue.get()
            if mid == "END":
                _TIME2 = time.time()
                return result, _TIME2 - _TIME1
            result += mid
    
    else:
        ## If the command elements are lacked
        raise WrongAttributeException(f"Not Listed option")


#
# main test
#
if __name__ == '__main__':
    args = sys.argv
    #print(args)
    result, ex_time = main(args)
    print(f"SUM of 0 ~ {args[2]} : {result} in {ex_time:.5f} sec")
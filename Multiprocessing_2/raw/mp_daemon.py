"""
* This file articulates the method to unlimit the waiting functionality, as known as .join().
* Commands for this file follows `~$ python3 <filename>`
* e.g. python3 mp_pool.py

* This file includes how to utilize Process.daemon and extra methods for multiprocessing.Process.

[Strength]
* This is very straightfoward.

[Weakeness]
* However, this could seem very trivial.
"""

from multiprocessing import Process, Queue
import sys, time, os
import psutil

from utils import log_cpu_pid

class WrongAttributeException(Exception):
    # When the program is given a wrong command input
    pass


## This function was defined to handle the case
## that the input command is multi.
def work2(id, queue, start, end):
    """
    The work function to compute a summation from `start` to `end` and collect it to `queue`.
    
    Parameters
    ----------
    id : simple integer number for process id
    queue : a Queue object to collect results on inter-process
    start : start number to sum
    end : end number to sum
    
    Return
    ------
    None
    """
    print(os.getpid())
    mid = 0
    for i in range(start+1, end+1):
        mid += i
    queue.put(mid)
    return

#
# Add
# Simple function
def work3(id):
    """
    The work function to print simple cpu info.
    
    Parameters
    ----------
    id : simple integer number for process id
    
    Return
    ------
    None
    """
    psp = psutil.Process()
    log_cpu_pid(p_sec='Sub-process', c_sec='CPU Core ID')
    time.sleep(5)
    return

#
# Add
# Load function
def load():
    """
    A loader function like a loading screen
    
    Parameters
    ----------
    None
    
    Return
    ------
    None
    """
    i = 0    
    while True:     
        if i == 4:  
            i = 0   # re-initialization 

        print(f'\rLoading{"."*i}', end='')
        time.sleep(1.5)
        print(f'\r{" "*12}', end='')
        i += 1
    return


## This Section was defined for main function
def main(args):
    """
    The main function when the file is executed
    
    Parameter
    ---------
    args : the length should be 1.
    ex) args would be ['mp_daemon.py']
    
    Return
    ------
    None
    
    Exceptions
    -----------
    raise WrongAttributeException
    due to wrong numbers of command arguments
    due to wrong command options
    """
    
    # The number of input command elements always
    # should be 1.
    if len(args) > 1: # ["mp_daemon.py"] (for example)
        raise WrongAttributeException("Too many arguments")
    
    # For Multi Processing
    else:
        p_num = 4
        queue = Queue() # for work2
        cnt = 100000    # for work2
        tasks = []
        

        _TIME1 = time.time()    # Time Measurement
        for i in range(p_num):
            # With work2 func
            thrd = Process(target=work2, args = (i, queue, (cnt*i)//p_num, (cnt*(i+1))//p_num))
            # With work3 func
            #thrd = Process(target=work3, args = (i,))
            # [CAUTION]
            # daemon should be stated before the thread starts.
            """Here, daemon is required"""

        """Here, daemon is required"""

        #for task in tasks:
        #    task.join()

        # Actually, this block functions .join().
        # Then, why is the daemon used?
        # It is because the given function is not appropriate for the 'background process'
        # Let's think of a game, which has a chatting system.
        # It does not require any of inter-processes data communication.
        while len(tasks) != 0:
            for task in tasks:
                if not task.is_alive(): # check processes' end
                    task.close()        # close process
                    tasks.remove(task)  # remove process from tasks list
            # do something if you need
        _TIME2 = time.time()    # Time Measurement

        """Here, how to finish?"""


        # Depending on function
        # Print other results.
        if queue.empty(): # for work2
            print(f"\nProcess Done in {_TIME2-_TIME1:.5} sec")
        else:
            res = 0
            for _ in range(p_num):
                res += queue.get_nowait()
            print(f"\nProcess Done - Result: {res} in {_TIME2-_TIME1:.5} sec")
        
#
# main test
#
if __name__ == '__main__':
    args = sys.argv
    log_cpu_pid(p_sec='Parent-process', c_sec='CPU Core ID')
    main(args)
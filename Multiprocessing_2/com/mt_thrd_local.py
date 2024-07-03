import threading as thrd
import sys, time, os

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


## This Section was defined for main function
def main(args):
    print(f'Parent-process: {os.getpid()}')

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

        # Here, local is required
        local = thrd.local()    # Main thread local memory region.
        local.result = []       # 'result' is stored as an element of dict of local


        for i in range(8):
            th = thrd.Thread(target=work2, args = (i, local.result, (num*i)//8, (num*(i+1))//8 ))
            # 100000
            # 0~12500, 12500 ~ 25000, ...
            tasks.append(th)
            th.start()

        
        for task in tasks:          # Await
            task.join()
        

        result = 0                  # Assemble final results
        for n in local.result:
            result += n
        
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
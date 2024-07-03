from multiprocessing import Process, Queue
import sys, time, os
import psutil

class WrongAttributeException(Exception):
    # When the program is given a wrong command input
    pass


## This function was defined to handle the case
## that the input command is multi.
def work2(id, queue, start, end):
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
    psp = psutil.Process()
    print(f'{id} / Sub-process: {os.getpid()} / CPU Core ID: {psp.cpu_num()}')
    time.sleep(5)
    return

#
# Add
# Load function
def load():
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
    # The number of input command elements always
    # should be 2.
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
            thrd.daemon = True  # it means the thread would be operated in background
            tasks.append(thrd)
            thrd.start()

        load_proc = Process(target=load)
        load_proc.daemon = True
        load_proc.start()


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

        load_proc.terminate()   # Terminate a process
        load_proc.join()        # Wait until the process is completely terminated
        # ~~~~~~~~^^^^^^ why is it required?
        load_proc.close()       # Free the object resource


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
    print(f'Parent Process ID: {os.getpid()}')
    main(args)
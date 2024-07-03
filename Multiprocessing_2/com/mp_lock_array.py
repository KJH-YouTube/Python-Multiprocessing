import multiprocessing as mp
import os

## Method 1 applied from mp_lock_value.py
def work1(sv, cnt):
    for i in range(cnt):
        sv.acquire() # if sv's lock property is False, it throws exception
        sv[i%10] += 1
        sv.release() # if called any lock is not acquired, it throws exception


def main():
    # Data Initialization for Shared Memory
    # Array(typecode_or_type, size_or_initializer, *, lock=True)
    # typecode_or_type   : implemented in sharedctypes.py
    # size_or_initializer: 
    
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


#
# main test
#
if __name__ == '__main__':
    print(f'Parent Process ID: {os.getpid()}')
    main()
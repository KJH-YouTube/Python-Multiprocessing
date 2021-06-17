from multiprocessing import Process, Queue
import sys, time

class WrongAttributeException(Exception):
    #When the program is given a wrong command input
    pass

def work1(num):
    summation = 0
    for i in range(1, num+1):
        summation += i
    return summation

def work2(id, queue, start, end):
    mid = 0
    for i in range(start+1, end+1):
        mid += i
    queue.put(mid)
    return

def main(args):
    if len(args) != 3: # ["multi2.py", "single", "1000000"] (for example)
        raise WrongAttributeException("Given 1 more arguments. Expected is 1 argument.")
    elif args[1].lower() == "single":
        _TIME1 = time.time()
        result = work1(int(args[2]))
        _TIME2 = time.time()
        return result, _TIME2 - _TIME1
    elif args[1].lower() == "multi":
        queue = Queue()
        tasks = []
        num = int(args[2])

        if num < 8:
            _TIME1 = time.time()
            result = work1(int(args[2]))
            _TIME2 = time.time()
            return result, _TIME2 - _TIME1
        
        _TIME1 = time.time()
        for i in range(8):
            thrd = Process(target=work2, args = (i, queue, (num*i)//8, (num*(i+1))//8 ))
            # 100000
            # 0~12500, 12500 ~ 25000, ...
            tasks.append(thrd)
            thrd.start()

        for task in tasks:
            task.join()

        queue.put("END")
        result = 0
        # 
        while True:
            mid = queue.get()
            if mid == "END":
                _TIME2 = time.time()
                return result, _TIME2 - _TIME1
            result += mid
    
    else:
        raise WrongAttributeException(f"Not Listed option - {args[1]}")

if __name__ == '__main__':
    args = sys.argv
    #print(args)
    result, ex_time = main(args)
    print(f"SUM of 0 ~ {args[2]} : {result} in {ex_time:.5f} sec")

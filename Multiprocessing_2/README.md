# Multiprocessing 2

## Contents

* [Introduction](#introduction)
* [Purpose](#purpose)
* [Description](#description)
* [Execution Commands](#execution-commands)
* [References and Extra Study](#references-and-extra-study)

## Introduction

This python-multiprocessing folder includes contents of this GitHub project's `purpose` and the main themes of the second multiprocessing lecture (on YouTube). This section deals with important concepts of parallel computing in the computer science field. Involving `thread`, `process`, `processor`, `process pool`, `daemon`, `asynchronization`, `synchronization`, `lock`, `GIL`, and `shared memory`, this project will enhance user experiences for parallel computing and multiprocessing. In this folder, many files have different and independent commands. Thus, it is recommended to check the execution commands section at least once.

## Purpose

For this program and video, I wanted those who want to study Python multiprocessing (threading) to learn this topic and programming skills with more efficient methods. Actually, although there are many directions and methods to implement multiprocessing program with python multiprocessing built-in module, some applications and methods which are revealed by public were sometimes not good and efficient. Thus, I wanted to provide people with more efficient structures of multiprocessing programming code design in Python.

## Description

Like every studying and lecture, my project also cannot include all contents, which are implemented in CPython. What my repository covers is the methods and modules that I frequently have utilized in my research. I tried to include the core functionalities of Python multiprocessing to maintain and utilize them in the easiest direction. The following table states the main contents of the given files in this folder.


| Filename               | Main content                                                                                   |
| ------------------------ | :----------------------------------------------------------------------------------------------- |
| `mp_daemon.py`         | The concept of daemon and multiprocessing programming of daemon-version.                       |
| `mp_lock_array,py`     | A synchronized shared-memory data type array to hold a lock (mp.Array-version).                |
| `mp_lock_value.py`     | A synchronized shared-memory function Value to hold two kinds of lock.                         |
| `mp_pool.py`           | Pool-managed multiprocessing                                                                   |
| `mp_pool_async.py`     | Pool-managed multiprocessing with asynchronizing                                               |
| `mt_thrd_local.py`     | A multithreaded programming to give communal data to each threads.                             |
| `mt_thrd_local_adv.py` | Advanced version of`mt_thrd_local` including ctypes integer value for performance optimization |
| `mt_thrd_queue.py`     | A multithreaded programming version of same operation a previous lecture.                      |

## Execution Commands

### Command 1

for a list of the following files: `mp_daemon.py`, `mp_lock_array.py`, `mp_lock_value.py`, `mp_pool_async.py`, and `mp_pool.py`.

For ***MacOS*** and ***Linux***

```bash
~$ python3 <filename.py>
```

For ***Windows***

```bash
~$ python <filename.py>
```

### Command 2

for a list of the following files: `mt_thrd_local_adv.py` and `mt_thrd_local.py`.

For ***MacOS*** and ***Linux***

```bash
~$ python3 <filename.py> <integer_number>
```

For ***Windows***

```bash
~$ python <filename.py> <integer_number>
```

### Command 3

for a list of the following files: `mt_thrd_queue.py`.

For ***MacOS*** and ***Linux***

```bash
~$ python3 <filename.py> <computing_type> <integer_number>
```

For ***Windows***

```bash
~$ python <filename.py> <computing_type> <integer_number>
```

> `<computing_type>` stands for "single" or "multi". This command line has an identical command structure with Multiprocessing_1 section.

## References and Extra Study

1. [Differences between map, apply, and async](https://discuss.python.org/t/differences-between-pool-map-pool-apply-and-pool-apply-async/6575/2)
2. [Multiprocessing.Pool and ProcessPoolExecuter](https://superfastpython.com/multiprocessing-pool-vs-processpoolexecutor/)
3. [CPython Implementation - Python 3.12](https://github.com/python/cpython/tree/3.12/Lib/)
4. [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

<br>

1. [SharedMemory](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory)
2. [Sharable List](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList)
3. [SharedMemoryManager](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager)
   <br>

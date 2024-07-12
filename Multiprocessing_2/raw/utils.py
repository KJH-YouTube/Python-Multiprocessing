import platform, os
import psutil


def log_cpu_pid(p_sec, c_sec=None) -> None:
    # process section
    # core section
    
    os = platform.system()

    # Windows
    if os == 'Windows':
        print(f'{p_sec}: {os.getpid()}')
    # MacOS
    elif os == 'Darwin':
        print(f'{p_sec}: {os.getpid()}')
    # Linux
    elif os == 'Linux':
        psp = psutil.Process()
        print(f'{p_sec}: {os.getpid()} / {c_sec}: {psp.cpu_num()}')
    # Others, unknown
    else:
        print(f'{p_sec}: {os.getpid()} - unknown')
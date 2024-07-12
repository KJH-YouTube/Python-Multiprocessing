import platform, os
import psutil


def log_cpu_pid(p_sec, c_sec=None) -> None:
    # process section
    # core section
    
    os_system = platform.system()

    # Windows
    if os_system == 'Windows':
        print(f'{p_sec}: {os.getpid()}')
    # MacOS
    elif os_system == 'Darwin':
        print(f'{p_sec}: {os.getpid()}')
    # Linux
    elif os_system == 'Linux':
        psp = psutil.Process()
        print(f'{p_sec}: {os.getpid()} / {c_sec}: {psp.cpu_num()}')
    # Others, unknown
    else:
        print(f'{p_sec}: {os.getpid()} - unknown')
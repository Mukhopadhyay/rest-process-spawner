import time
import random
import datetime
import multiprocessing
from typing import Optional, List


def take_some_time(n: Optional[int]=10) -> None:
    time.sleep(n)
    print('took some time!')
    return


def get_random_value():
    return random.randint(1, 1000)


def get_dt(fmt: Optional[str]='%d-%m-%Y %H:%M:%S') -> str:
    return datetime.datetime.now().strftime(fmt)


def get_active_processes(proc: Optional[bool]=False) -> List[int]:
    proc = multiprocessing.active_children()
    if proc:
        return proc
    return [p.pid for p in proc]

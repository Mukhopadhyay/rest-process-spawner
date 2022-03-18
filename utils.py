import time
import datetime
from typing import Optional

def take_some_time(n: Optional[int] = 2):
    time.sleep(n)
    print('took some time!')
    return

def get_dt() -> str:
    return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

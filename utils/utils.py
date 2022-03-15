import time
from typing import Optional

def take_some_time(n: Optional[int] = 2):
    time.sleep(n)
    print('took some time!')
    return

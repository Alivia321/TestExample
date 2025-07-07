from datetime import datetime
from time import sleep


def square_job(arg1: int, delay: float = 0) -> None:
    print(f"{datetime.now()}\t[{arg1}] Square job start", flush=True)
    if delay > 0:
        sleep(delay)
    result = arg1 * arg1
    print(f"{datetime.now()}\t[{arg1}] Result: {result}", flush=True)
    print(f"{datetime.now()}\t[{arg1}] Square job complete", flush=True)

from time import time, sleep
from contextlib import contextmanager

class cm_timer_1:

    def __enter__(self):
        self.start = time()
        return

    def __exit__(self, *args):
        print("time:", time() - self.start)


@contextmanager
def cm_timer_2():
    start = time()
    yield
    print("time:", time() - start)


if __name__ == "__main__":
    with cm_timer_1():
        sleep(1.5)
    with cm_timer_2():
        sleep(1.5)
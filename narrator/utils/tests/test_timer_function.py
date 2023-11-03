import time

from narrator.utils.timer_function import ELAPSED_SECONDS, timer_func


@timer_func
def my_function():
    time.sleep(0.01)


def test_timer_function():
    my_function()
    assert len(ELAPSED_SECONDS) == 1
    assert round(ELAPSED_SECONDS[0], 2) == 0.01

# Schedule Library imported
import sched
import time

# Functions setup
s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)


print(time.time())

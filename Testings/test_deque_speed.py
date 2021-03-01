"""
Testing the runtime speed for lists and deque append, appendleft and pop
"""

import time
from collections import deque

def deque_speed_append(rounds: list) -> dict:
    results = {}
    for i in rounds:
        q = deque()
        start = time.time_ns()
        for n in range(i):
            q.append(n)
        end = time.time_ns()
        results[i] = end - start
    return results

def deque_speed_appendleft(rounds: list) -> dict:
    results = {}
    for i in rounds:
        q = deque()
        start = time.time_ns()
        for n in range(i):
            q.appendleft(n)
        end = time.time_ns()
        results[i] = end - start
    return results

def list_append_speed(rounds: list) -> dict:
    results = {}
    for i in rounds:
        s = []
        start = time.time_ns()
        for n in range(i):
            s.append(n)
        end = time.time_ns()
        results[i] = end - start
    return results

def deque_speed_pop(rounds: list) -> dict:
    results = {}
    for i in rounds:
        q = deque(m for m in range(i))
        start = time.time_ns()
        for n in range(i):
            q.pop()
        end = time.time_ns()
        results[i] = end - start
    return results

def deque_speed_popleft(rounds: list) -> dict:
    results = {}
    for i in rounds:
        q = deque(m for m in range(i))
        start = time.time_ns()
        for n in range(i):
            q.popleft()
        end = time.time_ns()
        results[i] = end - start
    return results

def list_speed_pop(rounds: list) -> dict:
    results = {}
    for i in rounds:
        s = [m for m in range(i)]
        start = time.time_ns()
        for n in range(i):
            s.pop()
        end = time.time_ns()
        results[i] = end - start
    return results

def list_comprehension(rounds: list) -> dict:
    results = {}
    for i in rounds:
        s = []
        start = time.time_ns()
        s.append(n for n in range(i))
        end = time.time_ns()
        results[i] = end - start
    return results

if __name__ == '__main__':
    print(f'deque append >> \t{deque_speed_append([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')
    print(f'deque appendleft >> \t{deque_speed_appendleft([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')
    print(f'list append >> \t\t{deque_speed_append([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')
    print('--------------------------------------')
    print(f'list comprehension >> \t{list_comprehension([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')
    print('--------------------------------------')
    print(f'deque pop >> \t\t{deque_speed_pop([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')
    print(f'deque popleft >> \t{deque_speed_popleft([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')
    print(f'list pop >> \t\t{list_speed_pop([100, 1000, 10000, 100000, 1000000, 10000000, 100000000])}')



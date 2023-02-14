import time
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
def memoized(n, cache = {}):
    if n in cache:
        return cache[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = memoized(n-1, cache) + memoized(n-2, cache)
        cache[n] = result
        return result
    
values = range(36)

times = {'func': [], 'memoized': []}

for n in values:
    start_time = time.time()
    func(n)
    end_time = time.time()
    times['func'].append(end_time - start_time)

    start_time = time.time()
    memoized(n)
    end_time = time.time()
    times['memoized'].append(end_time - start_time)

plt.plot(values, times['func'], label='func')
plt.plot(values, times['memoized'], label='memoized')
plt.legend()
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.show()
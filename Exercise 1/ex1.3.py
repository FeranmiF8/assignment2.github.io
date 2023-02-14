def func(n, cache = {}):
    if n in cache:
        return cache[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = func(n-1, cache) + func(n-2, cache)
        cache[n] = result
        return result
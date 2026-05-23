def caching_fibonacci(): #creating a fibonacci calculator with private cache
    cache = [0, 1]

    def fibonacci(n):
        if n <= 0:
            return 0

        if n < len(cache):
            return cache[n]

        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache.append(result)

        return result

    return fibonacci

fib = caching_fibonacci()
print(fib(6))
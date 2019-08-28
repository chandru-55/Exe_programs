def fibonacci(count):
    sequence = (0, 1)
    for _ in range(2, count):
        sequence += (reduce(lambda a, b: a + b, sequence[-2:]), )

    return sequence[:count]
    print(fibonacci(10))

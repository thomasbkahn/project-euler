def solution(n=4000000):
    """Computes sum of all even-valued Fibonacci terms that are less than n."""
    a, b, ans = 1, 2, 0
    while b < n:
        if b & 1 == 0:
            ans += b
        a, b = b, a + b
    return ans


def solution_2(n=4000000):
    """Computes sum of all even-valued Fibonacci terms that are less than n."""
    a, b, ans = 1, 2, 0
    while b < n:
        ans += b
        for i in range(3):
            a, b = b, a + b
    return ans


def solution_3(n=4000000):
    """Computes sum of all even-valued Fibonacci terms that are less than n."""
    return sum(even_fib_gen(n))


def solution_4(n=4000000):
    """Computes sum of all even-valued Fibonacci terms that are less than n."""
    return sum(even_fib_gen_2(n))


def even_fib_gen(n):
    """Generator for even-valued Fibonacci terms that are less than n."""
    a, b = 1, 2
    while b < n:
        if b & 1 == 0:
            yield b
        a, b = b, a + b


def even_fib_gen_2(n):
    """Generator for even-valued Fibonacci terms that are less than n."""
    a, b = 1, 2
    while b < n:
        yield b
        for i in range(3):
            a, b = b, a + b


if __name__ == '__main__':
    from timeit import timeit
    from math import log10

    print('Answer: {}'.format(solution()))

    t_elapsed = timeit('solution()',
                       setup='from __main__ import solution',
                       number=3) / 3

    if t_elapsed < 3:
        run_time  = 10
        n_iters   = int(run_time / t_elapsed)
        t_elapsed = timeit('solution()',
                           setup='from __main__ import solution',
                           number=n_iters) / n_iters

    exp = log10(t_elapsed)

    if exp > 0:
        t_string = '{:.3g} s'.format(t_elapsed)
    elif exp > -3:
        t_string = '{:.3g} ms'.format(t_elapsed * 1e3)
    elif exp > -6:
        t_string = '{:.3g} µs'.format(t_elapsed * 1e6)
    else:
        t_string = '{:.3g} ns'.format(t_elapsed * 1e9)

    print('Average Duration: ' + t_string)

def solution(a=3, b=5, n=1000):
    """Computes sum of all multiples of a or b that are less than n"""
    a_set = set(range(a, n, a))
    ans = sum(a_set.union(range(b, n, b)))
    return ans


if __name__ == '__main__':
    from timeit import timeit
    from math import log10

    print('Answer: {}'.format(solution()))

    t_elapsed = timeit('solution()',
                       setup='from __main__ import solution',
                       number=3) / 3
    n_iters  = 0
    run_time = 10

    if t_elapsed > 3:
        pass
    else:
        n_iters = int(run_time / t_elapsed)

    if n_iters:
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

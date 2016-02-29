from math import sqrt, log


phi = (1 + sqrt(5)) / 2


def solution(n=4000000):
    """Computes sum of all even-valued Fibonacci terms that are less than n."""
    max_n = max_index(n)
    max_n = (max_n - 3) // 3
    term_1 = (phi ** 3) * geo_sum(phi ** 3, max_n)
    term_2 = ((1 - phi) ** 3) * geo_sum((1 - phi) ** 3, max_n)
    ans = (term_1 - term_2) / sqrt(5)
    return int(round(ans, 0))


def max_index(val):
    """Computes maximum index of Fibonacci sequence that is less than val."""
    return int(log(sqrt(5) * val, phi))


def geo_sum(r, n):
    """Computes sum of geometric series r**ni from 0 to n."""
    return (1 - (r ** (n + 1))) / (1 - r)


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

#include <stdio.h>
#include <math.h>
#include <sys/time.h>

unsigned long solution(unsigned long n=4000000) {

    unsigned long a   = 1;
    unsigned long b   = 2;
    unsigned long tmp = 0;
    unsigned long ans = 0;

    while (b < n) {

        if (!(b & 1)) {
            ans += b;
        }

        tmp = a;
        a   = b;
        b  += tmp;

    }

    return ans;
}

unsigned long solution_2(unsigned long n=4000000) {

    unsigned long a   = 1;
    unsigned long b   = 2;
    unsigned long tmp = 0;
    unsigned long ans = 0;

    while (b < n) {

        ans += b;

        for (short i = 0; i < 3; i++) {
            tmp = a;
            a   = b;
            b  += tmp;
        }

    }

    return ans;
}

//////////////////////////////////////////////////

typedef unsigned long long timestamp_t;

static timestamp_t

get_timestamp () {
  struct timeval now;
  gettimeofday (&now, NULL);
  return  now.tv_usec + (timestamp_t)now.tv_sec * 1000000;
}

int main() {

    printf("Answer: %lu\n", solution());

    timestamp_t t0 = get_timestamp();

    for (int i = 0; i < 3; ++i) {
        solution();
    }

    timestamp_t t1 = get_timestamp();

    double t_elapsed = (t1 - t0) / 1000000.0L / 3;

    if (t_elapsed < 3) {
         int run_time = 10;
         unsigned long long n_iters = run_time / t_elapsed;

         timestamp_t t0 = get_timestamp();

         for (int i = 0; i < n_iters; ++i) {
             solution();
         }

         timestamp_t t1 = get_timestamp();
         t_elapsed = (t1 - t0) / 1000000.0L / n_iters;
    }

    double exp_t = log10(t_elapsed);

    if (exp_t > 0) {
        printf("Average Duration: %.3g s\n", t_elapsed);
    } else if (exp_t > -3) {
        printf("Average Duration: %.3Lg ms\n", t_elapsed * 1000.0L);
    } else if (exp_t > -6) {
        printf("Average Duration: %.3Lg µs\n", t_elapsed * 1000000.0L);
    } else {
        printf("Average Duration: %.3Lg ns\n", t_elapsed * 1000000000.0L);
    }

    return 0;
}

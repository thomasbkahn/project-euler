function solution(n=4000000)
    a, b, ans = 1, 2, 0
    while b < n
        ans += b
        for i = 1:3
            a, b = b, a + b
        end
    end
    ans
end

function solution_2(n=4000000)
    a, b, ans = 1, 2, 0
    while b < n
        if (b % 2 == 0)
            ans += b
        end
        a, b = b, a + b
    end
    ans
end

function solution_3(n=4000000)
    reduce(+, even_fib_gen_2(n))
end

function solution_4(n=4000000)
    reduce(+, even_fib_gen(n))
end

function even_fib_gen(n)
    function _it()
        a, b = 1, 2
        while b < n
            produce(b)
            for i = 1:3
                a, b = b, a + b
            end
        end
    end
    Task(_it)
end

function even_fib_gen_2(n)
    function _it()
        a, b = 1, 2
        while b < n
            if b % 2 == 0
                produce(b)
            end
            a, b = b, a + b
        end
    end
    Task(_it)
end

##################################################

println("Answer: $(solution())")

time_arr = zeros(3)

for i = 1:3
  time_arr[i] = @elapsed solution()
end

t_elapsed = mean(time_arr)

if t_elapsed < 3
    run_time = 10
    n_iters  = round(Int, run_time / t_elapsed)
    time_arr = zeros(n_iters)
    for i = 1:n_iters
        time_arr[i] = @elapsed solution()
    end
    t_elapsed = mean(time_arr)
end

exp = log10(t_elapsed)

if exp > 0
    t_string = @sprintf "%.3g s" t_elapsed
elseif exp > -3
    t_string = @sprintf "%.3g ms" t_elapsed * 1e3
elseif exp > -6
    t_string = @sprintf "%.3g µs" t_elapsed * 1e6
else
    t_string = @sprintf "%.3g ns" t_elapsed * 1e9
end

println("Average Duration: $t_string")

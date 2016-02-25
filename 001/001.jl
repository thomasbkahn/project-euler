function solution(a=3, b=5, n=1000)
    sum(union(a:a:n-1, b:b:n-1))
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

function evaluate()

    printf('Answer: %d\n', solution());

    time_arr = zeros(3, 1);

    for i = 1:3
        tic(); solution(); ti = toc();
        time_arr(i) = ti;
    end

    t_elapsed = mean(time_arr);

    if t_elapsed < 3
        run_time = 10;
        n_iters  = round(run_time / t_elapsed);
        time_arr = zeros(n_iters, 1);
        for i = 1:n_iters
            tic(); solution(); ti = toc();
            time_arr(i) = ti;
        end
    end

    t_elapsed = mean(time_arr);
    exp_t = log10(t_elapsed);

    if exp_t > 0
        t_string = sprintf("%.3g s", t_elapsed);
    elseif exp_t > -3
        t_string = sprintf("%.3g ms", t_elapsed * 1e3);
    elseif exp_t > -6
        t_string = sprintf("%.3g µs", t_elapsed * 1e6);
    else
        t_string = sprintf("%.3g ns", t_elapsed * 1e9);
    end

    printf("Average Duration: %s\n", t_string);

end

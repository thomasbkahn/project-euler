function answer = solution(a, b, n)

    if ~exist('a', 'var')
        a = 3;
    end

    if ~exist('b', 'var')
        b = 5;
    end

    if ~exist('n', 'var')
        n = 1000;
    end

    answer = sum(union(a:a:n-1, b:b:n-1));

end

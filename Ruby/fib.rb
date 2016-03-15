def fib(c, x = 1, y = 1)
    n = [x, y]
    for i in 3..c
        n.push(n[-1] + n[-2])
    end
    return n[0..c-1]
end
puts fib(5)

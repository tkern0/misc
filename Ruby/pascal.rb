def pascal(n)
    pa = [[1], [1, 1]]
    for i in 1..n - 1
        x = [1]
        for j in 0..pa[-2].length
            j == pa[-2].length ? (x.push(1)) : (x.push(pa[-1][j] + pa[-1][j + 1]))
        end
        pa.push(x)
    end
    return pa[0..n]
end

for i in pascal(5); p i; end

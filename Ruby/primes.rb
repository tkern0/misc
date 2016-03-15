def is_prime(n)
    for i in 2..Math.sqrt(n).ceil
        return false if n % i == 0
    end
    n > 1
end
for i in 1..100
    puts i if is_prime(i)
end

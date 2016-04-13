function is_prime(n)
    for i = 2, math.ceil(math.sqrt(n)) do
        if n % i ==0 then
            return false
        end
    end
    if n > 1 then
        return true
    end
end

for i = 1, 100 do
    if is_prime(i) then
        print(i)
    end
end

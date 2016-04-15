function printable_array(array, showkeys)
    showkeys = showkeys or false
    str = "{"
    for k, v in pairs(array) do
        if type(k) == "table" then
            k = printable_array(k, showkeys)
        end
        if type(v) == "table" then
            v = printable_array(v, showkeys)
        end
        if showkeys == true then
            str = str..k..": "..v..", "
        else
            str = str..v..", "
        end
    end
    return string.sub(str, 1, -3).."}"
end

function pascal(n)
    t = {{1}, {1, 1}}
    for i = 1, n - 1 do
        x = {1}
        for j = 1, #t[#t - 1] do
            if j == #t[#t - 1] then
                x[#x + 1] = 1
            else
                x[#x + 1] = t[#t - 1][j] + t[#t - 1][j + 1]
            end
        end
        t[#t + 1] = x
    end
    return t
end

print(printable_array({{1, 2}}))

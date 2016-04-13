function splitString(str)
    ltr = {}
    for i = 1, string.len(str) do
        ltr[#ltr + 1] = string.sub(str, i, i)
    end
    return ltr
end

function lookSay(num, rl, times)
    for i = 1, times or 1 do
        snum = {}
        for i = 1, string.len(num) do
            snum[#snum + 1] = string.sub(num, i, i)
        end
        count = 0
        lvalue = snum[1]
        nnum = {}
        for k, v in ipairs(snum) do
            if v == lvalue then
                count = count + 1
            else
                nnum[#nnum + 1] = count .. lvalue
                count = 1
            end
            lvalue = v
        end
        nnum[#nnum + 1] = count .. lvalue
        nvalue = ""
        for k, v in ipairs(nnum) do
            nvalue = nvalue .. v
        end
        num = nvalue
    end
    if rl then
        return num
    else
        return string.len(num)
    end
end

print(lookSay(1, true, 2))

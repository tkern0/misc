def look_and_say(n)
    combo = 1
    newNum = ""
    for i in 0..n - 1 do
        if n[i] == n[i + 1] then
            combo += 1
        else
            newNum += combo.to_s + n[i].to_s
            combo = 1
        end
    end
    newNum += combo.to_s + n[i - 1].to_s
    combo = 1
    return newNum
end

p look_and_say(12)
# "202190"
# what

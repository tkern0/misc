def look_and_say(n)
    combo = 1
    newNum = ""
    for i in 0..n.length - 1 do
        if n[i] == n[i + 1] then
            combo += 1
        else
            newNum += combo.to_s + n[i].to_s
            combo = 1
        end
    end
    return newNum
end

p look_and_say("3112")
# "202190"
# what

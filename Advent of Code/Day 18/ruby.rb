$size = 6
$steps = 1
$path = "Advent of Code/Day 18/test.txt"

def format_input(startState)
    state = Hash.new(nil)
    for x in 0..$size + 1
        for y in 0..$size + 1
            state[[x, y]]
        end
    end
    return state
end

state = format_input(File.open($path))
file = File.open($path).readlines
p file

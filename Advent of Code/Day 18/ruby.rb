steps = 1
file = File.open("Advent of Code/Day 18/test.txt").readlines
$size = file.length

# Turns input into hash array with empty border
def format_input(startState)
    state = Hash.new(false)
    for y in 0..$size - 1 # Because it goes line by line "y" comes first here
        for x in 0..$size - 1
            state[[x + 1, y + 1]] = true if startState[y].split("")[x] == "#"
        end
    end
    return state
end

# Formats hash array the same way as input
def format_state(state)
    formated = ""
    for y in 1..$size # Builds line by line, so "y" comes first
        for x in 1..$size
            state[[x, y]]? (formated << "#") : (formated << ".")
        end
        formated << "\n"
    end
    return formated
end

# Counts how many neighbours are "true"
def get_neighbours(x, y, state)
    count = 0
    for ix in x - 1..x + 1
        for iy in y - 1..y + 1
            count += 1 if state[[ix, iy]] and not (ix == x and iy == y)
        end
    end
    return count
end

# Advances "state" by one step each time it is called
def advance(state)
    newState = Hash.new(false)
    for x in 1..$size
        for y in 1..$size
            neighbours = get_neighbours(x, y, state)
            if state[[x, y]]
                newState[[x, y]] = true if neighbours == 2 or neighbours == 3
            else
                newState[[x, y]] = true if neighbours == 3
            end
        end
    end
end

def count_true(state)
    count = 0
    state.each do |key, value|
        count += 1 if value
    end
    return count
end

state = format_input(file)

p count_true(state)
puts format_state(state)

for _ in 1..steps
    state = advance(state)
end

p count_true(state)
puts format_state(state)

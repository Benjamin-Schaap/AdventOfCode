
def IncreasingDepthsPart1():

    file = open("input.txt")

    depths = []

    # the values are read in with newline characters, remove them by casting them to ints
    for value in file.readlines():
        depths.append(int(value))

    prev = depths[0]

    output = 0

    for i in range(1, len(depths)):

        if depths[i] > prev:
            output += 1
        
        prev = depths[i]

    return output

def IncreasingDepthsPart2():

    file = open("input.txt")

    depths = []

    # the values are read in with newline characters, remove them by casting them to ints
    for value in file.readlines():
        depths.append(int(value))

    prev = sum(depths[:2])
    output = 0

    for i in range(1, len(depths) - 2):

        if sum(depths[i:i+3]) > prev:
            output += 1
        
        prev = sum(depths[i:i+3])


    return output

print(IncreasingDepthsPart1())
print(IncreasingDepthsPart2())
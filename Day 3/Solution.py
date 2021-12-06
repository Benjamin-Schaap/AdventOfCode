def LoadInput(fileName):

    file = open(fileName)

    binaryValues = [value.strip() for value in file.readlines()]

    file.close()

    return binaryValues

def FormatInputForTask1(input):

    lines = [None] * len(input[0])

    for index in range(len(lines)):

        lines[index] = [0,0]

    for value in input:

        for index in range(len(lines)):

            match value[index]:
                case "0":
                    lines[index][0] += 1
                case "1":
                    lines[index][1] += 1

    return lines

# In hindsight, if I had known part 2 was going to be so annoying, I would have just calculated the gamma and epsilon values in 'FormatInput' since I'd only need to traverse the input once with no extra space. Oh well :/ 
def PowerConsumption(input):

    gamma = ""
    epsilon = ""

    for zeros, ones in input:

        if zeros > ones:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"


    print("Gamma: ", gamma)
    print("Epsilon: ", epsilon)
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print("Power Consumption: ", gamma * epsilon)

def CalculateOxygenGeneratorRating(input):
    values = input
    
    for index in range(len(input[0]) + 1):

        StartsWith1 = []
        StartsWith0 = []

        countOf1s = 0
        countOf0s = 0

        if len(values) == 1:
            return str(values[0])
        else:
            for value in values:

                match value[index]:
                    case "1":
                        countOf1s += 1
                        StartsWith1.append(value[:])
                    case "0":
                        countOf0s += 1
                        StartsWith0.append(value[:])
            
            if countOf1s >= countOf0s:
                values = StartsWith1[:]
            else:
                values = StartsWith0[:]

    return -1

def CalculateCO2ScrubberRating(input):
    values = input
    
    for index in range(len(input[0]) + 1):

        StartsWith1 = []
        StartsWith0 = []

        countOf1s = 0
        countOf0s = 0

        if len(values) == 1:
            return str(values[0])
        else:
            for value in values:

                match value[index]:
                    case "1":
                        countOf1s += 1
                        StartsWith1.append(value[:])
                    case "0":
                        countOf0s += 1
                        StartsWith0.append(value[:])
            
            if countOf1s < countOf0s:
                values = StartsWith1[:]
            else:
                values = StartsWith0[:]

    return -1

def CalculateLifeSupportRating(input):

    OxygenRating = CalculateOxygenGeneratorRating(input)
    CO2Rating = CalculateCO2ScrubberRating(input)

    print("Oxygen Rating: ", OxygenRating, int(OxygenRating, 2))
    print("CO2 Rating: ", CO2Rating, int(CO2Rating, 2))

    OxygenRating = int(OxygenRating, 2)
    CO2Rating = int(CO2Rating, 2)
    print("Life Support Rating: ", OxygenRating * CO2Rating)


input = LoadInput("input.txt")
PowerConsumption(FormatInputForTask1(input))
print("- - - - - - - - - - - - - -")
CalculateLifeSupportRating(input)
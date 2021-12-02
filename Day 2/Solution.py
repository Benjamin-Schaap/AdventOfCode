from enum import Enum
from typing import Match

class CommandType(str, Enum):
    Forward = 'forward'
    Down    = 'down'
    Up      = 'up'

class Solution:

    def __init__(self, fileLocation):

        # read in commands/directions
        input = open(fileLocation)
        instructions = [line.split() for line in input.readlines()]
        self.commands = [(command, int(value)) for command, value in instructions]

    def NavigatePart1(self):

        distance = 0
        depth = 0

        # 1746616
        # 1741971043
        
        for command, value in self.commands:
            match command:
                case CommandType.Forward:
                    distance += value
                case CommandType.Up:
                    depth -= value
                case CommandType.Down:
                    depth += value
        
        return distance * depth

    def NavigatePart2(self):

        distance = 0
        depth = 0
        aim = 0
        
        for command, value in self.commands:
            match command:
                case CommandType.Forward:
                    distance += value
                    depth += value * aim
                case CommandType.Up:
                    aim -= value
                case CommandType.Down:
                    aim += value
        
        return distance * depth

solution = Solution("input.txt")
print(solution.NavigatePart1())
print(solution.NavigatePart2())
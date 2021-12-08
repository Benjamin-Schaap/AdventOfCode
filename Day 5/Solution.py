class NavigateVents:

    def __init__(self):
        self.lines = []
        self.seen_coordinates = set()
        self.large_coordinates = set()

    def LoadInput(self, fileName):

        file = open(fileName)

        lines = file.readlines()

        line_coordinates = []

        for line in lines:

            chunk = line.split()

            left_coordinate = [int(c) for c in chunk[0].strip().split(",")]
            right_coordinate = [int(c) for c in chunk[2].strip().split(",")]

            line_coordinates.append(((left_coordinate[0], left_coordinate[1]), (right_coordinate[0], right_coordinate[1])))
        
        self.lines = line_coordinates

    def NavigateHydroThermalVentsPt1(self):

        self.seen_coordinates = set()
        self.large_coordinates = set()

        for line in self.lines:

            left, right = line[0], line[1]

            # check to see if we are drawing a row
            if left[0] == right[0]:

                x_coordinate = left[0]

                for y_coordinate in range(min(left[1], right[1]), max(right[1], left[1]) + 1):

                    if (x_coordinate, y_coordinate) in self.seen_coordinates:
                        
                        if (x_coordinate, y_coordinate) not in self.large_coordinates:
                            self.large_coordinates.add((x_coordinate, y_coordinate))
                    else:
                        self.seen_coordinates.add((x_coordinate, y_coordinate))
            
            # check to see if we are drawing a column
            if left[1] == right[1]:

                y_coordinate = left[1]

                for x_coordinate in range(min(left[0], right[0]), max(right[0], left[0]) + 1):

                    if (x_coordinate, y_coordinate) in self.seen_coordinates:
                        
                        if (x_coordinate, y_coordinate) not in self.large_coordinates:
                            self.large_coordinates.add((x_coordinate, y_coordinate))
                    else:
                        self.seen_coordinates.add((x_coordinate, y_coordinate))
        
        print(len(self.large_coordinates))

    def NavigateHydroThermalVentsPt2(self):

        self.seen_coordinates = set()
        self.large_coordinates = set()

        for line in self.lines:

            left, right = line[0], line[1]

            # check to see if we are drawing a horizontal line
            if left[0] == right[0]:

                x_coordinate = left[0]

                for y_coordinate in range(min(left[1], right[1]), max(right[1], left[1]) + 1):

                    if (x_coordinate, y_coordinate) in self.seen_coordinates:
                        
                        if (x_coordinate, y_coordinate) not in self.large_coordinates:
                            self.large_coordinates.add((x_coordinate, y_coordinate))
                    else:
                        self.seen_coordinates.add((x_coordinate, y_coordinate))
            
            # check to see if we are drawing a vertical line
            if left[1] == right[1]:

                y_coordinate = left[1]

                for x_coordinate in range(min(left[0], right[0]), max(right[0], left[0]) + 1):

                    if (x_coordinate, y_coordinate) in self.seen_coordinates:
                        
                        if (x_coordinate, y_coordinate) not in self.large_coordinates:
                            self.large_coordinates.add((x_coordinate, y_coordinate))
                    else:
                        self.seen_coordinates.add((x_coordinate, y_coordinate))
        
            # check to see if we are drawing a diagonal line
            if abs(left[0] - right[0]) == abs(left[1] - right[1]):

                distance = abs(left[1] - right[1])

                for index in range(distance + 1):

                        y_coordinate = None

                        smallest_y = min(left[1], right[1])
                        smallest_x = min(left[0], right[0])

                        # essentially what we're asking here is "Is my smallest y value paired with my smallest x value?"
                        # if it is, then we will raise y by index, otherwise they are inversed and I need to decrease y while still raising x.
                        if (smallest_x, smallest_y) == left or (smallest_x, smallest_y) == right:
                            y_coordinate = min(left[1], right[1]) + index
                        else:
                            y_coordinate = max(left[1], right[1]) - index

                        x_coordinate = min(left[0], right[0]) + index

                        if (x_coordinate, y_coordinate) in self.seen_coordinates:
                        
                            if (x_coordinate, y_coordinate) not in self.large_coordinates:
                                self.large_coordinates.add((x_coordinate, y_coordinate))
                        else:
                            self.seen_coordinates.add((x_coordinate, y_coordinate))
     
        print(len(self.large_coordinates))





navigator = NavigateVents()
navigator.LoadInput("input.txt")
navigator.NavigateHydroThermalVentsPt1()
navigator.NavigateHydroThermalVentsPt2()
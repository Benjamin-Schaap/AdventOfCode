from heapq import nlargest
from operator import itemgetter

# yeesh not proud of this one

class Bingo():

    def __init__(self):
        self.picks = []
        self.boards = {}
        self.board_scores = []
        print("Bingo Board Initialized")
    
    def LoadData(self, fileName):
        file = open(fileName)

        lines = file.readlines()

        dictionary_key = -1
        for index, line in enumerate(lines):

            if index == 0:
                self.picks = line.strip().split(",")
            else:

                line = line.strip()
                row = [(r, False) for r in line.split()]

                if line == "":
                    dictionary_key += 1
                    self.boards[dictionary_key] = []
                else:
                    self.boards[dictionary_key].append(row)

    def isWinningRowChoice(self, boardNumber, rowIndex, columnIndex):

        rowCheck = self.boards[boardNumber][rowIndex]

        isValidRow = True

        # if the 'choice' is False, it means we haven't placed on it yet and it isn't a winning row
        for number, choice in rowCheck:
            
            if not choice:
                isValidRow = False
                break
        
        if isValidRow:
            return True

        colCheck = []
        isValidCol = True

        for row in range(len(self.boards[boardNumber])):
            if not self.boards[boardNumber][row][columnIndex][1]:
                isValidCol = False
                break
                
            colCheck.append(self.boards[boardNumber][row][columnIndex])
        
        if isValidCol:
            return True
        
        return False

    def CalculateBoardScore(self, boardIndex, lastPick):

        # Now calculate the winning score
        unmarkedSum = 0

        for rowIndex in range(len(self.boards[boardIndex])):

            for colIndex in range(len(self.boards[0])):

                if not self.boards[boardIndex][rowIndex][colIndex][1]:
                    unmarkedSum += int(self.boards[boardIndex][rowIndex][colIndex][0])

        print("Result: ", int(lastPick) * unmarkedSum)
    
    def WinningBingoScorePt1(self):

        fastestWin = float('inf') # fastestWin is the number if picks before the game was won. 
        fastestBoardIndex = None
        lastChoiceFastestBoard = None

        for boardNumber, board in self.boards.items():

            lastChoice = None
            picks = 0
            doneCounting = False

            for numberCalledIndex in range(len(self.picks)):

                numberCalled = self.picks[numberCalledIndex]

            
                # runtime is not great on this method due to the fact that we access every element in every board. This could be sped up to cancel out of the board the second it wins.
                # big O runtime is still O(B * M * N) with M being the rows, N being the columns, and B being the number of boards.
                for rowIndex in range(len(board)):

                    for colIndex in range(len(board[0])):


                        if not doneCounting:
                            if board[rowIndex][colIndex][0] == str(numberCalled):
                                lastChoice = numberCalled

                                board[rowIndex][colIndex] = (lastChoice, True)

                                if self.isWinningRowChoice(boardNumber, rowIndex, colIndex):

                                    # stop counting for this particular board number, we just found the best option for it
                                    doneCounting = True

                                    self.board_scores.append((picks, boardNumber, lastChoice))

                                    if picks < fastestWin:
                                        fastestWin = picks
                                        fastestBoardIndex = boardNumber
                                        lastChoiceFastestBoard = lastChoice
                picks += 1
        print(" - - - - - - - - - - - - - - - - - - - - -")
        print("Winning Board")
        print("FastestBoardIndex: ", fastestBoardIndex + 1)
        print("Number of Picks: ", fastestWin)
        print("Last choice: ", lastChoiceFastestBoard)
        self.CalculateBoardScore(fastestBoardIndex, lastChoiceFastestBoard)

    def LosingBingo(self):
        print(" - - - - - - - - - - - - - - - - - - - - -")
        print("Losing Board")

        # building off of our caching in part one, simple get the largest element in the list, which we will convert to a max heap.
        # use the 'picks' field to get the worst win
        # self.board_scores.append((picks, boardNumber, lastChoice))
        worstWin = nlargest(1, self.board_scores, key=itemgetter(0))
        self.CalculateBoardScore(worstWin[0][1], worstWin[0][2])

        




bingo_game = Bingo()
bingo_game.LoadData("input.txt")
bingo_game.WinningBingoScorePt1()
bingo_game.LosingBingo()
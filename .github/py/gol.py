# Filename=CGOL.py
#Kirk Martin
#CSCI 77800 Fall 2022
# .
class Cgol :
    
    @staticmethod
    def  createNewBoard( r,  c) :
        board = [[' '] * (c) for _ in range(r)]
        rows = len(board)
        cols = len(board[0])
        i = 0
        while (i < rows) :
            j = 0
            while (j < cols) :
                board[i][j] = '.'
                j += 1
            i += 1
        return board
    
    @staticmethod
    def printBoard( board) :
        rows = len(board)
        cols = len(board[0])
        i = 0
        while (i < rows) :
            j = 0
            while (j < cols) :
                print(str(board[i][j]) + " ", end ="")
                j += 1
            print()
            i += 1
    # this should set cell (r,c) to val
    
    @staticmethod
    def setCell( board,  r,  c,  val) :
        board[r][c] = val
    # this should return number of living neigbours of board[r][c]
    @staticmethod
    def  countNeighbours( board,  r,  c) :
        count = 0
        i = r - 1
        while (i < r + 2) :
            j = c - 1
            while (j < c + 2) :
                if (i > -1 and i < len(board) and not (r == i and c == j) and j > -1 and j < len(board[0]) and board[i][j] == 'X') :
                    # Case sensitive!!!
                    count += 1
                j += 1
            i += 1
        return count
    # This should do the pre condition and post conditionsad ' ')
    @staticmethod
    def  getNextGenCell( board,  r,  c) :
        neighbors = Cgol.countNeighbours(board, r, c)
        if (board[r][c] == 'X' and (neighbors == 2 or neighbors == 3)) :
            return 'X'
        if (board[r][c] == '.' and neighbors == 3) :
            return 'X'
        return '.'
    # This should create and return a new board 
    @staticmethod
    def  generateNextBoard( board) :
        rows = len(board)
        cols = len(board[0])
        newBoard = [[' '] * (cols) for _ in range(rows)]
        # Note: In order to have modifications not affect results you have to create a newBoard so that you DON'T lose original data (because you want results to be simultaneous)
        i = 0
        while (i < rows) :
            j = 0
            while (j < cols) :
                newBoard[i][j] = Cgol.getNextGenCell(board, i, j)
                j += 1
            i += 1
        return newBoard
    @staticmethod
    def main( args) :
        board = None
        board = Cgol.createNewBoard(10, 10)
        # breathe life into some cells:
        Cgol.setCell(board, 0, 0, 'X')
        Cgol.setCell(board, 0, 2, 'X')
        Cgol.setCell(board, 1, 1, 'X')
        Cgol.setCell(board, 2, 0, 'X')
        # TASK:
        # Once your initial version is running,
        # try out different starting configurations of living cells...
        # (Feel free to comment out the above three lines.)
        print("Gen X:")
        Cgol.printBoard(board)
        print("--------------------------\n\n")
        print("Cell (1,1) has " + str(Cgol.countNeighbours(board, 1, 1)) + " neighbors")
        # TEST
        print("Cell (1,1) has the new state of  " + str(Cgol.getNextGenCell(board, 1, 1)) + " \t.")
        # TEST
        board = Cgol.generateNextBoard(board)
        print("Gen X+1:")
        Cgol.printBoard(board)
        print("--------------------------\n\n")
        board = Cgol.generateNextBoard(board)
        print("Gen X+2:")
        Cgol.printBoard(board)
        print("--------------------------\n\n")
    

if __name__=="__main__":
    Cgol.main([])

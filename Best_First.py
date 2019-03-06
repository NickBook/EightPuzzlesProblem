class PuzzleNode_Best_First():
    def __init__(self,parent,grid):
        self.grid = grid
        self.h_cost = 0
    
    def clone_puzzle(self):
        '''
        Clone the current node and return a new node. Copies
        over existing grid tile by tile, increases depth, and
        sets parent to self.
        '''
        new_puzzle_node = PuzzleNode_Best_First(self,[])
        for i in range(len(self.grid)):
            new_puzzle_node.grid.append([])
            for j in range(len(self.grid[i])):
                new_puzzle_node.grid[i].append(self.grid[i][j])
        return new_puzzle_node


class Best_First():
    def __init__(self):
        def __init__(self):
        self.SOLVED = [['1','2','3'], ['8','','4'], ['7','6','5']]
        self.open = []
        self.close = []
        self.summary = ''

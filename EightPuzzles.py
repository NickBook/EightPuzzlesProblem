import math, random

class EightPuzzlesGrid():
    '''
    A grid holds a 3x3 grid, stores iteration number, and
    stores the algorithm type
    '''
    
    def __init__(self, alg_name):
        '''
        Generates a random 3x3 grid
        '''
        GRID_ENTRIES = ['','1','2','3','4','5','6','7','8']
        self.grid_arr = []

        for i in range(3):
            self.grid_arr.append([])
            for j in range(3):
                self.grid_arr[i].append(GRID_ENTRIES[random.randint(0,len(GRID_ENTRIES)-1)])
                GRID_ENTRIES.remove(self.grid_arr[i][j])

        self.iteration =  0
        self.algorithm = alg_name

    def iterate(self):
        # To be implemented in each algorithm.
        pass
from random import randint

class PuzzleNode_A_Star():
    def __init__(self,parent,grid):
        self.grid = grid
        self.parent = parent
        self.h_cost = 0
        if(self.parent == None):
            self.depth = 0
        else:
            self.depth = self.parent.depth
    
    def clone_puzzle(self):
        '''
        Clone the current node and return a new node. Copies
        over existing grid tile by tile, increases depth, and
        sets parent to self.
        '''
        new_puzzle_node = PuzzleNode_A_Star(self,[])
        new_puzzle_node.depth = self.depth + 1
        for i in range(len(self.grid)):
            new_puzzle_node.grid.append([])
            for j in range(len(self.grid[i])):
                new_puzzle_node.grid[i].append(self.grid[i][j])
        return new_puzzle_node


class A_Star():
    def __init__(self):
        self.SOLVED = [['1','2','3'], ['8','','4'], ['7','6','5']]
        self.open = []
        self.close = []
        self.summary = ''
        self.root_puzzle_node = PuzzleNode_A_Star(None,[])
        self.assign_random_puzzle(self.root_puzzle_node)

    
    def solve_puzzle(self):
        '''
        Solve the eight puzzle problem by using the A* searching
        algorithm with depth and heuristic evaluation function.
        '''
        self.root_puzzle_node.depth = 0
        self.root_puzzle_node.h_cost = self.h_cost(self.root_puzzle_node)
        self.open.append(self.root_puzzle_node)

        while(not self.is_solved(self.open[0])):
            node_to_expand = self.open[0]
            self.open.remove(node_to_expand)
            self.close.append(node_to_expand)

            up_node = self.up_operation(node_to_expand.clone_puzzle())
            down_node = self.down_operation(node_to_expand.clone_puzzle())
            left_node = self.left_operation(node_to_expand.clone_puzzle())
            right_node = self.right_operation(node_to_expand.clone_puzzle())

            possible_moves = []
            possible_moves.append(up_node)
            possible_moves.append(down_node)
            possible_moves.append(left_node)
            possible_moves.append(right_node)

            for move in possible_moves:
                if(move != None):
                    move.h_cost = self.h_cost(move)
                    f_cost = move.depth + move.h_cost

                    open_index = self.is_node_in_list(move,self.open)
                    closed_index = self.is_node_in_list(move,self.close)
                    if(open_index == -1 and closed_index == -1):
                        self.open.append(move)
                    elif(open_index > -1):
                        existing_puzzle = self.open[open_index]
                        existing_f_cost = existing_puzzle.depth + existing_puzzle.h_cost
                        if(existing_f_cost > f_cost):
                            self.open[open_index] = move
                            
            self.open = sorted(self.open, key=lambda node: node.depth + node.h_cost)

        print('Solved with A*')
        print(self.open[0].grid[0])
        print(self.open[0].grid[1])
        print(self.open[0].grid[2])
        self.summary = 'The A* algorithm touched {} different game states before finding the solution. The solution can be reached in {} moves'.format(str(len(self.close)), str(self.open[0].depth-1))
        
        print("Depth was " + str(self.open[0].depth))
        return self.trace_back_path(self.open[0])


    def trace_back_path(self,solution_node):
        '''
        Generates the path traveled to get to the
        goal node. Adds the parent of each node to the
        moves array until parent is null.
        '''
        count_moves = 0
        moves = []
        while(solution_node.parent != None):
            count_moves += 1
            moves.append(solution_node.grid)
            solution_node = solution_node.parent
        moves.reverse()
        return moves


    def is_node_in_list(self,puzzle_node,some_list):
        '''
        some_list is a list of Nodes and puzzle_node is the search
        node. Returns false if the search grid is not in the 
        list, true otherwise
        '''
        for item in some_list:
            item_grid = item.grid
            found = True
            for i in range(len(item_grid)):
                for j in range(len(item_grid[i])):
                    if(puzzle_node.grid[i][j] != item_grid[i][j]):
                        found = False
            if(found):
                return some_list.index(item) 
        return -1


    def h_cost(self, puzzle_node):
        '''
        Define h_cost as the sum of the distances
        each tile is from the goal state.
        '''
        cost = 0
        if(puzzle_node == None):
            return 100
        for i in range(len(puzzle_node.grid)):
            for j in range(len(puzzle_node.grid[i])):
                tile = puzzle_node.grid[i][j]
                goal_spot = self.goal_index_of_tile(tile)
                cost += abs(goal_spot[1]-j)
                cost += abs(goal_spot[0]-i)
        return cost
    
    
    def assign_random_puzzle(self,puzzle_node):
        '''
        Takes in a puzzle node and assigns a random grid. Since some grids
        aren't solveable, it starts with the solution and then randomly moves
        around tiles a random number of times.
        '''
        randint
        puzzle_node.grid = [['1','2','3'], ['8','','4'], ['7','6','5']]
        for i in range(randint(15,100)):
            up_node = self.up_operation(puzzle_node.clone_puzzle())
            down_node = self.down_operation(puzzle_node.clone_puzzle())
            left_node = self.left_operation(puzzle_node.clone_puzzle())
            right_node = self.right_operation(puzzle_node.clone_puzzle())

            possible_moves = []
            if(up_node != None):
                possible_moves.append(up_node)
            if(down_node != None):
                possible_moves.append(down_node)
            if(left_node != None):
                possible_moves.append(left_node)
            if(right_node != None):
                possible_moves.append(right_node)

            move = randint(0,len(possible_moves)-1)
            puzzle_node.grid = possible_moves[move].grid
        puzzle_node.depth = 0



    def index_of_free_spot(self,puzzle_node):
        '''
        Returns a tuple (x,y) of the index of the open
        spot in the grid.
        '''
        for i in range(len(puzzle_node.grid)):
            for j in range(len(puzzle_node.grid[i])):
                if puzzle_node.grid[i][j] == '':
                    return (i,j)  # Return tuple of index
        return None # Invalid grid if None...

    
    def goal_index_of_tile(self, tile):
        '''
        Returns a tuple (x,y) of the index of the tile
        where it is supposed to be (goal spot).
        '''
        for i in range(len(self.SOLVED)):
            for j in range(len(self.SOLVED[i])):
                if self.SOLVED[i][j] == tile:
                    return (i,j)  # Return tuple of index
        return (-1,-1) # Invalid grid if not found


    def swap_tiles(self,r1,c1,r2,c2,puzzle_node):
        '''
        Swaps the r1,c1 tile with the r2,c2 tile of the 
        new_puzzle. Note that this acts like pass by reference
        in c++ where new_puzzle's grid_arr is changed where 
        it is called. 
        '''
        tmp = puzzle_node.grid[r1][c1]
        puzzle_node.grid[r1][c1] = puzzle_node.grid[r2][c2]
        puzzle_node.grid[r2][c2] = tmp


    def up_operation(self,puzzle_node):
        '''
        Swaps the free spot with the tile above. If there is
        no tile above, then None, else return the swapped puzzle_node.
        Note that this will change puzzle_node (pass by reference).
        '''
        free_spot = self.index_of_free_spot(puzzle_node)
        if(free_spot[0] == 0):
            return None
        self.swap_tiles(free_spot[0],free_spot[1],free_spot[0]-1,free_spot[1], puzzle_node)
        return puzzle_node


    def down_operation(self,puzzle_node):
        '''
        Swaps the free spot with the tile below. If there is
        no tile below, then None, else return the swapped 
        puzzle_node.
        '''
        free_spot = self.index_of_free_spot(puzzle_node)
        if(free_spot[0] == 2):
            return None
        self.swap_tiles(free_spot[0],free_spot[1],free_spot[0]+1,free_spot[1], puzzle_node)
        return puzzle_node    

    def left_operation(self, puzzle_node):
        '''
        Swaps the free spot with the tile to the right. If there is
        no tile to the left, then None, else return the swapped puzzle_node.
        '''
        free_spot = self.index_of_free_spot(puzzle_node)
        if(free_spot[1] == 0):
            return None
        self.swap_tiles(free_spot[0],free_spot[1],free_spot[0],free_spot[1]-1, puzzle_node)
        return puzzle_node


    def right_operation(self, puzzle_node):
        '''
        Swaps the free spot with the tile to the right. If there is
        no tile to the right, then None, else return the swapped puzzle_node.
        '''
        free_spot = self.index_of_free_spot(puzzle_node)
        if(free_spot[1] == 2):
            return None
        self.swap_tiles(free_spot[0],free_spot[1],free_spot[0],free_spot[1]+1, puzzle_node)
        return puzzle_node   


    def is_solved(self,puzzle_node):
        '''
        Checks if the grid has been solved. This is the same across
        all algorithms. True if solved, false otherwise
        '''
        for i in range(len(self.SOLVED)):
            for j in range(len(self.SOLVED[i])):
                if(self.SOLVED[i][j] != puzzle_node.grid[i][j]):
                    return False
        return True

# testing the algorithm
#alg = A_Star()
#alg.solve_puzzle()
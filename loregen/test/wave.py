import random

class Map: 
    def __init__(self, size): 
        self.size = size 
        self.world_map = self.init_grid()

    def init_grid(self): 
        '''Makes the grid of a required matrix size'''
        matrix = []
        for i in range(self.size): 
            row = [0] * self.size 
            matrix.append(row)
        return matrix 



class WaveCollapse: 
    def __init__(self, matrix): 
        '''
        W = Water
        S = Sand 
        G = Grass 
        D = Dirt 
        T = Trees 
        E = Elevation 
        '''
        self.chars = {"W", "S", "G", "T", "E"}

        # domain of all tile types
        self.water = {"W", "S"}
        self.sand = {"S", "W", "G"}
        self.grass = {"G", "S", "D", "T", "E"}
        self.dirt = {"D", "G"}
        self.trees = {"T", "G"}
        self.elevation = {"E", "G"}

        self.matrix = matrix 
        self.fill = 0

    def pprint_map(self): 
        for row in self.matrix: 
            for col in row: 
                print(col, end=" ") 
                
            print("\n")
        print("\n")

    def get_surrounding(self, tile): 
        '''Given a specific character tile return list of possible neighbors'''
        if tile == "W": # Water  
            neighbors = ["W", "S"]
        elif tile == "S": # Sand 
            neighbors = ["S", "W", "G"]
        elif tile == "G": 
            neighbors = ["G", "S", "D", "T"]
        elif tile == "D": 
            neighbors = ["D", "G"]
        elif tile == "T": 
            neighbors = ["T", "G"]

        return neighbors



    def check_valid_tile(self, row, col): 
        if ((row >= 0 and row < len(self.matrix)) and (col >= 0 and col < len(self.matrix))): 
            return True             

    def get_nearby_tiles(self, row, col):  
        # Check up 
        valid_tiles = []
        if self.check_valid_tile(row - 1, col): 
            valid_tiles.append((row - 1, col)) 
        
        # Up Right Diagonal 
        if self.check_valid_tile(row-1, col+1):
            valid_tiles.append((row-1, col+1)) 

        # Right 
        if self.check_valid_tile(row, col+1): 
            valid_tiles.append((row, col+1)) 

        # Down Right Diagonal 
        if self.check_valid_tile(row+1, col+1): 
            valid_tiles.append((row+1, col+1)) 

        # Down
        if self.check_valid_tile(row + 1, col): 
            valid_tiles.append((row + 1, col)) 

        # Left Down Diagonal 
        if self.check_valid_tile(row+1, col-1): 
            valid_tiles.append((row+1, col-1)) 

        # Left 
        if self.check_valid_tile(row, col - 1): 
            valid_tiles.append((row, col - 1)) 

        # Up Left Diagonal 

        if self.check_valid_tile(row-1, col-1): 
            valid_tiles.append((row-1, col-1))

        return valid_tiles

    def get_set(self, char): 
        domain_set = None 
        if char == "W": # Water  
            domain_set = self.water 
        elif char == "S": # Sand 
            domain_set = self.sand 
        elif char == "G": 
            domain_set = self.grass 
        elif char == "D": 
            domain_set = self.dirt 
        elif char == "T": 
            domain_set = self.trees
        elif char == "E": 
            domain_set = self.elevation
        else: 
            domain_set = self.chars 

        return domain_set


    def check_domain(self, row, col): 
        domain_set = self.chars
        nearby_tiles = self.get_nearby_tiles(row, col)
        domain_set = domain_set.intersection(self.get_set(self.matrix[row][col]))
        for tile in nearby_tiles: 
            if self.matrix[tile[0]][tile[1]] == 0: 
                domain_set = domain_set.intersection(domain_set) 
            if self.matrix[tile[0]][tile[1]] == "W": 
                domain_set = domain_set.intersection(self.water)
            if self.matrix[tile[0]][tile[1]] == "S": 
                domain_set = domain_set.intersection(self.sand)
            if self.matrix[tile[0]][tile[1]] == "E": 
                domain_set = domain_set.intersection(self.elevation)
            if self.matrix[tile[0]][tile[1]] == "G": 
                domain_set = domain_set.intersection(self.grass)
            if self.matrix[tile[0]][tile[1]] == "D": 
                domain_set = domain_set.intersection(self.dirt)

            if self.matrix[tile[0]][tile[1]] == "T": 
                domain_set = domain_set.intersection(self.trees)

        return domain_set

        




    def get_random_tile(self): 
        rand_row = random.randint(0, len(self.matrix) - 1 )
        rand_col = random.randint(0, len(self.matrix[rand_row]) - 1) 

        return (rand_row, rand_col)


    def iterated_wave(self):  
        tile = random.choice(list(self.chars))
        self.matrix[0][0] = tile 
        for i in range(len(self.matrix)):  
            for j in range(len(self.matrix[i])): 
                tile = random.choice(list(self.check_domain(i, j)))
                self.matrix[i][j] = tile 






#m1 = Map()
#w1 = WaveCollapse(m1.world_map)
#w1.iterated_wave()


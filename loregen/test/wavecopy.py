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
        self.universal = ["G", "T", "S", "W"]
        self.grass = ["G", "T", "S", "E"]
        self.tree = ["T", "G"]
        self.sand = ["S", "W", "G"]
        self.water = ["W", "S"]


        self.domains = {
            "G": self.grass,
            "T": self.tree, 
            "S": self.sand,
            "W": self.water,
        }

        self.matrix = matrix 
        self.grid = matrix 
        self.fill = 0

    def pprint_map(self): 
        for row in self.grid: 
            for col in row: 
                print(col["value"], end=" ") 
            print("\n")
        print("\n")

    def make_grid(self): 
        for i, row in enumerate(self.matrix): 
            for j, col in enumerate(row): 
                grid_object = {
                    "value": 0, # default value
                    "collapsed": False, 
                    "domain": self.universal, # Up, right, down, left
                }
                self.grid[i][j] = grid_object

        

    def check_valid_tile(self, row, col): 
        if ((row >= 0 and row < len(self.grid)) and (col >= 0 and col < len(self.grid))): 
            return True             

    def get_nearby_tiles(self, row, col):  
        # Check up 
        valid_tiles = []
        if self.check_valid_tile(row - 1, col): 
            valid_tiles.append((row - 1, col, 'UP')) 
        
        # Up Right Diagonal 
        #if self.check_valid_tile(row-1, col+1):
        #    valid_tiles.append((row-1, col+1, 'UP_RIGHT')) 

        # Right 
        if self.check_valid_tile(row, col+1): 
            valid_tiles.append((row, col+1, "RIGHT")) 

        # Down Right Diagonal 
        #if self.check_valid_tile(row+1, col+1): 
        #    valid_tiles.append((row+1, col+1, "DOWN_RIGHT")) 

        # Down
        if self.check_valid_tile(row + 1, col): 
            valid_tiles.append((row + 1, col, "DOWN")) 

        # Left Down Diagonal 
        #if self.check_valid_tile(row+1, col-1): 
        #    valid_tiles.append((row+1, col-1, "LEFT_DOWN")) 

        # Left 
        if self.check_valid_tile(row, col - 1): 
            valid_tiles.append((row, col - 1, "LEFT")) 

        # Up Left Diagonal 

        #if self.check_valid_tile(row-1, col-1): 
        #    valid_tiles.append((row-1, col-1, "UP_LEFT"))

        return valid_tiles



    def compare_domain(self, grid_obj1, grid_obj2):
        # Intersect grid_obj2 with grid_obj1  
        new_domain = []
        for element in grid_obj2 : 
            if element in grid_obj1: 
                new_domain.append(element)

        return new_domain

    def update_domain(self): 
        for i, row in enumerate(self.grid): 
            for j, col in enumerate(row): 
                if self.grid[i][j]["value"] == 0: 
                    neighbors = self.get_nearby_tiles(i,j)
                    for n in neighbors: 
                        grid_obj = self.grid[n[0]][n[1]] 
                        if grid_obj["value"] != 0: 
                            self.grid[i][j]["domain"] = self.compare_domain(self.grid[i][j]["domain"], grid_obj["domain"])



    def get_random_tile(self): 
        rand_row = random.randint(0, len(self.matrix) - 1 )
        rand_col = random.randint(0, len(self.matrix[rand_row]) - 1) 

        return (rand_row, rand_col)


    def collapse_tile(self, row, col):  

        # Up 
        if self.check_valid_tile(row - 1, col): 
            pass 
        
        # Right 
        if self.check_valid_tile(row, col+1): 
            pass  

        # Down
        if self.check_valid_tile(row + 1, col): 
            pass 

        # Left 
        if self.check_valid_tile(row, col - 1): 
            pass 

    def propagate(self, row, col, domain): 
        propagation = random.choice(domain)
        self.grid[row][col]["value"] = propagation 
        self.grid[row][col]["domain"] = self.domains[propagation]

    def min_entropy(self): 
        entropy_dict = {}
        cords = []
        for i, row in enumerate(self.grid): 
            for j, col in enumerate(row): 
                if col["value"] == 0: 
                    entropy_dict[(i, j)] = len(col["domain"])
            
        minimum = min((list(entropy_dict.values())))
        for cord in entropy_dict: 
            if entropy_dict[cord] == minimum and self.grid[cord[0]][cord[1]]["value"] == 0: 
                cords.append(cord) 



        return random.choice(cords) 
                

    def wfc(self): 
        '''wave function collapse'''
        rand_tile = self.get_random_tile() 
        self.propagate(rand_tile[0],rand_tile[1], random.choice(self.universal))
        self.fill += 1 
        while self.fill < len(self.matrix) * len(self.matrix): 
            self.update_domain() 

            cords = self.min_entropy()
            grid_object = self.grid[cords[0]][cords[1]]

           
            random_value = random.choice(grid_object["domain"])
            self.propagate(cords[0], cords[1], random_value)
            self.fill += 1 
            print(self.fill)

        return self.grid   






#m1 = Map(100)
#w1 = WaveCollapse(m1.world_map)
#w1.make_grid()
#w1.wfc()

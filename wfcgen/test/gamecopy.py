import pygame 
from wavecopy import Map, WaveCollapse 


class Game(): 
    '''Class for game graphics'''
    def __init__(self, matrix, base_grid): 
        self.matrix = matrix
        self.base_grid = base_grid
        self.draw_scale = len(self.matrix)
        self.screen_width = 900
        self.screen_height = 900 
        self.pixel_positions = self.base_grid  # The pixel positions corresponding to each element in the maze matrix
        self.loop = True 


        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
    

    def create_pixel_positions(self, matrix): 
        '''Changes the value of each element in the maze to a corresponding pixel position'''
        x = 0 
        y = 0 
        for i, row in enumerate(matrix): 
            for j, col in enumerate(row): 
                self.pixel_positions[i][j] = (x,y)
                x += self.screen_width // self.draw_scale

            x = 0 
            y += self.screen_height // self.draw_scale

    def draw_grid(self, matrix): 
        '''Draw the maze''' 
        x = 0 
        y = 0 
        for row in matrix: 
            for char in row: 
                if char['value'] == "W": 
                    color = pygame.Color("Blue")
                elif char['value'] == "G": 
                    color = pygame.Color(21,71,52)  
                elif char['value'] == "S":
                    color = pygame.Color(225,191,146)
                elif char['value'] == "T": 
                    color = pygame.Color(21,61,42)
                elif char['value'] == "D": 
                    color = pygame.Color("#050A30")
                elif char['value'] == "E": 
                    color = pygame.Color("Gray")




                bar = pygame.Rect(x, y, self.screen_width // self.draw_scale, self.screen_height // self.draw_scale)
                pygame.draw.rect(self.screen, color, bar) 

                x += self.screen_width // self.draw_scale
            x = 0 
            y += self.screen_height // self.draw_scale 


    def run(self, speed): 
        '''Runs the main game loop'''
        self.create_pixel_positions(self.base_grid)
        while self.loop: 
            self.draw_grid(self.matrix)


            pygame.display.flip()
            pygame.time.wait(speed)


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.loop = False 


m1 = Map(100)
w1 = WaveCollapse(m1.world_map)
w1.make_grid()
wfc_grid = w1.wfc()
g1 = Game(wfc_grid, m1.init_grid())
g1.run(0)
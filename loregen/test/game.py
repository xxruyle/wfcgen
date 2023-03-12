import pygame 
from wave import Map, WaveCollapse 


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
                if char == "W": 
                    color = pygame.Color("Blue")
                elif char == "G": 
                    color = pygame.Color("Green")  
                elif char == "S":
                    color = pygame.Color(225,191,146)
                elif char == "T": 
                    color = pygame.Color(21,71,52)
                elif char == "D": 
                    color = pygame.Color("#987654")
                elif char == "E": 
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


grid = Map(20)
base_grid = grid.init_grid()
w1 = WaveCollapse(grid.world_map)
w1.iterated_wave()
m1 = Game(w1.matrix, base_grid)
m1.run(0)
import pygame 
import random

universal_domain = {"grass_mid", "grass_up", "grass_up_right_corner", "grass_right", "grass_down_right_corner", "grass_down", "grass_down_left_corner", "grass_left", "grass_up_left_corner", "blank"}

modules = {
    "grass_mid": { # 0
        "up_domain": {"grass_mid",  "grass_up"},
        "right_domain": {"grass_mid", "grass_right"},
        "down_domain": {"grass_mid", "grass_down"},
        "left_domain": {"grass_mid", "grass_left"} 
    },
    "grass_up": { # 1 
        "up_domain": {"blank"},
        "right_domain": {"grass_up", "grass_up_right_corner"}, 
        "down_domain": {"grass_mid"}, 
        "left_domain": {"grass_up", "grass_up_left_corner"}
    },
    "grass_up_right_corner": { # 2 
        "up_domain": {"blank"},
        "right_domain": {"blank"}, 
        "down_domain": {"grass_right"}, 
        "left_domain": {"grass_up"}
    },
    "grass_right": { # 3
        "up_domain": {"grass_up_right_corner"},
        "right_domain": {"blank"}, 
        "down_domain": {"grass_down_right_corner"}, 
        "left_domain": {"grass_mid"}
    }, 
    "grass_down_right_corner": { # 4 
        "up_domain": {},
        "right_domain": {}, 
        "down_domain": {}, 
        "left_domain": {}
    },
    "grass_down": { # 5 
        "up_domain": {},
        "right_domain": {}, 
        "down_domain": {}, 
        "left_domain": {}
    }, 
    "grass_down_left_corner": { # 6 
        "up_domain": {},
        "right_domain": {}, 
        "down_domain": {}, 
        "left_domain": {}
    }, 
    "grass_left": { # 6 
        "up_domain": {},
        "right_domain": {}, 
        "down_domain": {}, 
        "left_domain": {}
    },
    "grass_up_left_corner": { # 7 
        "up_domain": {},
        "right_domain": {}, 
        "down_domain": {}, 
        "left_domain": {}
    },

    ##################################
    "blank": { # 8 
        "up_domain": {"grass_down"},
        "right_domain": {"grass_left"}, 
        "down_domain": {"grass_up"}, 
        "left_domain": {"grass_right"}
    }
}






def make_grid(size): 
    grid = []
    for i in range(size): 
        row = [0] * size 
        grid.append(row)
    return grid 


stored_domains = {}
def initial_domain(grid): 
    for i, row in enumerate(grid): 
        for j, col in enumerate(row): 
            if col == 0: 
                stored_domains[(i,j)] = {
                    "up_domain": universal_domain,
                    "right_domain": universal_domain, 
                    "down_domain": universal_domain, 
                    "left_domain": universal_domain
                    }



grid = make_grid(3)
initial_domain(grid)
print(stored_domains)
















width = 600 
height = 600

screen = pygame.display.set_mode((width,height))

def draw_grid(grid): 
    x = 0 
    y = 0 
    for i in range(len(grid)): 
        for j in range(len(grid[i])): 
            color = pygame.Color("Red")
            square = pygame.Rect(x,y, width // len(grid), height // len(grid))
            pygame.draw.rect(screen, color, square, 1)

            x += width // len(grid)
        x = 0 
        y += height // len(grid)


def run_game(): 
    grid = make_grid(5)
    loop = True 
    while loop: 
        draw_grid(grid)
        pygame.display.flip()


        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                loop = False 

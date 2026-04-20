import numpy as np
from core.grid import Grid
from core.velocity import Velocity
from config.parameters import *

class Advection:
    
    def __init__(self, grid: Grid, velocity: Velocity) -> None:
        self.grid = grid
        self.velocity = velocity
        self.dt = TIME_STEP
        
    def advectDensity(self):
        tempGrid = np.zeros_like(self.grid.grid)
        gridWidth = self.grid.gridWidth
        gridHeight = self.grid.gridHeight    
        
        for i in range(gridHeight):
            for j in range(gridWidth):
                
                if self.velocity.obstacles[i, j] == 1:
                    tempGrid[i, j] = self.grid.grid[i, j]
                    continue
                
                oldX = i - self.velocity.u[i, j] * self.dt
                oldY = j - self.velocity.v[i, j] * self.dt
                
                oldX = max(0, min(self.grid.gridHeight - 1, oldX))
                oldY = max(0, min(self.grid.gridWidth - 1, oldY))
                
                if self.velocity.obstacles[int(oldX), int(oldY)] == 1:
                    tempGrid[i, j] = self.grid.grid[i, j]
                    continue
                
                x0 = int(np.floor(oldX))
                x1 = x0 + 1
                y0 = int(np.floor(oldY))
                y1 = y0 + 1
                
                x1 = min(self.grid.gridHeight - 1, x1)
                y1 = min(self.grid.gridWidth - 1, y1)
                
                sx = oldX - x0
                sy = oldY - y0
                
                def sample(x, y):
                    if self.velocity.obstacles[x, y] == 1:
                        return self.grid.grid[i, j]
                    return self.grid.grid[x, y]
                
                bottom = (1 - sx) * sample(x0, y0) + sx * sample(x1, y0)
                top = (1 - sx) * sample(x0, y1) + sx * sample(x1, y1)
                value = (1 - sy) * bottom + sy * top
        
                tempGrid[i, j] = value
        
        self.grid.grid[:, :] = tempGrid
import numpy as np
from config.parameters import *
from core.velocity import Velocity
from core.grid import Grid

class Diffusion:
    
    def __init__(self, grid: Grid, velocity: Velocity) -> None:
        self.diffusionRate = DIFFUSION_RATE
        self.grid = grid
        self.velocity = velocity
        
    def diffuse(self) -> np.array:
        tempGrid = self.grid.grid.copy()
        
        for i in range(self.grid.gridHeight):
            for j in range(self.grid.gridWidth):
                
                if self.velocity.obstacles[i, j] == 1:
                    tempGrid[i, j] = self.grid.grid[i, j]
                    continue
                
                neighbours = []
                currentCellFluidAmount = self.grid.grid[i, j]
                
                if (i-1 >= 0) and (self.velocity.obstacles[i-1, j] == 0): neighbours.append(self.grid.grid[i-1, j]) 
                if (i+1 < self.grid.gridHeight) and (self.velocity.obstacles[i+1, j] == 0): neighbours.append(self.grid.grid[i+1, j]) 
                if (j-1 >= 0) and (self.velocity.obstacles[i, j-1] == 0): neighbours.append(self.grid.grid[i, j-1]) 
                if (j+1 < self.grid.gridWidth) and (self.velocity.obstacles[i, j+1] == 0): neighbours.append(self.grid.grid[i, j+1]) 
                
                if len(neighbours) == 0:
                    tempGrid[i, j] = currentCellFluidAmount
                    continue
                
                neighboursTotalFluidAmount = np.sum(neighbours)
                
                totalNeighbours = len(neighbours)

                fluidAmountToMove = currentCellFluidAmount + self.diffusionRate * (neighboursTotalFluidAmount - totalNeighbours * currentCellFluidAmount)
                tempGrid[i, j] = fluidAmountToMove
                
        self.grid.grid[:, :] = tempGrid
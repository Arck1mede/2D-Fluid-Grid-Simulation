import numpy as np
from config.parameters import *

class Grid:
    
    def __init__(self) -> None:
        self.gridWidth = GRID_WIDTH
        self.gridHeight = GRID_HEIGHT
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=float)
        
    def initializeWorld(self):
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                self.grid[i, j] = getRandomGridNum()
    
    def readFluidValue(self, i, j):
        return self.grid[i, j] 

    def changeFluidValue(self, i, j, newValue: int):
        self.grid[i, j] = newValue
    
    def addFluid(self, i, j, fluidValue: int):
        self.grid[i, j] += fluidValue
        
    def removeFluid(self, i, j, fluidValue):
        self.grid[i, j] -= fluidValue
            
    def resetWorld(self):
        self.grid[:, :] = 0
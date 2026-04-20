import numpy as np
from core.grid import Grid
from config.parameters import *

class Velocity:
    
    def __init__(self, grid: Grid):
        self.grid = grid
        self.u = np.zeros(shape=(self.grid.gridHeight, self.grid.gridWidth)) 
        self.v = np.zeros(shape=(self.grid.gridHeight, self.grid.gridWidth))
        self.obstacles = np.zeros_like(self.grid.grid)
        self.timeStep = TIME_STEP
        self.forceStrength = FORCE_STRENGTH
    
    def step(self):
        self.u[:, :] = HORIZONTAL_VEL_ADD_AMOUNT
        self.v[:, :] = VERTICAL_VEL_ADD_AMOUNT 
        
    def getMagnitude(self):
        return np.sqrt(self.u ** 2 + self.v ** 2)
    
    def placeRectangeObstacle(self):
        self.obstacles[OBSTACLE_X_START:OBSTACLE_X_END, OBSTACLE_Y_START:OBSTACLE_Y_END] = 1
        
    def placeCircleObstacle(self):
        circleXPos, circleYPos = CIRCLE_X_POS, CIRCLE_Y_POS
        circleRadius = CIRCLE_RADIUS
        
        for x in range(self.grid.gridHeight):
            for y in range(self.grid.gridWidth):
                dist = np.sqrt((x - circleXPos)**2 + (y - circleYPos)**2)
                if dist <= circleRadius:
                    self.obstacles[x, y] = 1
                
    def checkBoundaries(self):
        for i in range(self.grid.gridHeight):
            for j in range(self.grid.gridWidth):
                                
                if self.obstacles[i, j] == 1:
                    self.u[i, j] = 0 
                    self.v[i, j] = 0 
                    continue
                
                if i < self.grid.gridHeight - 1: 
                    if self.obstacles[i+1, j] == 1 and self.u[i, j] > 0:
                        self.u[i, j] *= -0.5
                        
                if i > 0: 
                    if self.obstacles[i-1, j] == 1 and self.u[i, j] < 0:
                        self.u[i, j] = 0
                        
                if j < self.grid.gridWidth - 1: 
                    if self.obstacles[i, j+1] == 1 and self.v[i, j] > 0:
                        self.v[i, j] = 0
                        
                if j > 0:
                    if self.obstacles[i, j-1] == 1 and self.v[i, j] < 0:
                        self.v[i, j] = 0
        
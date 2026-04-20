import matplotlib.pyplot as plt
import numpy as np
from core.grid import Grid
import matplotlib.colors as colors
from config.parameters import *

class PlotFrame:
    
    def __init__(self, grid: Grid):
        self.grid = grid
    
    def createHeatmap(self) -> tuple:
        data = self.grid.grid
        colorsList = GRID_PLOT_COLORS
        colorbarTicks = np.linspace(MIN_RAND_NUM, MAX_RAND_NUM, num=5)
        yTickLabels = [str(num) for num in colorbarTicks]
        
        cmap = colors.ListedColormap(colorsList)

        fig, ax = plt.subplots()
        
        im = ax.imshow(data.T, cmap=cmap, vmin=MIN_RAND_NUM, vmax=MAX_RAND_NUM , extent=[0, self.grid.gridWidth, 0, self.grid.gridHeight], origin='lower')
        
        cbar = plt.colorbar(im, ticks=colorbarTicks)
        cbar.ax.set_yticklabels(yTickLabels)

        plt.title("2D Grid Visualized")
        plt.xlabel("X")
        plt.ylabel("Y")
            
        return fig, ax, im
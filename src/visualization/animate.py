from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from core.grid import Grid
from visualization.plotFrame import PlotFrame
from config.parameters import *

class Animation:
    
    def __init__(self, grid: Grid, plotFrame: PlotFrame, simulation) -> None:
        self.grid = grid
        self.loopTime = LOOP_TIME
        self.pauseInterval = PAUSE_INTERVAL
        self.fig, self.ax, self.image = plotFrame.createHeatmap()
        self.simulation = simulation
    
    def update(self, frame):
        self.simulation.step()
        self.image.set_data(self.grid.grid)
        
    def start(self):
        self.grid.initializeWorld()
        self.anim = FuncAnimation(fig=self.fig, 
                                  func=self.update,
                                  frames=self.loopTime, 
                                  interval=100, 
                                  blit=False, 
                                  repeat=True)
        plt.show()
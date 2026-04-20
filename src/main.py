from core.grid import Grid
from core.diffusion import Diffusion
from visualization.plotFrame import PlotFrame
from visualization.animate import Animation
from core.velocity import Velocity
from core.advection import Advection

class Simulation:
    
    def __init__(self) -> None:
        self.grid = Grid()
        self.velocity = Velocity(self.grid)
        self.diffusion = Diffusion(self.grid, self.velocity)
        self.plotFrame = PlotFrame(self.grid)
        self.advection = Advection(self.grid, self.velocity)
        self.velocity.placeCircleObstacle()
        self.velocity.placeRectangeObstacle()
    
    def step(self) -> None:
        self.velocity.step()
        self.velocity.checkBoundaries()
        self.advection.advectDensity()
        self.diffusion.diffuse()
    

if __name__ == "__main__":                    
    simulation = Simulation()
    animation = Animation(simulation.grid, simulation.plotFrame, simulation)
    animation.start()



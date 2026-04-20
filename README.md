# 💧 2D Fluid Grid Simulation

This is my second project regarding fluid simulation and it features a fluid moving using a grid, which holds the actual values to move the fluid. The whole project is animated in real time showing how the fluid interacts with two types of obstacles (a rectangle and a circle) and uses common fluid characteristics such as advention and diffusion.

## 💻 Technologies Used

* ```Matplotlib```

* ```Numpy```

## 🃏 Features

### The simulation has the following characteristics:

- Advection: the ```advection.py``` file implements fluid advection. Advention is all about fluid movement: it uses the horizontal and vertical velocity to update the fluid position. This is done by implementing backward-tracing and Semi-Lagrangian bilinear interpolation.

- Diffusion: the ```diffusion.py``` file implements fluid diffusion, which is another fluid property. In simple terms, diffusions makes the fluid spread around and works by looking at the neighbours: do they have more values or not? It so, the particle that spreads gets some of it.

- Grid System: I created a grid system for both the fluid and the obstacles. The fluid grid values go from 0 to 10 while the obstacle grid uses 1 or 0 to identify if there is an obstacle or not at a certain position,
respectively.

- Fluid Animation: all the simulation is rendered and simulated in real time by using ```imshow``` and a slider is added to the right side of the plot to show the grid value at a certain point. By default, the values go
from 0 to 10. 

## 🏫 What I Learned

After completing the project I learned:

1.	Grid System Implementation: I needed to come up with a way to store the fluid values and this is where the grid became useful. Not only for fluid but also for obstacles.

2.	Fluid Properties: I learned and implemented two new fluid properties I didn't know about, namely advection and diffusion. These form the core of how fluids move and spread around, filling areas that before were
unfilled.
   
3. Physics Interaction: to make the fluid more alive, I learned to make it interact with two types of obstacles, namely a rectangle placed in the center of the screen and a circle found at the bottom left. 
 
## 💭 How Can It Be Improved?

- 3D Implementation: I think the 2D implementation came up okay overall but a 3D implementation would definitely improve the visuals and the understanding of fluid movement. 
- Vortices: the fluid currently moves but there are no vortices or conditions that make it swirl around. This would the whole simulation more real.

## 📹 Video
https://github.com/user-attachments/assets/aea7b658-d85a-4920-a395-a449dd2fe3dc

import matplotlib.pyplot as plt
import numpy as np

s = 50
max = 200

world = np.zeros(shape=(s,s),dtype=int)
def near(world):
    P,Q = world.shape
    world_diff = np.zeros(shape=world.shape,dtype=int)
    ADJACENTS = {(-1, 1), (0, 1), (1, 1), (-1, 0),
             (1, 0), (-1, -1), (0,-1), (1,-1)}
    for y,row in enumerate(world):
        for x,val in enumerate(row):
            for dy, dx in ADJACENTS:
                if 0 <= y+dy < P and 0 <= x+dx < Q:
                    world_diff[y,x] += world[y+dy,x+dx]
    return world_diff


def tetris(i,j):
    world[i,j] = 1
    world[i,j-1] = 1
    world[i,j+1] = 1
    world[i+1,j] = 1
    world[i-1,j-1] = 1

def line(i,j):
    world[i,j] = 1
    world[i-1,j] = 1
    world[i+1,j] = 1

def box(i,j):
    world[i,j] = 1
    world[i+1,j+1] = 1
    world[i+1,j] = 1
    world[i,j+1] = 1

def glider_s(i,j):
    world[i,j] = 1
    world[i-1,j-1] = 1
    world[i-1,j-2] = 1
    world[i,j-2] = 1
    world[i+1,j-2] = 1

def glider_b(i,j):
    world[i,j] = 1
    world[i,j+2] = 1
    world[i+1,j+3] = 1
    world[i+2,j+3] = 1
    world[i+3,j+3] = 1
    world[i+4,j+3] = 1
    world[i+5,j+3] = 1
    world[i+5,j+2] = 1
    world[i+5,j+1] = 1
    world[i+4,j] = 1
    world[i+2,j-1] = 1

glider_b(12,12)
box(25,12)
box(30,30)
tetris(20,40)
tetris(40,20)

for t in range(max):
    print(t)
    plt.imshow(world)
    plt.pause(0.001)
    world_n = np.copy(world)
    pop = near(world)
    for i in range(s):
        for j in range(s):
            if (world[i,j] == 1):
                if (pop[i,j] < 2):
                    world_n[i,j] = 0
                if (pop[i,j] == 2 or pop[i,j] == 3):
                    world_n[i,j] = 1
                if (pop[i,j] > 3):
                    world_n[i,j] = 0
            if (world[i,j] == 0):
               if (pop[i,j] == 3):
                    world_n[i,j] = 1 
    world = np.copy(world_n)
plt.show()
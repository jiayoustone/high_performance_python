#!/usr/bin/env python2.7

from __future__ import division
import time

grid_shape = (512, 512)

#@profile
def evolve(grid, dt, out, D=1.0):
    xmax, ymax = grid_shape
    #new_grid = [[0.0, ] * ymax] * xmax              # 二维数组
    for i in range(xmax):
        for j in range(ymax):
            grid_xx = grid[(i + 1) % xmax][j] + grid[(i - 1) % xmax][j] - 2.0 * grid[i][j]
            grid_yy = grid[i][(j + 1) % ymax] + grid[i][(j - 1) % ymax] - 2.0 * grid[i][j]
            out[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt

def run_experiment(num_iterations):
    # setting up initial conditions
    xmax, ymax = grid_shape
    grid = [[0.0, ] * ymax] * xmax                        # 二维数组
    new_grid = [[0.0, ] * ymax] * xmax

    # initialization assumes that xmax <= ymax
    block_low = int(xmax * .4)
    block_high = int(xmax * .5)
    for i in range(block_low, block_high):
        for j in range(block_low, block_high):
            grid[i][j] = 0.005

    start = time.time()
    for i in range(num_iterations):
        evolve(grid, 0.1, new_grid)
        grid, new_grid = new_grid, grid
    return time.time() - start



if __name__ == "__main__":
    run_experiment(500)

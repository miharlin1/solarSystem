#Author: Mia Harlin
#Date: 10/27/2024
#Purpose: System Class

from cs1lib import *

class System:
    def __init__(self, body_list):
        self.body_list = body_list #list of pre defined body instances
    def update(self, timestep):
        #for each body in body_list, update position and velocity (by finding acceleration)
        # ax = 0.005 #m / s2
        # ay = 0 #m / s2
        for i in range(len(self.body_list)):
            self.body_list[i].update_position(timestep)
            ax, ay = self.compute_acceleration(i)
            self.body_list[i].update_velocity(ax, ay,timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx,cy,pixels_per_meter)

    def compute_acceleration(self, n):
        #computer acceleration of each body onto body at index n
        G = 6.67384 * (10**(-11)) #gravity
        ax, ay = 0,0

        for i in range(len(self.body_list)):
            if i != n: #don't compute acceleration of n on itself
                dx = (self.body_list[i].x - self.body_list[n].x) #x distance between body n and body i
                dy = (self.body_list[i].y - self.body_list[n].y) #y distance between body n and body i
                r = (dx**2 + dy**2)**(1/2) #total distance between two bodies
                a = G * self.body_list[i].mass / (r**2) #total amount of acceleration
                ax += a * (dx / r) #acceleration in x direction
                ay += a * (dy / r) #acceleration in y direction

        return ax, ay
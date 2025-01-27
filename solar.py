#Author: Mia Harlin
#Date: 10/27/2024
#Purpose: Solar system, system driver

#ideas for extra credit: can click on moving objects and their mass and distance from sun projected (educational material)
#maybe even image pops up too
#scaler so you can choose time_scale
from cs1lib import *
from Labs.Lab2_solarsystem.system import System
from Labs.Lab2_solarsystem.body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# time_scale = 3.0e6       # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

#define rectangle variables
REC_WIDTH = 180
REC_HEIGHT = 10
recx = WINDOW_WIDTH // 15 + 150
recy = WINDOW_HEIGHT // 15 - REC_HEIGHT

#define ball variables
BR = 10 #ball radius
bx = WINDOW_WIDTH // 15 + 150 + REC_WIDTH//2 #middle of scale
by = recy + BR//2

mpressed = False
mousex = 0
mousey= 0
def draw_tracker_ball():
    global bx
    set_fill_color(1,0,0)
    if mpressed:
        if recx < mousex < recx+REC_WIDTH and recy < mousey < recy + REC_HEIGHT:
            bx = mousex

    draw_circle(bx, by, BR)

def update_time_scale():
    #simulation begins at center of scale, at value 3.0e6
    #then multiply times factor value
    #factor determined by distance from center of scale (mid_rec) and then scaled
    time_scale = 3.0e6
    mid_rec = WINDOW_WIDTH // 15 + 150 + REC_WIDTH // 2  # middle of rectangle is starting point
    factor = (mid_rec-bx)* 0.005 #distance from middle (starting point)
    time_scale = time_scale * (1 - factor)

    return time_scale

def draw_scaler():
    enable_stroke()
    set_font_size(15)
    set_stroke_color(1,1,1)
    draw_text("Change time_sale : ", WINDOW_WIDTH//15,WINDOW_HEIGHT//15)
    set_fill_color(1,1,1)

    draw_rectangle(recx, recy, REC_WIDTH,REC_HEIGHT)
    draw_tracker_ball()

def main():
    set_clear_color(0, 0, 0)    # black background

    clear()
    draw_scaler()
    # Draw the system in its current state.
    solarsystem.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    time_scale = update_time_scale()
    solarsystem.update(TIMESTEP * time_scale)

def define_bodies():
#define bodies with provided values
    sun = Body (1.98892e30, 0,0,0,0, 19, 1,1,0)
    mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 3, .79,.69,.58)
    venus = Body(4.87e24,  -108.2e9, 0, 0, 35040, 6,.78,.44,.44)
    earth = Body(5.97e24, -149.6e9, 0,0,29790,7,.44,.58,.86)
    mars = Body(0.642e24, -227.9e9, 0,0,24140, 4, .69,.25,.21)

    solarsystem = System([sun, mercury, venus, earth, mars])
    return solarsystem


def my_mpress(mx, my): #this function must take two parameters
    global mpressed
    mpressed = True

def my_mrelease(mx, my):
    global mpressed
    mpressed = False

def my_mmove(mx,my):
    global mousex, mousey
    mousex = mx
    mousey = my

solarsystem = define_bodies()
start_graphics(main, 2400, framerate=FRAMERATE, mouse_press=my_mpress, mouse_release=my_mrelease, mouse_move=my_mmove)
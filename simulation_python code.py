from turtle import color
from matplotlib import pyplot as plt
from matplotlib import animation
import math

g = 9.8
u = eval(input("Enter the initial velocity(>44.27): ")) # velocity in swinging phase
v = 2*u      #velocity in supporting phase
theta = eval(input("Enter the initial angle: "))
time_swinging_phase = 2*u*math.sin(math.radians(theta))/g
total_time = (5*time_swinging_phase)/4
x = -100   # starting position

def time_list(): #for generating a list of times at dt interval

    intervals = []
    t = 0
    dt = 0.01
    while t <= total_time:
        intervals.append(t)
        t = t + dt
    return intervals
           
    
def change_position(i, circle, intervals, u, theta):
    t = intervals[i]
    if t < time_swinging_phase :               
                x = -100 + (u*math.cos(math.radians(theta))*t)
                y = (u*math.sin(math.radians(theta))*t - (0.5*g*t*t))
    else :        #supporting phase 
                y = 0
                x = 100 - (v*(t-time_swinging_phase))
        
    circle.center = x, y
    return circle


intervals = time_list()
xmin = -100
xmax = 100
ymin = 0
ymax = (u*u)/(2*g)
fig = plt.gcf()                           # to get the current figure
axis = plt.axes(xlim=(xmin-150,xmax+150 ), ylim=(ymin-50,ymax+100))  
    
circle = plt.Circle((xmin, ymin), 10, color='r')
axis.add_patch(circle)
anim = animation.FuncAnimation(fig, change_position,
                        fargs=(circle, intervals, u, theta),
                        frames=len(intervals), interval=20,
                        repeat=True)
    
    
plt.grid(True)
plt.show()
import numpy as np 
import matplotlib.pyplot as plt 

def do_time_integration_step(time_step,y_old,dydt):
    y_new=y_old+time_step*(24*epsilon)
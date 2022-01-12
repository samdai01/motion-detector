# ********************************************************************************
# Plotting script that executes capture_video and plots the object enter and exit
# data.
# Written by Sam Dai 
# ********************************************************************************

# Importing of dataFrame data from capture_video and needed bokeh plotting libraries.
from capture_video import dataFrame
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Change name of output graph, make sure that string ends in ".html"
output_file("motionData.html")

# Creates a new figure, sets its dimensions and configures the title and format.
f = figure(x_axis_type = "datetime", height = 200, width = 1000, title = "Motion Data")
f.yaxis.minor_tick_line_color = None
f.xgrid.grid_line_color = None
f.ygrid.grid_line_color = None

# Creates the graph elements based on the output data times.
glyph = f.quad(left = dataFrame["Start Times"], right = dataFrame["End Times"], bottom = False, top = True, color = "blue")

output_file("motionData.html")

show(f)
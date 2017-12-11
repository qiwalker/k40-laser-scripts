#!/usr/bin/env python
# coding=UTF-8
"""Module containing Gcode parsing functions"""

__author__ = "Dylan Armitage"
__email__ = "d.armitage89@gmail.com"


####---- Imports ----####
from pygcode import Line, GCodeLinearMove

def bounding_box(gcode_file):
    """Take in file of gcode, return tuples of min/max bounding values"""
    lines = [Line(line) for line in gcode_file]
    params = [p.get_param_dict() for p in lines if p.word == "G01"]
    x_pos = [p["X"] for p in params]
    y_pos = [p["Y"] for p in params]
    return ((min(x_pos),min(y_pos)), (max(x_pos),max(y_pos)))

def box_gcode(min_xy, max_xy):
    """Take in min/max coordinate tuples, return G0 commands to bound it"""
    gcode = []
    gcode.append(GCodeLinearMove(X=min_xy[0], Y=min_xy[1]))
    gcode.append(GCodeLinearMove(X=max_xy[0], Y=min_xy[1]))
    gcode.append(GCodeLinearMove(X=max_xy[0], Y=max_xy[1]))
    gcode.append(GCodeLinearMove(X=min_xy[0], Y=max_xy[1]))
    gcode.append(GCodeLinearMove(X=min_xy[0], Y=min_xy[1]))
    # Convert from GCodeLinearMove class to string
    gcode = [str(line) for line in gcode]
    return gcode

def mid_gcode(min_xy, max_xy):
    """Take in min/max coord tuples, return G0 to go to midpoint"""
    mid_x = float((min_xy[0]+max_xy[0])/2)
    mid_y = float((min_xy[1]+max_xy[1])/2)
    return str(GCodeLinearMove(X=mid_x, Y=mid_y))

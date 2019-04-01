'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M Programming-for-Spatial-Analysts-Advanced-Skills
    Author: Annabel Whipp
    File name: explosionscript.py
'''

# imports

import arcpy


p0 = arcpy.GetParameterAsText(0)
p1 = arcpy.GetParameterAsText(1)
p2 = arcpy.GetParameterAsText(2)
p3 = arcpy.GetParameterAsText(3)

try:
    try:
        arcpy.ImportToolbox("m:/advancedprogramming/models.tbx", "models")
    except arcpy.ExecuteError as e:
        print("Import toolbox error", e)
    try:
        arcpy.Explosion_models(p0,p1,p2,p3)
#        arcpy.Explosion_models("M:/advancedprogramming/data/input/explosion.shp",
#						"100 Meters", 
#						"M:/advancedprogramming/data/input/buildings.shp", 
#						"M:/advancedprogramming/data/generated/int4.shp") # Your parameters, here.
    except arcpy.ExecuteError as e:
        print("Model run error", e)
except Exception as e:
    print(e)

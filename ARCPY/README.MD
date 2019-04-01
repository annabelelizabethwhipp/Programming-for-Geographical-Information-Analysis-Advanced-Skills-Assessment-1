## ArcPy

This practical utilises a Python script using ArcPy to access the same functionality from the ArcGIS Python environment

The Python script is then added to an ArcToolbox so it can be run from there 

The model created is named the "Model1" and can be found in the toolbox provided in this folder "Toolbox.tbx"

Running the script calls the model and passes it 4 arguments

These arguments are:

1. The shape file for the explosion 

2. The buffer distance

3. The shape file for the buildings

4. The output shape file. The output is the intersection of the buffer and the buildings 


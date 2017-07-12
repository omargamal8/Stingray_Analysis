This is a repo made specifically to create performance test scripts to analyze the Stingray library.
How this repo is structured is as follow:
For each module in Stingray there will be a folder in this repo that contain all its testing scripts.
In the folder you can find subfolders for each method contained in the module.
In each of the subfolder you will find a script named 'SingleTest.py' which contains the code that tests and records the time taken to call the method being tested.

For example the Lightcurve module.
There is a main folder name 'Lightcurve', in the Lightcurve folder you can find subfolders for each method found in Lightcurve class.
For instance, you can see the __init__ folder, in the __init__ folder you will find the SingleTest.py script which tests the Lightcurve __init__ method.
For each method, the results are saved in the consequent 'TimeProfiles' folder in the plotting_values.txt

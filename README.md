This is a repo made specifically to create performance test scripts to analyze the Stingray library.
How this repo is structured is as follow:
For each module in Stingray there will be a folder in this repo that contain all its testing scripts.
In the folder you can find subfolders for each method contained in the module.
In each of the subfolder you will find a script named 'SingleTest.py' which contains the code that tests and records the time taken to call the method being tested.

For example the Lightcurve module.
There is a main folder name 'Lightcurve', in the Lightcurve folder you can find subfolders for each method found in Lightcurve class.
For instance, you can see the \__init__ folder, in the \__init__ folder you will find the SingleTest.py script which tests the Lightcurve \__init__ method.
For each method, the results are saved in the consequent 'TimeProfiles' folder in the plotting_values.txt with a plotted Graph which represents the analyzed time complexity.

You can go right to the Summary folders to see the results of the analysis generated. Every class has its own plot with all its method's results are combined.

There are two ways to run the tests.
1. Run all scripts by running the "RunAllTests.py"
2. Run a single test by going to the appropriate method directory and find its "SingleTest.py"
   You then should run the script and specify its arguments (base and power). The script will run a test with using the size of base*10^power.
   For example if we want to tests the lightcurve.\__init__ We would go to the ./Lightcurve/\__init__/ directory.
   Then run `python SingleTest.py 1 4` which would run the test with a Lightcurve of size 1 * 10^4 which is equal to (10,000).
    

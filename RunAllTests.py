import os
from TimeContinuousTester import ContinuousTester
import plotter


def findSingleTest(dir,depth=0):
	paths = []
	if "SingleTest.py" in os.listdir(dir):
		return [dir]
	else:
		if(depth >3):
			return None
		subdirs = [subdir for subdir in os.listdir(dir) if os.path.isdir(dir+subdir)]
		for subdir in subdirs:
			returned_paths = findSingleTest(dir+subdir+"/", depth+1)
			if returned_paths != None:
				paths = paths + (returned_paths)
		return paths		

current_dir = os.getcwd()
# current_dir +='/Lightcurve'
modules = [dir for dir in os.listdir(current_dir) if os.path.isdir(current_dir+'/'+dir) if not dir == ".git" if not dir == "__pycache__"]
modules = [modules[1]]
print(modules)
# print(modules)

for module in modules:
		print("Module",module)
		module_fullpath = current_dir + '/' + module + '/'
		SingleTests = findSingleTest(module_fullpath)
		if SingleTests == None:
			print("SingleTest.py not found in " + module)
			continue
		else:
			print(SingleTests)
			for SingleTest in SingleTests:

				print("Testing "+ SingleTest)
				Tester = ContinuousTester(4,6,9)
				# Tester.runTests(SingleTest)
				# Tester.testAndWrite(SingleTest)
				plotter.plotAndSaveFromRaw(SingleTest+"/TimeProfiles/plotting_values.txt")


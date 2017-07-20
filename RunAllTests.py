import os
from TimeContinuousTester import ContinuousTester
import plotter


def findSingleTest(dir,depth=0, keyword = "SingleTest.py"):
	paths = []
	if keyword in os.listdir(dir):
		return [dir]
	else:
		if(depth >3):
			return None
		subdirs = [subdir for subdir in os.listdir(dir) if os.path.isdir(dir+subdir)]
		for subdir in subdirs:
			returned_paths = findSingleTest(dir+subdir+"/", depth+1, keyword)
			if returned_paths != None:
				paths = paths + (returned_paths)
		return paths		


if __name__ == '__main__':
	current_dir = os.getcwd()
	# current_dir +='/Lightcurve'
	modules = [dir for dir in os.listdir(current_dir) if os.path.isdir(current_dir+'/'+dir) if not dir == ".git" if not dir == "__pycache__"]
	modules = [modules[0]]
	print(modules)
	# print(modules)

	for module in modules:
			print("Module",module)
			module_fullpath = current_dir + '/' + module + '/'
			SingleTests = findSingleTest(module_fullpath)
			SingleTests = [module_fullpath+'coherence/Static_SegmentSize/',module_fullpath+'time_lag/Static_SegmentSize/']
			if SingleTests == None or SingleTests==[]:
				print("SingleTest.py not found in " + module)
				continue
			else:
				print(SingleTests)
				# for SingleTest in SingleTests:
				# 	print("Testing "+ SingleTest)
				# 	Tester = ContinuousTester(4,4,9)
				# 	Tester.testAndWrite(SingleTest)
					# plotter.plotAndSaveFromRaw(SingleTest+"/TimeProfiles/plotting_values.txt")
			print("Plots in Module")
			plotter.plotGroup(module_fullpath)

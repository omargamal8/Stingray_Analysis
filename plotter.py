import matplotlib.pyplot as plt
from collections import OrderedDict
import sys

def test_value_gen():
	base = 1
	power = 4
	while(True):
		yield base * ( 10 ** power)
		base += 1
		if(base == 10):
			base = 1
			power+=1

def dictToLists(dict):
	keys= []
	values= []
	for key in dict:
		keys.append(key)
		values.append(dict[key])
	return[list(dict.keys()),list(values)]	

def _readValues(path):
	input_file = open(path, "r")
	print("Input Path", input_file)
	lines = input_file.readlines()
	values = OrderedDict()
	input_file.close()

	for line in lines:
	   if line == "\n":
	   	continue
	   print("__line:",line)
	   bins,value = line.split(':')
	   print("bins: "+bins+" : value "+value)
	   value = float(value)
	   bins = int(bins)
	   bins/=1000 
	   values[bins] = float(value)
	print(values.values())
	return values

def plotAndSaveFromRaw(path):
	values = _readValues(path)
	valkeys = dictToLists(values)
	plt.clf()
	# print(valkeys[1])
	plt.plot(valkeys[0], valkeys[1],'b')
	plt.xlabel("bins  1:1000")
	plt.ylabel("seconds")
	input_dirs = path.split('/')[:-1]
	output_dir = ""
	for dir in input_dirs:
		output_dir+=dir+"/"		
	plt.savefig(output_dir+"timefig.png")

def nextColor():
	colors = ['b','m','y','k','b--','m--','y--','k--','r','g','r--','g--']
	for color in colors:
		yield color
def plotGroup(topDir):
	# print("top dir:",topDir)
	# return
	from RunAllTests import findSingleTest
	colors = nextColor()
	paths = findSingleTest(topDir, keyword="plotting_values.txt")
	legend = []
	laf=0
	for path in paths:
		laf+=1
		print(laf)
		values = _readValues(path+'/plotting_values.txt')
		valkeys = dictToLists(values)
		plt.plot(valkeys[0], valkeys[1], next(colors))
		subdirs = path.split('/')
		label = ""
		for i, subdir in enumerate(subdirs):
			if(i > subdirs.index(topDir.split('/')[-2]) and subdir != path.split('/')[-2]):
				label+= subdir+" "
		legend.append(label)
	plt.xlabel("bins 1:1000")
	plt.ylabel("seconds")
	plt.suptitle(topDir.split('/')[-2])
	plt.legend(legend)
	plt.show()

if __name__ == "__main__":
	arguments = sys.argv
	if(len(arguments)>1):
		input_path = arguments[1]
	else:
		input_path = input("plotting values dir  ")
		save = input("if you want to save the figure enter '-s'  ")
		if(save == '-s'):
			arguments.append('-s')
	
	input_path += "plotting_values.txt"


	if('-s' in arguments):
		plotAndSaveFromRaw(input_path)

	else:
		values1 = _readValues(input_path)
		# print("aa")
		# print(values1.keys())
		# print(values1.values())
		valkeys1 = dictToLists(values1)
		plt.clf()

		# values2 = readValues("./plotting_values_worst.txt")
		# valkeys2 = dictToLists(values2)

		# values3 = readValues("./plotting_values_best.txt")
		# valkeys3 = dictToLists(values3)


		# # plt.plot(valkeys1[0],valkeys1[1],'b')
		# plt.plot(valkeys2[0][:len(valkeys1[0])],valkeys2[1][:len(valkeys1[0])],'y--')
		# plt.plot(valkeys3[0][:len(valkeys1[0])],valkeys3[1][:len(valkeys1[0])],'g')

		# plt.plot(valkeys2[0],valkeys2[1],'b')
		# plt.plot(valkeys3[0],valkeys3[1],'y--')

		plt.plot(valkeys1[0],valkeys1[1],'b')	

		plt.xlabel("bins  1:1000")
		plt.ylabel("seconds")
		plt.show()

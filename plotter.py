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
	return[keys,values]	

def readValues(path):
	input_file = open(path, "r")
	lines = input_file.readlines()
	values = OrderedDict()
	input_file.close()

	key_gen = test_value_gen()
	for line in lines:
	   if line == "\n":
	   	continue
	   values[next(key_gen)/10 ** 3] = float((line.split(':')[1]))
	return values

def plotAndSaveFromRaw(path):
	values = readValues(path)
	valkeys = dictToLists(values)
	plt.clf()
	plt.plot(valkeys[0], valkeys[1],'b')
	plt.xlabel("bins  1:1000")
	plt.ylabel("seconds")
	input_dirs = path.split('/')[:-1]
	output_dir = ""
	for dir in input_dirs:
		output_dir+=dir+"/"		
	plt.savefig(output_dir+"timefig.png")

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
		values1 = readValues(input_path)
		valkeys1 = dictToLists(values1)

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

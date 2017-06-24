import sys
from collections import OrderedDict


def printdict(dict):
	for key in dict.keys():
		print(key, dict[key])

def writeResults(dict):
	output_path = "./TimeProfiles/plotting_values.txt"
	output_file = open(output_path, "a")
	for key in dict.keys():
		strToBeWritten = str(key) + ":" + str(dict[key])
		output_file.write(strToBeWritten+'\n')
	output_file.close()

test_arg = sys.argv
if(len(test_arg)<=1):
	initial_power = int(input("Initial Power:"))
	final_power = int(input("Final Power:"))
	upper_base = int(input("Final Base:"))
else:
	initial_power = int(test_arg[1])
	final_power = int(test_arg[2])
	upper_base = int(test_arg[3])

import SingleTest

power = initial_power
attempts = 1
times = OrderedDict()

print("Starting Shift Tests")
while(power <= final_power):
	if(power == final_power):
		final_base = upper_base+1
	else:
		final_base = 10

	for base in range(1,final_base):
		accumulative_time = 0
		print(str(base) + " * 10^" + str(power) + ":")

		for attempt in range(attempts):
			print("attempt:", attempt)
			time = SingleTest.singleTest(base, power)
			accumulative_time += time

		avg_time = accumulative_time/attempts
		print(avg_time,"\n")
		times[base*(10 ** power)] = avg_time
	power+=1


printdict(times)
if(len(test_arg) > 4):
	if(test_arg[4] == 'w'):
		writeResults(times)
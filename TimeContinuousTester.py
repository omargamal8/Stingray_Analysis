import sys
import os
from collections import OrderedDict

class ContinuousTester:
	def __init__(self,initial_power=4,final_power=7,final_base=9):
		self.initial_power = initial_power
		self.final_power = final_power
		self.upper_base = final_base

	def printdict(self,dict):
		for key in dict.keys():
			print(key, dict[key])

	def writeResults(self,dict,dir):
		if not (os.path.isdir(dir+"/TimeProfiles")):
			os.mkdir(dir+"/TimeProfiles")
		output_path = dir + "/TimeProfiles/plotting_values.txt"
		output_file = open(output_path,"w")
		for key in dict.keys():
			strToBeWritten = str(key) + ":" + str(dict[key])
			output_file.write(strToBeWritten+'\n')
		output_file.close()

	def appendResult(self,key,value,dir):
		if not (os.path.isdir(dir+"/TimeProfiles")):
			os.mkdir(dir+"/TimeProfiles")
		output_file_path = dir+"/TimeProfiles/backup.txt"
		output_file = open(output_file_path,"a")
		output_file.write(str(key)+":"+str(value)+"\n")
		output_file.close()

	def runTests(self,Single_Test_Dir):
		print("Run Tests!! for dir ",Single_Test_Dir)

		sys.path.append(Single_Test_Dir)
		# print("+++++++++++++++++",sys.path)
		import SingleTest

		power = self.initial_power
		attempts = 1
		times = OrderedDict()

		print("Starting"+ Single_Test_Dir.split("/")[-1] + " Tests")

		while(power <= self.final_power):
			if(power == self.final_power):
				final_base = self.upper_base+1
			else:
				final_base = 10

			for base in range(1,final_base):
				try:
					accumulative_time = 0
					succeded_times = 0

					print(str(base) + " * 10^" + str(power) + ":")

					for attempt in range(attempts):
						print("attempt:", attempt)
						time = SingleTest.singleTest(base, power)
						succeded_times+=1
						accumulative_time += time
						if( time >= 700):
							break

					avg_time = accumulative_time/attempts
					print(avg_time,"\n")
					times[base*(10 ** power)] = avg_time
					self.appendResult(base*(10 ** power),avg_time,Single_Test_Dir)
				except MemoryError:
					print("Memory errored, submitting results..")
					break
					
			power+=1

		del sys.modules["SingleTest"]
		sys.path.pop(sys.path.index(Single_Test_Dir))
		# print(sys.path)
		self.printdict(times)
		return times

	def testAndWrite(self,Single_Test_Dir):
		results = self.runTests(Single_Test_Dir)
		self.writeResults(results,Single_Test_Dir)
if __name__ == "__main__":

	test_arg = sys.argv
	Single_Test_Dir = os.getcwd()
	if(len(test_arg)<=1):
		initial_power = int(input("Initial Power:"))
		final_power = int(input("Final Power:"))
		upper_base = int(input("Final Base:"))
		write = input("enter \"-w\" if you want to write the results ")
		test_arg.append(write)
		Single_Test_Dir = input("Single test dir ")
	else:
		try:
			initial_power = int(test_arg[1])
			final_power = int(test_arg[2])
			upper_base = int(test_arg[3])
			if("-p" in test_arg):
				index = test_arg.index("-p")
				Single_Test_Dir = test_arg[index+1]
		except:
			print("Enter correct options")

			sys.exit()
	Tester = ContinuousTester(initial_power, final_power, upper_base)
	times = Tester.runTests(Single_Test_Dir)

	if('-w' in test_arg):
		Tester.writeResults(times, Single_Test_Dir)


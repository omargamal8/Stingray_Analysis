import SingleTest
import sys

test_arg = sys.argv
if(len(test_arg)<=1):
	initial_power = int(input("Initial Power:"))
	final_power = int(input("Final Power:"))
	final_base = int(input("Final Base:"))
else:
	initial_power = int(test_arg[1])
	final_power = int(test_arg[2])
	final_base = int(test_arg[3])

f = open("./TimeProfiles/Snaps_Results.txt","a")
for power in range(initial_power,final_power+1):
	if (power == final_power):
		base = final_base
	else:
		base = 1
	res = SingleTest.singleTest(base,power)
	print(res)
	f.write(str(base)+" * ten pw " + str(power)+":"+str(res)+"\n")
f.close()
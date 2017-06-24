import matplotlib.pyplot as plt
from collections import OrderedDict

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

input_path = "./plotting_values.txt"
input_file = open(input_path, "r")

lines = input_file.readlines()
values = OrderedDict()
input_file.close()

key_gen = test_value_gen()
for line in lines:
   if line == "\n":
   	continue
   values[next(key_gen)/10 ** 3] = float((line.split(' ')[1]))

valkeys = dictToLists(values)
plt.plot(valkeys[0],valkeys[1])
plt.xlabel("bins  1:1000")
plt.ylabel("seconds")
plt.show()

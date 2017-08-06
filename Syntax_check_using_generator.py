import stingray_parallel
import numpy as np
class _class:
	def _make_cross(self,gen_obj):
		self.gen_obj = gen_obj
		self.member_att = 3
		self.big_fn(next(self.gen_obj))
	def big_fn(self,a):
		function_attr = 9
		member_att = self.member_att
		def work_fn(noth):
			print("working on:", noth)
			print("I see func_attr:",function_attr)
			print("I also see this:", member_att)
			return
		stingray_parallel.execute_parallel(work_fn, [lambda noth:None],a)

def generator():
	arr = [np.arange(10),[np.arange(10)]]
	i = 0
	yield arr[i]
	i+=1
my_class = _class()
my_class._make_cross(generator())
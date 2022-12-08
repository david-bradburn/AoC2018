#################################################################
###### https://adventofcode.com/2018/day/3 ######################
#################################################################

import re

file = "test.txt"

DAY_NO = "3"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = []
for line in rawInput:
	# print(line)
	temp = line.strip('\n')
	print(temp)
	temp = re.split('#| @ |,|: |x', temp)
	cleanerInput.append([temp[1], temp[2], temp[3], temp[4], temp[5]])
	# print(temp)
print(cleanerInput)

class Fabric():

	def __init__(self, input) -> None:
		self.claims = input


p1 = Fabric(cleanerInput)
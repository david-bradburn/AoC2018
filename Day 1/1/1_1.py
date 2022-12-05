#################################################################
###### https://adventofcode.com/2018/day/1 ######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

total = 0

for change in raw_input:
	sign = change[0]
	striped_input = int(change[1:].strip('\n'))
	if sign == '+':
		total += striped_input
	elif sign == '-':
		total -= striped_input
	else:
		raise Exception
	

print(total)
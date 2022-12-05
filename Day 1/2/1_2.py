#################################################################
###### https://adventofcode.com/2018/day/1 ######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

total = 0
frequencyList = []
frequencyRepeat = True
while frequencyRepeat:
	for change in raw_input:
		sign = change[0]
		striped_input = int(change[1:].strip('\n'))
		if sign == '+':
			total += striped_input
		elif sign == '-':
			total -= striped_input
		else:
			raise Exception

		if total not in frequencyList:
			frequencyList.append(total)
			# print(frequencyList)
		else:
			print("Frequency seen before {}".format(total))
			frequencyRepeat = False
			break
	print(total)
	

print(total)
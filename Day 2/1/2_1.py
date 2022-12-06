#################################################################
###### https://adventofcode.com/2018/day/2 ######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [row.strip('\n') for row in rawInput]
print(cleanerInput)

class Boxes():

	def __init__(self, input) -> None:
		self.twosTotal = 0
		self.threesTotal = 0

		self.idData = input

		self.main()

	
	def processID(self, id):
		tempIdDict = {}
		for no in range(len(id)):
			if id[no] not in tempIdDict:
				tempIdDict[id[no]] = 1
			else:
				tempIdDict[id[no]] += 1
		
		print(tempIdDict)
		self.countNoOccurences(tempIdDict)
		print(self.twosTotal)
		print(self.threesTotal)
		
	def countNoOccurences(self, idDict):
		twoFound = False
		threeFound = False
		for key in idDict:
			if (idDict[key] == 2) and not twoFound:
				self.twosTotal += 1
				twoFound = True

			if (idDict[key] == 3) and not threeFound:
				self.threesTotal += 1
				threeFound = True

	def main(self):

		for id in self.idData:
			self.processID(id)
		
		print(self.twosTotal * self.threesTotal)

p1 = Boxes(cleanerInput)
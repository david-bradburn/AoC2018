#################################################################
###### https://adventofcode.com/2018/day/13 #####################
#################################################################

import numpy as np

file = "test2.txt"

DAY_NO = "13"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"
train_dict = {}
train_index = 0


with open(file_path_base + file, "r") as fd:
	raw = fd.readlines()

cleaner_input = []
for line in raw:
	cleaner_input += [line.strip('\n')]

raw_len_y = len(cleaner_input)
raw_len_x = len(cleaner_input[0])

track_map = np.empty((raw_len_y, raw_len_x), dtype=str)
train_map = np.empty_like(track_map, dtype='O')

class train():

	def __init__(self, st_direction) -> None:

		self.current_direction = st_direction
		self.next_direction_arr = ['l', 's', 'r']
		self.next_direction_index = 0

		self.next_corssing_direction = self.next_direction_arr[self.next_direction_index]

	def update_next_crossing(self):
		self.next_direction_index += 1
		if self.next_direction_index > 2:
			self.next_direction_index = 0

		self.next_corssing_direction = self.next_direction_arr[self.next_direction_index]
	
	def update_direction_train(self, new_direction):
		self.current_direction = new_direction



for row_index, row in enumerate(cleaner_input):
	assert len(row) == raw_len_x

	for column_index, value in enumerate(row):
		match value:
			case '<':
				train_map[row_index][column_index] = train('<')
				track_map[row_index][column_index] = '-'
				
			case '>':
				
				train_map[row_index][column_index] = train('>')
				track_map[row_index][column_index] = '-'
				
			case '^':
				
				train_map[row_index][column_index] = train('^')
				track_map[row_index][column_index] = '|'
				
			case 'v':
				train_map[row_index][column_index] = train('v')
				track_map[row_index][column_index] = '|'
				
			case _:
				track_map[row_index][column_index] = cleaner_input[row_index][column_index] ## no train here

##^^ input processing




def find_next_direction(direction: str, location: list):

	## figure out what is the next track type -/\|+
	match direction:
		case "<":
			next_track_type = track_map[location[0]-1][location[1]]
		
		case ">":
			next_track_type = track_map[location[0]+1][location[1]]
		
		case "^":
			next_track_type = track_map[location[0]][location[1]-1]

		case "v":
			next_track_type = track_map[location[0]][location[1]+1]

	
	match next_track_type:
		case "-":
			new_direction = direction
			assert new_direction in ['<', '>']
		
		case "|":
			new_direction = direction
			assert new_direction in ['^', 'v']
		
		case "/":
			match direction:
				case "<":
					new_direction = "v"
				case ">":
					new_direction = "^"
				case "^":
					new_direction = ">"
				case "v":
					new_direction = "<"

		case "\\":
			match direction:
				case "<":
					new_direction = "^"
				case ">":
					new_direction = "v"
				case "^":
					new_direction = ">"
				case "v":
					new_direction = "<"
		
		case "+":
			match train_map[location[0]][location[1]].next_crossing_direction:
				case 'l':
					match direction:
						case "<":
							new_direction = "v"
						case ">":
							new_direction = "^"
						case "^":
							new_direction = "<"
						case "v":
							new_direction = ">"
				case 's':
					new_direction = direction

				case 'r':
					match direction:
						case "<":
							new_direction = "^"
						case ">":
							new_direction = "v"
						case "^":
							new_direction = ">"
						case "v":
							new_direction = "<"
			
			train_map[location[0]][location[1]].update_next_crossing()

	return new_direction

def run_tick():
	new_train_map = np.empty_like(train_map, dtype = 'O')
	for row_index, row in enumerate(train_map): # one tick
		for colum_index, value in enumerate(row):
			match value:
				case None:
					pass
				
				case _:
					cur_dr = train_map[colum_index][row_index]
					new_dr = find_next_direction(cur_dr, [colum_index,row_index])
					







			


print(track_map)
print(train_map)


	
	# print(test)
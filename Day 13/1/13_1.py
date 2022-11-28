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

test = []
for line in raw:
	test += [line.strip('\n')]

raw_len_y = len(test)
raw_len_x = len(test[0])

track_map = np.empty((raw_len_y, raw_len_x), dtype=str)
train_map = np.zeros_like(track_map, dtype=str)
for row_index, row in enumerate(test):
	assert len(row) == raw_len_x
	for column_index, value in enumerate(row):
		match value:
			case '<':
				train_map[row_index][column_index] = 'l'
				track_map[row_index][column_index] = '-'
				
			case '>':
				
				train_map[row_index][column_index] = 'r'
				track_map[row_index][column_index] = '-'
				
			case '^':
				
				train_map[row_index][column_index] = 'u'
				track_map[row_index][column_index] = '|'
				
			case 'v':
				train_map[row_index][column_index] = 'd'
				track_map[row_index][column_index] = '|'
				
			case _:
				track_map[row_index][column_index] = test[row_index][column_index]



def update_direction(direction, location):
	match direction:
		case "l":
			next_track = track_map[colum_index-1][row_index]
		
		case "r":
			next_track = track_map[colum_index-1][row_index]

	return new_direction


for row_index, row in enumerate(train_map): # one tick
	for colum_index, value in enumerate(row):
		match value:
			case '':
				pass:
			
			case 'l':

				track_map[colum_index-1][row_index]







			


print(track_map)
print(train_map)


	
	# print(test)
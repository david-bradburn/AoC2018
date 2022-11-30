#################################################################
###### https://adventofcode.com/2018/day/13 #####################
#################################################################

import numpy as np

file = "input.txt"

DAY_NO = "13"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"



with open(file_path_base + file, "r") as fd:
	raw = fd.readlines()

cleaner_input = []
for line in raw:
	cleaner_input += [line.strip('\n')]

raw_len_y = len(cleaner_input)
raw_len_x = len(cleaner_input[0])


class train():

	def __init__(self, st_direction) -> None:

		self.current_direction = st_direction
		self.next_direction_arr = ['l', 's', 'r']
		self.next_direction_index = 0
		self.state = True

		self.next_crossing_direction = self.next_direction_arr[self.next_direction_index]

	def update_next_crossing(self):
		self.next_direction_index += 1
		if self.next_direction_index > 2:
			self.next_direction_index = 0

		self.next_crossing_direction = self.next_direction_arr[self.next_direction_index]
	
	def update_direction_train(self, new_direction):
		self.current_direction = new_direction

	def explode(self):
		self.state = False

	def display_representation(self):
		if self.state:
			return self.current_direction
		else:
			return 'x'


class world_map:
	def __init__(self, raw_len_y, raw_len_x, cleaner_input) -> None:
		self.y_world_size = raw_len_y
		self.x_world_size = raw_len_x
		self.track_map = np.empty((raw_len_y, raw_len_x), dtype=str)
		self.train_map = np.empty_like(self.track_map, dtype='O')
		self.init_input = cleaner_input
		self.colision_detected = False
		self.tick_counter = 0
		self.train_sum = 0
		self.no_of_trains = 0
		
		self.main()

	
	def process_input(self):
		for row_index, row in enumerate(self.init_input):
			assert len(row) == self.x_world_size

			for column_index, value in enumerate(row):
				match value:
					case '<':
						self.train_map[row_index][column_index] = train('<')
						self.no_of_trains += 1
						self.track_map[row_index][column_index] = '-'
						
					case '>':
						self.train_map[row_index][column_index] = train('>')
						self.no_of_trains += 1
						self.track_map[row_index][column_index] = '-'
						
					case '^':
						self.train_map[row_index][column_index] = train('^')
						self.no_of_trains += 1
						self.track_map[row_index][column_index] = '|'
						
					case 'v':
						self.train_map[row_index][column_index] = train('v')
						self.no_of_trains += 1
						self.track_map[row_index][column_index] = '|'
						
					case _:
						self.track_map[row_index][column_index] = cleaner_input[row_index][column_index] ## no train here

		##^^ input processing
	
	def find_next_direction(self, direction: str, location: list):

		## figure out what is the next track type -/\|+
		match direction:
			case "<":
				next_track_type = self.track_map[location[0]][location[1]-1]
				next_location = [location[0], location[1]-1]
			
			case ">":
				next_track_type = self.track_map[location[0]][location[1]+1]
				next_location = [location[0], location[1]+1]
			
			case "^":
				next_track_type = self.track_map[location[0]-1][location[1]]
				next_location = [location[0]-1, location[1]]

			case "v":
				next_track_type = self.track_map[location[0]+1][location[1]]
				next_location = [location[0]+1, location[1]]
			
			case "_":
				print(direction)

		assert next_track_type in ["|", "-", "\\", "/", "+"]
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
						new_direction = "<"
					case "v":
						new_direction = ">"
			
			case "+":
				match self.train_map[location[0]][location[1]].next_crossing_direction:
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
				
				self.train_map[location[0]][location[1]].update_next_crossing()

			case _:
				raise Exception

		return new_direction, next_location



	def run_tick(self):
		self.new_train_map = np.empty_like(self.train_map, dtype = 'O')
		# print(self.train_map)
		for row_index, row in enumerate(self.train_map): # one tick
			for colum_index, value in enumerate(row):
				match value:
					case None:
						pass
					
					case _:
						cur_dr = self.train_map[row_index][colum_index].current_direction
						new_dr, new_loc = self.find_next_direction(cur_dr, [row_index, colum_index])
						self.train_sum += row_index + 1000*colum_index
						self.train_map[row_index][colum_index].update_direction_train(new_dr)
						#udpate location
						if (self.new_train_map[new_loc[0]][new_loc[1]] == None) and (self.train_map[new_loc[0]][new_loc[1]] == None):#no trains in spot
							self.new_train_map[new_loc[0]][new_loc[1]] = self.train_map[row_index][colum_index]
						else:
							self.new_train_map[new_loc[0]][new_loc[1]] = None
							self.train_map[new_loc[0]][new_loc[1]] = None
							self.no_of_trains -= 2
					
		self.train_map = self.new_train_map

	def main(self):
		self.process_input()
		# self.track_display()
		while self.no_of_trains != 1:
			self.run_tick()
			# self.track_display()
			# if (self.tick_counter == 117):
			# 	self.track_display()
			print("Tick {} {}".format(self.tick_counter, self.no_of_trains))
			self.train_sum = 0
			self.tick_counter += 1
		print(self.tick_counter)
		self.track_display()
		for row_index, row in enumerate(self.train_map):
			for column_index, value in enumerate(row):
				if value != None:
					print("{},{}".format(column_index, row_index))


	def track_display(self):
		for row_index, row in enumerate(self.track_map):
			temp = ''
			for column_index, value in enumerate(row):
				if self.train_map[row_index][column_index] != None:
					temp += self.train_map[row_index][column_index].display_representation()
				else:
					temp += value
			print(temp)



world = world_map(raw_len_y, raw_len_x, cleaner_input)




##12365
	
	# print(test)
from first_thing import *
from gen_iii_arrays import *


def calc_iii(em, double_bool, double_all_bool, scale_bool, evolve_bool, custom_offset, gen_number):
	#current integer byte-offset for TRdata
	#TRdata, Emerald starts from 0x310058 = 3211352, TRPoke 0x30B62C = 3192364
	
	#default values
	
	#Emerald
	if(gen_number == 3.2):
		trainer_pointer = 3211352
		#pokemon_pointer =  3192364
		max_trainers = 854
		evolve_array_iii = evolve_array_iii_default
		evolve_level_barrier_array_iii = evolve_level_barrier_array_iii_default
	#FireRed
	elif(gen_number == 3.1):
		trainer_pointer = 2353864 #23EAC8
		#pokemon_pointer =  3192364
		max_trainers = 854
		evolve_array_iii = evolve_array_iii_default
		evolve_level_barrier_array_iii = evolve_level_barrier_array_iii_default
	#Gaia
	elif(gen_number == 3.11):
		trainer_pointer = 2353904 #0x23EAF0
		#pokemon_pointer =  9225576
		evolve_array_iii = evolve_array_iii_gaia
		evolve_level_barrier_array_iii = evolve_level_barrier_array_iii_gaia
	#Ultra Shiny Gold Sigma
	elif(gen_number == 3.12):
		trainer_pointer = 2353904 #0x23EAF0
		evolve_array_iii = evolve_array_iii_usgs
		evolve_level_barrier_array_iii = evolve_level_barrier_array_iii_usgs
	
	#set custom offset if entered
	if(custom_offset != 0):
		#Don't need the pokemon_pointer, Trdata has the pointers anyway
		trainer_pointer = custom_offset
	
	trainer_number = 1
	
	temp_trainer_pointer = trainer_pointer
	back_bool = True
	
	unparsable_pokemon = [0]
	
	
	#find the first TrData endflag (08). Assume that the given address is close the true start of the data
	while True:
		#if offset + 39 is the endflag and the following byte makes sense for the first of the next data (is at most 3
		if(em[trainer_pointer] <= 3 and em[trainer_pointer + 39] == 8 and em[trainer_pointer + 40] <= 3):
			break
		#jump back one
		elif(back_bool and trainer_pointer != 0):
			trainer_pointer += 1
		#if got to start of file, go back to where we started and search forwards
		elif(back_bool and trainer_pointer == 0):
			back_bool = False
			trainer_pointer = temp_trainer_pointer
		#otherwise, parse forwards
		else:
			trainer_pointer -= 1
			
	print(trainer_pointer)
	#Now we know with reasonable certainty that we are pointing to the start of Trdata.
	
	#increment the ith place by one for each occurence of the level i
	max_level_array = [0]*101
	
	level_array = []
	
	gaia_double_error_check = True
	
	#iterate over trainers
	while True:
		#get the number of Pokemon the trainer has
		number_pokemon = em[trainer_pointer + 32]
	
		#Induce Double Battles as per options
		
		#get trainer name for Gaia
		if(gen_number == 3.11 and (double_bool or double_all_bool)):
			trainer_name_array = [em[trainer_pointer + 4], em[trainer_pointer + 5], em[trainer_pointer + 6], em[trainer_pointer + 7], em[trainer_pointer + 8], em[trainer_pointer + 9], em[trainer_pointer + 10], em[trainer_pointer + 11]]
			#check if name is one of the error-names
			for arr in double_not_set_gaia:
				if(array_equality(trainer_name_array, arr)):
					gaia_double_error_check = False
		
		#Major trainers
		if(double_bool and trainer_number in doubles_set_emerald and number_pokemon >= 2):
			#don't modify if already set to double battle
			if(em[trainer_pointer + 24]%2 != 1):
				em[trainer_pointer + 24] += 1
		#Anyone with enough Pokemon
		if(double_all_bool and number_pokemon >= 2):
			if(em[trainer_pointer + 24]%2 != 1):
				if(gen_number != 3.11):
					em[trainer_pointer + 24] += 1
				#avoid glitches in Gaia
				elif(gaia_double_error_check):
					em[trainer_pointer + 24] += 1
				else:
					print("Trainer name-code", trainer_name_array, "Index Number", trainer_number, "not doubled")
		
		
		if(scale_bool or evolve_bool):
			#Do the Pokemon have hold items? Custom moves?
			extra_type = em[trainer_pointer]
			
			#none or custom hold items but not moves
			if(extra_type == 0 or extra_type == 2):
				pokemon_length = 8
			#custom moves but no items
			elif(extra_type == 1):
				if(gen_number == 3.11):
					pokemon_length = 14
				else:
					pokemon_length = 14
			elif(extra_type == 3):
			#hold items and custom moves
				pokemon_length = 16
			else:
				print("Trainer data error - incorrect value or incorrect pointer")
			
			
			
			#get the pointer to the trainer's first Pokemon (to check against iterated value)
			pokemon_pointer = em[trainer_pointer + 36] + 256*em[trainer_pointer + 37] + 65536*em[trainer_pointer + 38]
			
			extra_bytes = em[trainer_pointer + 39]
			
			if(extra_bytes >= 9):
				extra_bytes = (extra_bytes - 8)*16777216
				pokemon_pointer += extra_bytes
			
			
			if(gen_number != 3.11):
				next_trainer_pointer = em[trainer_pointer + 36 + 40] + 256*em[trainer_pointer + 37 + 40] + 65536*em[trainer_pointer + 38 + 40]
				
				if(extra_bytes >= 9):
					extra_bytes = (extra_bytes - 8)*16777216
					next_trainer_pointer += extra_bytes
					
				allocated_team_length = next_trainer_pointer - pokemon_pointer
				
				allocated_pokemon_length = allocated_team_length/number_pokemon
				
				if(allocated_pokemon_length.is_integer()):
					if(allocated_pokemon_length != pokemon_length):
						if(allocated_pokemon_length == 8 or allocated_pokemon_length == 16 or allocated_pokemon_length == 14):
							print("Correcting length from", pokemon_length, "to", allocated_pokemon_length)
							pokemon_length = int(allocated_pokemon_length)
			#else:
			#	print("Does not work")
			
			
				
			
			
			#print("trainer", trainer_number, "has", number_pokemon, "Pokemon, each", pokemon_length, "long")
			
			#iterate over that trainer's Pokemon
			while True:
				
				
				
				#avoids glitch if there's a zeroed-out trainer
				if(pokemon_pointer == 0):
					break
					
					
				#get level
				level = em[pokemon_pointer + 2]
				#print("Level", level)
				#use level * (1 + level/50) = (level + (level^2/50)) = (50 * level + level ^2)/50. Level 10 has (500 + 100)/50 = 600/50 = 60/5 = 12, level 20 has 20*1.4 = 28, level 30 has 30*1.6 = 48, level 40 has 40*1.8 = 72, 50*2 = 100
				
				#final check for incorrect values. either level that is too high or too low, or the after-level spot is not 0. The only thing the latter seems to have been causing was turning Roselias into Spheals and Dusclops into Glalies.
				if(level == 0 or level > 100): #or em[pokemon_pointer + 2 + 1] != 0):
					print("Found level of", level, "at", pokemon_pointer + 2, "trainer number", trainer_number)
					
					#Some trainers seem to have allocated space different than expected. If this is the case for the last Pokemon of a trainer, it does not matter, it will be caught by the pointer of the next trainer
					
					
					if(pokemon_length == 14):
						#Check the position if length should have been 16
						level = em[pokemon_pointer + 2 + 2]
						if((level > 0 or level <= 100) and em[pokemon_pointer + 2 + 2 + 1] == 0):
							#print("Found a 16 that was encoded as 14")
							pokemon_pointer += 2
						#check if length 8 works
						else:
							level = em[pokemon_pointer + 2 - 6]
							if((level > 0 or level <= 100) and em[pokemon_pointer + 2 - 6 + 1] == 0):
								#print("Found an 8 that was encoded as 14")
								pokemon_pointer -= 6
								
					#check for encoded-as-16 that is incorrect
					elif(pokemon_length == 16):
						#check if 14 works
						level = em[pokemon_pointer + 2 - 2]
						if((level > 0 or level <= 100) and em[pokemon_pointer + 2 - 2 + 1] == 0):
							#print("Found a 14 that was encoded as 16")
							pokemon_pointer -= 2
						
						#otherwise check if 8 works
						else:
							level = em[pokemon_pointer + 2 - 8]
							if((level > 0 or level <= 100) and em[pokemon_pointer + 2 - 8 + 1] == 0):
								#print("Found an 8 that was encoded as 16")
								pokemon_pointer -= 8
								
					#check for encoded-as-8 that is incorrect
					else:
						#check if 14 works (check this first, in this case, if 14 is also wrong it will be the low EV value, which is rarely if ever in the level range, while if 16 is wrong it will be the low index value, which is often in the level range
						
						level = em[pokemon_pointer + 2 + 6]
						if((level > 0 or level <= 100) and em[pokemon_pointer + 2 + 6 + 1] == 0):
							#print("Found a 14 that was encoded as 8")
							pokemon_pointer += 6
						
						#otherwise check if 16 works
						else:
							level = em[pokemon_pointer + 2 + 8]
							if((level > 0 or level <= 100) and em[pokemon_pointer + 2 + 8 + 1] == 0):
								#print("Found a 16 that was encoded as 8")
								pokemon_pointer += 8
					print("Modified Level to:", level)	
				
				#final catch for incorrectly parsed Pokemon Data
				try:
					if(level <= 100 and level > 0):
						#this is for Gaia for now, the Pokemon greater than 60 aren't available yet
						if(gen_number == 3.11):
							if(level <= 60):
								#record the current level
								max_level_array[level] += 1
								
								#keep track of highest level
								if(max_level_array[0] < level):
									max_level_array[0] = level
						
								#record pointer to current level
								level_array.append(pokemon_pointer)
								
						else:
							#record the current level
							max_level_array[level] += 1
							
							#keep track of highest level
							if(max_level_array[0] < level):
								max_level_array[0] = level
							
							#record pointer to current level
							level_array.append(pokemon_pointer)
					else:
						print("Could not parse this Pokemon, skipping.")
						unparsable_pokemon[0] += 1
						unparsable_pokemon.append(pokemon_pointer)
				except:
					print("Could not parse this Pokemon, skipping.")
					unparsable_pokemon[0] += 1
					unparsable_pokemon.append(pokemon_pointer)
				
					
				#decrement party count of current trainer
				number_pokemon -= 1
				
				#checks if finished with current trainer, if so, break. If not, everything is set up for next iteration
				if(number_pokemon == 0):
					break
				else:
					pokemon_pointer += pokemon_length
					
			
				
		trainer_pointer += 40 #0x28
		trainer_number += 1
		gaia_double_error_check = True
		
		
		#since each trainer-data has an end flag of 0x08, we just stop when the current trainer pointer + 39 is not 0x08
		#Some hacks seems to have 0x02 and 0x09 end flags as well. The 0x09 uses the lowest byte for larger pointers.
		
		
			
		if(em[trainer_pointer + 39] != 2 and em[trainer_pointer + 39] != 8 and em[trainer_pointer + 39] != 9):
			#USGS has garbage data in the middle, ignore that by skipping two more
			if(gen_number == 3.12 and trainer_pointer < 2389607):
				trainer_pointer += 80 #0x28
				trainer_number += 2
			else:
				print("First non-end flag at", trainer_pointer + 39)
				print(trainer_number - 1, "trainers")
				break
		if(gen_number == 3.12 and trainer_number > 873):
			print("First non-end flag at", trainer_pointer + 39)
			print(trainer_number - 1, "trainers")
			break
		
	#this is for Gaia for now, the Pokemon greater than 60 aren't available yet
	if(gen_number == 3.11):
		print("If you are seeing this and you're modifying Gaia Version 4 of or higher, please download the new version or contact me to update")
	
	meanmaxarr = 0
	div = 0
	#get average level
	for x in range(1,min(max_level_array[0] + 1,100)):
		meanmaxarr += max_level_array[x]*x
		div += max_level_array[x]
	
	meanmaxarr = meanmaxarr/div
	
	print("Average level is", meanmaxarr)
	
	temp = []
	#get median
	for x in range(1,min(max_level_array[0] + 1,100)):
		zzz = [x]*max_level_array[x]
		temp.extend(zzz)
	medmaxarr = median(temp)
	
	print("Median level is", medmaxarr)
	
	
	#figure out what to map to 50
	while True:
		#If either is less than 50, use whichever is less
		if(int(medmaxarr) <= 45 or int(meanmaxarr) <= 45):
			level_to_50 = min(medmaxarr, meanmaxarr)
			break
		#otherwise, truncate the top 10% of the level array and use median of that
		else:
			print("Current level curve has median level close to 50. This implies that the level curve might already be rather steep, and in particular that this program might already have been run on it. Will now remove the top percentile of levels from consideration and recalculate. (This message might appear multiple times)")
			
			print("Reducing list from", len(temp), "Pokemon to")
			
			del temp[-int(round(len(temp)/10)):]
			medmaxarr = median(temp)
			
			print(len(temp), "Pokemon.")
			print("The new median is", medmaxarr, ".")
	
	curve_exponent_50 = 0.5
	
	curve_divisor_50 = level_to_50**(1+curve_exponent_50)/(50 - level_to_50)
	
	
	
	
	print('Initially mapping', level_to_50, 'to 50.', 'Curve divisor is', curve_divisor_50)
	
	if(scale_bool):
		#create lookup table for modification
		print("Table as follows:")
		print("Initial Level |", "Output Level")
		
		change_table = [0]*101
		for j in range(1, max_level_array[0] + 1):
			#first scale entire table by the level 50 curve:
			level = j*(1 + (j**curve_exponent_50)/curve_divisor_50)
			level = min(round(level), 100)
			change_table[j] = level
			
		#need to add 100 - change_table[max_level_array[0]]
		addendum = 100 - change_table[max_level_array[0]]
		
		if(addendum > 0):
			iter = 0
			while True:
				#adds the full needed addition to the highest level, then one less than that to the second-highest, etc.
				change_table[min(max_level_array[0] + 2 - iter, 100)] += addendum
				addendum -= 1
				
				#if addendum is now 0, we've added all we needed to
				if(addendum == 0):
					break
				else:
					iter += 1
	
	
		for j in range(1, max_level_array[0] + 1):
			print(j, "|", change_table[j])
	
	modify_count = [0,0]
	for pointer in level_array:
		
		#get level
		level = em[pointer + 2]
		
		#get new level from lookup table
		if(scale_bool):	
			level = change_table[level]
				
		#If the Pokemon should be evolved, evolve it. Will evolve any unevolved Pokemon that is above the minimum level
		
		index = em[pointer + 4] + 256*em[pointer + 5]
		
		#If the Pokemon is past the level it evolves at by level-up
		try:	
			if(level >= evolve_level_barrier_array_iii[index] and evolve_bool):
				new_index = evolve_array_iii[index]
				if(new_index != index):
					
					#convert back to hex pairs & write
					em[pointer + 4] = new_index%256
					try:
						em[pointer + 5] = int((new_index)/256)
					#the above throws an error if the high bytes are 0
					except:
						em[pointer + 5] = 0
					modify_count[0] += 1
				else:
					modify_count[1] += 1
			else:
				modify_count[1] += 1
			#write level now, so that if the index doesn't make sense, we don't write anything
			if(scale_bool):
				em[pointer + 2] = level
		
		except:
			print("Error at ",pointer, index)
	
	print("Evolved", modify_count[0], "out of", modify_count[0] + modify_count[1], "Pokemon")
	
	if(unparsable_pokemon[0] > 0):
		print("A total of", unparsable_pokemon[0], "Pokemon were odd, and could not be parsed. This might be a result of Trainers that were not actually implemented in the game. If there are more than just a few of these, there might be a glitch in this program, or there might be something unusual about the game being modified.")

	

	
	return(em)
	
def get_files_gen_iii():

	#for Emerald, modify .gba directly
	
	#get hex file locations:
	rom_location = askopenfilename(filetypes = (("Select Emerald GBA file", "*.*"), (".GBA", "*.gba")))
	
	
	rom = bytearray()
	
	#get the data
	with open(rom_location, 'rb') as f:
		rom_bin = f.read()
	
	
	#convert the binary data into bytearrays. each index is one hex-pair
	rom = bytearray(rom_bin)
	
	return(rom, rom_location)
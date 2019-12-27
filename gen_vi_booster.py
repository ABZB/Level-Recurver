from first_thing import *
import random

doubles = [4,41,45,53,139,141,142,143,144,145,146,147,148,149,150,151,177]

def calc_vi(trdata, trpoke, scale_bool):

	
	pointer_data = 0
	pointer_poke = 0
	trainer_number = 1
	doubled_count = 0
	
	pokemon_offset_array = [0]
	pokemon_relative_offset = 0
	
	#Search for 42 4D 49 46 (66 77 73 70), which is 0x20 = 32 before the first trainer
	while True:
		if(trdata[pointer_data] == 66 and trdata[pointer_data + 1] == 77 and trdata[pointer_data + 2] == 73 and trdata[pointer_data + 3] == 70):
			pointer_data += 32
			print(pointer_data)
			break
		#otherwise move forward by one
		else:
			pointer_data += 1
	
	#current integer byte-offset for TRdata
	max_trainer_index = 783
	
	
	
	#parse trdata
	while True:
	
		skip_number = 8
		
		if(trdata[pointer_data + 2] == 0 and trdata[pointer_data + 1] in doubles):
			print("Setting Leader to Double/Triple")
			trdata[pointer_data + 2] = trdata[pointer_data + 1]%2 + 1
			trdata[pointer_data + 12] = 135
		
		#get the "has items/has moves" booleans
		extra_space_bool = trdata[pointer_data]
		
		#if moves
		if(extra_space_bool & 1 == 1):
			skip_number += 8
		#if items
		if(extra_space_bool & 2 == 2):
			skip_number += 2
		
		#get # of Pokemon, which is the 3rd hex pair on
		number_pokemon = trdata[pointer_data + 3]
		
		
		while True:
			if(number_pokemon == 0):
				break
			#increment total offset from start of first Pokemon
			pokemon_relative_offset += skip_number
			#write offset of next Pokemon
			pokemon_offset_array.append(pokemon_relative_offset)
			number_pokemon -= 1
		
		if(trainer_number == max_trainer_index):
			break
		else:
			trainer_number += 1
			pointer_data += 20
	
	if(scale_bool):
		total_pokemon = len(pokemon_offset_array) - 1
		pokemon_count = 0
		
		adjustment = 0
		strikes = 0
		while True:
			#point to next level
			pointer_poke = 15872 + pokemon_offset_array[pokemon_count] + adjustment + 2
			level = trpoke[pointer_poke]
			
			if(level <= 0 or level >= 100):
				print("Read nonsense level of", level, "at", pointer_poke)
				if(strikes == 0):
					adjustment +=2
					strikes += 1
					print("Trying level of", level, "at", pointer_poke + adjustment)
				elif(strikes == 1):
					adjustment -= 2 + 2
					print("Trying level of", level, "at", pointer_poke + adjustment)
					strikes += 1
				else:
					pokemon_count += 1
					print("Failed to find level, for certain")
					strikes = 0
			else:
				strikes = 0
				new_level = min(round(level*1.18), 100)
				trpoke[pointer_poke] = new_level
				print(level, "mapped to", new_level)
				pokemon_count += 1
			if(pokemon_count >= total_pokemon):
				break


	return(trpoke, trdata)

def get_files_gen_vi(gen_number):

	#for B2W2, trdata is a091, trpoke is a092
	
	#get hex file locations:
	if(gen_number == 6.0):
		trdata_location = askopenfilename(filetypes = (("Select a/0/3/8", "*.*"), ("All Files", "*.*")))
		trpoke_location = askopenfilename(filetypes = (("Select a/0/4/0", "*.*"), ("All Files", "*.*")))
	

		trdata = bytearray()
		trpoke = bytearray()

		#read from file
		with open(trdata_location, 'rb') as f:
			trdata_bin = f.read()
		with open(trpoke_location, 'rb') as f:
			trpoke_bin = f.read()

		#convert the binary data into bytearrays. each index is one hex-pair
		trdata = bytearray(trdata_bin)
		trpoke = bytearray(trpoke_bin)
		return(trdata, trpoke, trpoke_location)
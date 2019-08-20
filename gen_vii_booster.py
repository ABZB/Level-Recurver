from first_thing import *
import random

evolve_array_usum = []


evolve_level_barrier_array_usum = []

def calc_vii(trdata, trpoke, double_all_bool, scale_bool, evolve_bool):
	
	trainer_array = []
	pokemon_array = []
	
	
	pointer_data = 0
	pointer_poke = 0
	trainer_number = 1
	skip_number = 22
	doubled_count = 0
	
	#Search for 42 4D 49 46 (66 77 73 70), which always precedes a series of 00 prior to first trainer.
	while True:
		if(trdata[pointer_data] == 66 and trdata[pointer_data + 1] == 77 and trdata[pointer_data + 2] == 73 and trdata[pointer_data + 3] == 70):
			pointer_data += 32
			print(pointer_data)
			break
		#otherwise move forward by one
		else:
			pointer_data += 1
	
	
	#current integer byte-offset for TRdata
	#TRdata, start from 0x19B4 = 6580
	max_trainer_index = 652
	
	#will have bump at the trainer number location
	trainer_bump = []
	
	
	#parse trdata
	while True:
		#every pokemon is exactly 0x20 long
		
		#get # of Pokemon, which is the 3rd hex pair on
		number_pokemon = trdata[pointer_data + 3] & 7
		
		#Only modify to Double Battle if a regular single battle (third parameter checks if the double battle AI is set)
		if(double_all_bool and trdata[pointer_data + 2] == 0 and trdata[pointer_data + 12]&8 == 0 and number_pokemon > 2):
			
			#if they have 3 or 4 Pokemon, 50% chance of double battle
			#if 5 or 6 Pokemon, always double battle
			if((random.randint(1,2) == 1 and number_pokemon <= 4) or number_pokemon > 4):
				trdata[pointer_data + 2] = 1
				#set double battle AI
				trdata[pointer_data + 12] += 8
				doubled_count += 1
				
		#write as many skips as the trainer has Pokemon
		#pokemon_count = 0
		#while True:
		#	trainer_array.append([trainer_number, skip_number])
		#	pokemon_count += 1
		#	if(pokemon_count == number_pokemon):
		#		break
		
		#trainer_bump.append(0)
		
		
		if(trainer_number == max_trainer_index):
			break
		else:
			trainer_number += 1
			pointer_data += 20
	
	
	#if(scale_bool):
	if(False):

		if(pointer_poke == 0):		
			#offset initial for trpoke = 19AC = 6572
			pointer_poke = 6572 + 2 #first level at 0x19AE = 6574
			
		pokemon_count = 0
		total_pokemon = len(trainer_array)
		

		edit_array = []
		
		#max level
		#sum, number
		max_level_array = [50,1]
		
		#pull all the levels, check that they are good:
		while True:
			
			while True:
				level = trpoke[pointer_poke]
				if(level == 0 or level > 100):
					#For some reason, some trainer have an FF FF after their last Pokemon. This checks for that
					if(level == 255):
						#If so, need to advance pointer by 2 
						if(trpoke[pointer_poke + 1] == 255):
							pointer_poke += 4
							print("Pointer advanced by 2 due to FF FF at at trainer", trainer_array[pokemon_count][0], "address", pointer_poke)
						#If so, need to advance pointer by 1
						elif(trpoke[pointer_poke - 1] == 255):
							pointer_poke += 3
							print("Pointer advanced by 1 due to FF FF at at trainer", trainer_array[pokemon_count][0], "address", pointer_poke)
				
					else:
						level1 = trpoke[pointer_poke+2]
						level2 = trpoke[pointer_poke-2]
						print("trying", level1, level2)
						
						if((level1 == 0 or level1 > 100) and (level2 == 0 or level2 > 100)):
							print("cannot fix")
							print("problem at trainer", trainer_array[pokemon_count][0], "getting value", level, "at", pointer_poke)
						#two ahead is good but two behind is not
						elif((level1 > 0 and level1 <= 100) and (level2 == 0 or level2 > 100)):
							print("two ahead good", level1, "replacing", level, "at trainer", trainer_array[pokemon_count][0], "address", pointer_poke)
							level = level1
							pointer_poke += 2
						#two behind is good but two ahead is not
						elif((level1 == 0 or level1 > 100) and (level2 > 0 and level2 <= 100)):
							print("two behind good", level2, "replacing", level, "at trainer", trainer_array[pokemon_count][0], "address", pointer_poke)
							level = level2
							pointer_poke -= 2
						#both good
						else:
							print("Both make sense, check manually", level1, level2, "error value", level, "at trainer", trainer_array[pokemon_count][0], "address", pointer_poke)
							level = min(level1, level2)
				else:
					break
			
			#level at address pokemon_count
			edit_array.append([level, pointer_poke])
			
			#keep track of highest and second highest levels, and their counts
			if(level > max_level_array[0]/max_level_array[1]  and level < 95):
				max_level_array[0] += level
				max_level_array[1] += 1
				
			
			#if this is the last Pokemon, break
			if(pokemon_count + 1 >= total_pokemon):
				break
			else:
				#move to the next pokemon
				pointer_poke += trainer_array[pokemon_count][1]
				#increment the pokemon count
				pokemon_count += 1
		
		
		
		
		#calculate level curve
		
		#The level that will the first level mapped to 100
		level_to_100 = max_level_array[0]/max_level_array[1]
		
		#avoid divide by zero, in this case rescaling is minimal anyway
		if(level_to_100 == 100):
			level_to_100 = 99
		
		curve_exponent = 0.35
		
		curve_divisor = level_to_100**(1+curve_exponent)/(100 - level_to_100)
		
		print('Mapping', level_to_100, 'to 100.', 'Curve divisor is', curve_divisor)
		
		
		#modification of Pokemon
		pokemon_count = 0
		while True:
			
		#edit Pokemon Level
			level = edit_array[pokemon_count][0]
			
			#function adds to level L (L^(curve_exponent))/(curve_divisor)*100% of L
			level = level*(1 + (level**curve_exponent)/curve_divisor)
			
			level = min(round(level), 100)
			
			pointer_poke = edit_array[pokemon_count][1]
			
			trpoke[edit_array[pokemon_count][1]] = level
			
			
		#evolve if possible
			low_digits = trpoke[pointer_poke + 2]
			high_digits = trpoke[pointer_poke + 3]*256
			
			index_number = low_digits + high_digits
			
			new_number = index_number
				
			#get the level that Pokemon should be evolved above. recurse in case a non-evolved pokemon is high enough to evolve twice
			while True:
				#get the level this Pokemon should evolve by
				try:
					evolve_level = evolve_level_barrier_array_bw[new_number]
				except:
					print("Error at", trainer_array[pokemon_count][0] + 1)
					break
					
				#if it's high enough, grab the index number of the next stage
				if(level >= evolve_level):
					new_number = evolve_array_bw[new_number]
				else:
					break
				if(new_number == evolve_array_bw[new_number]):
					break
			
			#write new index number if different
			if(new_number != index_number):
				#get low digit
				low_digits = new_number % 256
				high_digits = int((new_number - low_digits)/256)
				
				trpoke[pointer_poke + 2] = low_digits
				trpoke[pointer_poke + 3] = high_digits			
			#if this is the last Pokemon, break
			if(pokemon_count + 1 >= total_pokemon):
				break
			else:
				#increment the pokemon count
				pokemon_count += 1
	
	print("Set", doubled_count, "trainers to challenge player to Double Battles. Please remember that the game will crash if you battle such a trainer without at least two Pokemon in your party (all will be fine even if all but one is fainted).")
	return(trpoke, trdata)

def get_files_gen_vii(gen_number):

	#for B2W2, trdata is a091, trpoke is a092
	
	#get hex file locations:
	if(gen_number == 7.1):
		trdata_location = askopenfilename(filetypes = (("Select a/1/0/6", "*.*"), ("All Files", "*.*")))
		trpoke_location = askopenfilename(filetypes = (("Select a/1/0/7", "*.*"), ("All Files", "*.*")))
	

		trpoke = bytearray()
		trdata = bytearray()

		#read from file
		with open(trpoke_location, 'rb') as f:
			trpoke_bin = f.read()
		with open(trdata_location, 'rb') as f:
			trdata_bin = f.read()

		#convert the binary data into bytearrays. each index is one hex-pair
		trpoke = bytearray(trpoke_bin)
		trdata = bytearray(trdata_bin)
		return(trdata, trpoke, trpoke_location)
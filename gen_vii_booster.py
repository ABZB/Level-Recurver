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
		number_pokemon = trdata[pointer_data + 3]
		
		#Only modify to Double Battle if a regular single battle (third parameter checks if the double battle AI is set)
		if(double_all_bool and trdata[pointer_data + 2] == 0 and trdata[pointer_data + 12]&8 == 0 and number_pokemon >= 4):
			
			#if they have 3 or 4 Pokemon, 50% chance of double battle
			#if 5 or 6 Pokemon, always double battle
			if(True):#(random.randint(1,2) == 1 and number_pokemon <= 4) or number_pokemon > 4):
				trdata[pointer_data + 2] = 1
				#set double battle AI
				trdata[pointer_data + 12] += 8
				doubled_count += 1
				
		
		if(trainer_number == max_trainer_index):
			break
		else:
			trainer_number += 1
			pointer_data += 20
	
	
	
	
	print("Set", doubled_count, "trainers to challenge player to Double Battles. Please remember that the game will crash if you battle such a trainer without at least two Pokemon in your party (all will be fine even if all but one is fainted).")
	return(trpoke, trdata)

def get_files_gen_vii(gen_number):

	#for B2W2, trdata is a091, trpoke is a092
	
	#get hex file locations:
	if(gen_number == 7.1):
		trdata_location = askopenfilename(filetypes = (("Select a/1/0/6", "*.*"), ("All Files", "*.*")))
		trpoke_location = askopenfilename(filetypes = (("Select a/1/0/7", "*.*"), ("All Files", "*.*")))
	

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
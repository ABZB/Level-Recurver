import io
import string
import math
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import binascii
import os
import time

trainer_scale_array_hgss = [13,4,4,5,18,14,16,4,23,12,100,11,11,46,74,23,48,8,100,8,13,18,9,17,9,8,8,70,7,19,21,46,27,26,52,70,22,67,21,100,100,100,6,21,21,20,4,72,8,7,6,6,6,6,6,8,8,77,65,8,10,14,100,14,14,14,12,12,12,18,18,16,22,16,16,16,16,16,100,16,19,21,68,68,23,23,100,100,20,24,24,24,24,24,24,24,24,24,24,10,11,70,60,60,100,100,100,48,44,51,51,51,70,60,60,44,51,100,51,100,48,31,29,47,47,44,44,100,29,31,31,31,100,29,67,68,47,100,75,72,100,14,48,48,48,48,49,70,69,69,49,76,76,49,10,25,25,100,25,100,100,100,100,100,100,100,100,100,100,100,100,31,31,100,100,100,100,17,67,100,17,17,68,17,45,45,45,45,45,45,45,45,45,100,45,45,45,45,45,45,100,100,100,100,100,100,100,100,100,100,22,22,22,22,22,46,22,46,46,46,100,46,46,46,100,100,46,46,100,62,100,60,46,69,75,100,100,75,75,100,100,75,100,58,58,58,58,72,4,48,25,79,73,70,60,64,68,62,80,82,81,100,21,101,4,13,21,101,13,21,59,101,100,14,14,8,8,48,4,4,100,20,46,100,101,101,101,59,59,6,79,100,78,78,100,77,70,70,76,66,67,67,100,100,100,100,100,73,63,63,63,67,66,66,66,65,65,74,9,65,65,65,29,29,47,64,76,67,70,70,67,69,69,14,49,64,60,100,100,100,100,100,100,100,100,64,100,65,65,66,66,100,46,100,100,64,69,65,65,16,70,76,100,63,63,70,100,62,62,79,79,100,78,77,100,100,70,74,74,65,65,67,8,9,100,19,12,16,21,9,46,46,46,100,17,60,21,21,75,21,22,31,31,46,47,47,47,47,14,21,70,60,70,100,62,64,100,58,70,65,65,100,100,75,75,75,100,100,100,17,17,17,17,21,21,17,17,21,21,22,22,100,100,60,60,100,47,47,16,47,48,48,49,16,16,70,70,70,70,5,5,8,8,21,21,31,31,45,45,45,46,46,100,100,100,100,100,46,47,45,45,45,45,45,47,12,47,46,101,101,101,65,20,20,3,3,3,25,45,52,52,52,17,100,17,100,21,100,22,4,100,5,16,100,8,100,29,8,100,14,100,31,10,100,14,100,16,21,100,31,100,100,100,100,100,100,100,100,100,100,100,100,100,100,76,76,74,74,74,74,74,74,63,63,65,65,65,65,65,65,65,65,65,66,66,66,66,66,67,67,67,66,66,66,66,66,66,66,66,78,78,78,78,78,78,100,78,78,77,77,77,77,77,77,77,77,77,61,61,61,11,100,49,70,48,48,60,47,70,21,17,47,17,17,17,14,14,14,16,16,16,72,72,72,72,72,72,66,66,66,66,66,66,66,66,66,67,67,67,67,67,67,67,67,67,66,66,66,66,66,66,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,100,100,100,100,100,22,22,22,45,70,70,70,19,19,81,81,81,81,73,79,79,79,80,80,80,80,80,80,75,100,75,75,75,100,100,58,100,100,100,46,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,26,27,27,27,27,100,100,100,100,100]

trainer_min_level_array_hgss = [21,5,5,7,27,21,22,6,39,21,100,17,17,52,96,39,56,17,100,16,21,27,17,24,17,17,17,69,16,27,34,50,40,39,61,69,38,92,38,100,100,100,8,38,38,34,6,95,17,16,8,8,8,8,8,17,17,98,91,17,17,21,100,21,21,21,21,21,21,27,27,22,38,22,22,22,22,22,100,22,31,38,93,93,39,39,100,100,34,39,39,39,39,39,39,39,39,39,39,17,17,69,65,65,100,100,100,56,47,61,61,61,69,65,65,47,61,100,61,100,56,42,41,56,56,47,47,100,41,42,42,42,100,41,92,93,56,100,81,95,100,21,56,56,56,56,56,69,93,93,56,98,98,56,17,39,39,100,39,100,100,100,100,100,100,100,100,100,100,100,100,42,42,100,100,100,100,24,92,100,24,24,93,24,50,50,50,50,50,50,50,50,50,100,50,50,50,50,50,50,100,100,100,100,100,100,100,100,100,100,38,38,38,38,38,52,38,52,52,52,100,52,52,52,100,100,52,52,100,89,100,65,52,93,81,100,100,81,81,100,100,81,100,86,86,86,86,95,6,56,39,99,96,69,65,90,93,89,100,100,100,100,34,100,5,21,34,100,21,34,86,100,100,21,21,17,17,56,6,6,100,34,52,100,100,100,100,86,86,8,99,100,99,99,100,98,69,69,98,91,92,92,100,100,100,100,100,96,89,89,89,92,91,91,91,91,91,96,17,91,91,91,41,41,56,90,98,92,69,69,92,93,93,21,56,90,65,100,100,100,100,100,100,100,100,90,100,91,91,91,91,100,52,100,100,90,93,91,91,22,69,98,100,89,89,69,100,89,89,99,99,100,99,98,100,100,69,96,96,91,91,92,17,17,100,31,21,22,38,17,52,52,52,100,24,65,38,38,81,38,38,42,42,52,56,56,56,56,21,38,69,65,69,100,89,90,100,86,69,91,91,100,100,81,81,81,100,100,100,24,24,24,24,38,38,24,24,38,38,38,38,100,100,65,65,100,56,56,22,56,56,56,56,22,22,69,69,69,69,7,7,17,17,38,38,42,42,50,50,50,52,52,100,100,100,100,100,50,52,50,50,50,50,50,52,17,52,50,100,100,100,91,34,34,5,5,5,39,50,61,61,61,24,100,24,100,38,100,38,6,100,7,22,100,17,100,41,17,100,21,100,42,17,100,21,100,22,38,100,42,100,100,100,100,100,100,100,100,100,100,100,100,100,100,98,98,96,96,96,96,96,96,89,89,91,91,91,91,91,91,91,91,91,91,91,91,91,91,92,92,92,91,91,91,91,91,91,91,91,99,99,99,99,99,99,100,99,99,98,98,98,98,98,98,98,98,98,88,88,88,17,100,56,69,56,56,65,56,69,38,24,56,24,24,24,21,21,21,22,22,22,95,95,95,95,95,95,91,91,91,91,91,91,91,91,91,92,92,92,92,92,92,92,92,92,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,100,100,100,100,100,38,38,38,50,69,69,69,31,31,100,100,100,100,96,99,99,99,100,100,100,100,100,100,81,100,81,81,81,100,100,86,100,100,100,50,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,40,40,40,40,40,100,100,100,100,100]

evolve_array_hgss = [0,2,3,3,5,6,6,8,9,9,11,12,12,14,15,15,17,18,18,20,20,22,22,24,24,25,26,28,28,30,31,31,33,34,34,36,36,38,38,40,40,42,169,45,182,45,47,47,49,49,51,51,53,53,55,55,57,57,59,59,62,186,62,64,65,65,67,68,68,70,71,71,73,73,75,76,76,78,78,80,80,82,462,83,85,85,87,87,89,89,91,91,93,94,94,208,97,97,99,99,101,101,103,103,105,105,106,107,463,110,110,112,464,242,465,115,117,230,119,119,121,121,122,123,124,466,467,127,128,130,130,131,132,133,134,135,136,233,139,139,141,141,142,143,144,145,146,148,149,149,150,151,153,154,154,156,157,157,159,160,160,162,162,164,164,166,166,168,168,169,171,171,25,35,39,176,468,178,178,180,181,181,182,184,184,185,186,188,189,189,424,192,192,469,195,195,196,197,430,199,429,201,202,203,205,205,206,472,208,210,210,211,212,213,214,461,217,217,219,219,221,473,222,224,224,225,226,227,229,229,230,232,232,474,234,235,237,237,124,125,126,241,242,243,244,245,247,248,248,249,250,251,253,254,254,256,257,257,259,260,260,262,262,264,264,266,267,267,269,269,271,272,272,274,275,275,277,277,279,279,281,282,282,284,284,286,286,288,289,289,291,291,292,294,295,295,297,297,183,476,301,301,302,303,305,306,306,308,308,310,310,311,312,313,314,407,317,317,319,319,321,321,323,323,324,326,326,327,329,330,330,332,332,334,334,335,336,337,338,340,340,342,342,344,344,346,346,348,348,350,350,351,352,354,354,356,477,357,358,359,202,362,362,364,365,365,367,367,368,369,370,372,373,373,375,376,376,377,378,379,380,381,382,383,384,385,386,388,389,389,391,392,392,394,395,395,397,398,398,400,400,402,402,404,405,405,315,407,409,409,411,411,413,413,414,416,416,417,419,419,421,421,423,423,424,426,426,428,428,429,430,432,432,358,435,435,437,437,185,122,113,441,442,444,445,445,143,448,448,450,450,452,452,454,454,455,457,457,226,460,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507]

evolve_level_barrier_array_hgss = [0,16,32,0,16,36,0,16,36,0,7,10,0,7,10,0,18,36,0,20,0,20,0,22,0,0,0,22,0,16,21,0,16,21,0,5,0,5,0,5,0,22,27,21,26,0,24,0,31,0,26,0,28,0,33,0,28,0,5,0,25,30,0,16,21,0,28,33,0,21,26,0,30,0,25,30,0,40,0,37,0,30,35,0,31,0,34,0,38,0,5,0,25,30,0,5,26,0,28,0,30,0,5,0,28,0,0,0,5,35,0,42,47,52,57,0,32,37,33,0,5,0,0,0,0,5,10,0,0,20,0,0,0,0,0,0,0,30,40,0,40,0,0,0,0,0,0,30,55,0,0,0,16,32,0,14,36,0,18,30,0,15,0,20,0,18,0,22,0,0,27,0,10,10,10,10,30,25,0,15,30,0,0,18,0,0,0,18,27,0,40,5,0,5,40,0,0,0,40,0,40,0,0,0,31,0,0,40,0,23,0,0,0,0,0,30,30,0,38,0,33,38,0,25,0,0,0,0,24,0,0,25,0,40,0,0,20,0,30,30,30,0,0,0,0,0,30,55,0,0,0,0,16,36,0,16,36,0,16,36,0,18,0,20,0,7,10,0,10,0,14,19,0,14,19,0,22,0,25,0,20,30,0,22,0,23,0,18,36,0,20,0,0,20,40,0,24,0,15,30,20,0,0,0,32,42,0,37,0,26,0,0,0,0,0,36,26,0,30,0,40,0,33,0,0,32,0,0,35,45,0,32,0,35,0,0,0,0,0,30,0,30,0,36,0,40,0,40,0,5,0,0,0,37,0,37,42,0,0,0,15,42,0,32,44,0,5,0,0,0,0,30,50,0,20,45,0,0,0,0,0,0,0,0,0,0,0,18,32,0,14,36,0,16,36,0,14,34,0,15,0,10,0,15,30,0,10,0,30,0,30,0,20,0,0,21,0,0,26,0,25,0,30,0,0,28,0,5,0,0,0,38,0,10,34,0,33,0,10,10,10,0,0,24,48,0,30,35,0,34,0,40,0,37,0,0,31,0,30,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



def evolve_poke(index_number):
	return(evolve_array_hgss[index_number])
	
def calc(trdata, trpoke):
	
	trainer_array = []
	pokemon_array = []
	
	#current integer byte-offset for TRdata
	#TRdata, start from 0x1758 = 5976
	pointer_data = 5976
	trainer_number = 0
	#will have bump at the trainer number location
	trainer_bump = []
	
	
	#parse trdata
	while True:
		skip_number = 8
	
		#get the "has items/has moves" booleans
		extra_space_bool = trdata[pointer_data]
		
		#if moves
		if(extra_space_bool & 1 == 1):
			skip_number += 8
		#if items
		if(extra_space_bool & 2 == 2):
			skip_number += 2
		
		#get # of Pokemon, which is the 3rd hex pair on
		number_pokemon = trdata[pointer_data + 3] & 7
	
		
		#write as many skips as the trainer has Pokemon
		pokemon_count = 0
		while True:
			#fix for Bugsy (third Pokemon has an extra byte for some reason)
			#if((trainer_number == 20 and pokemon_count == 2) or (trainer_number == 31 and pokemon_count == 2) or (trainer_number == 32 and pokemon_count == 2) or (trainer_number == 159 and pokemon_count == 0) or (trainer_number == 160 and pokemon_count == 0)):
				#skip_number += 2
				#print("fix")
			trainer_array.append([trainer_number, skip_number])
			pokemon_count += 1
			if(pokemon_count == number_pokemon):
				break
		
		trainer_bump.append(0)
		
		trainer_number += 1
		pointer_data += 20
		
		if(trainer_number == 737):
			break
			
	
	#offset initial for trpoke = 174E = 5966
	pointer_poke = 5966
	pokemon_count = 0
	total_pokemon = len(trainer_array)
	
	edit_array = []
	
	#pull all the levels:
	while True:
		
		level = trpoke[pointer_poke]
		
		if(level == 0 or level > 100):
			level1 = trpoke[pointer_poke+2]
			level2 = trpoke[pointer_poke-2]
			print("trying", level1, level2)
			
			if((level1 == 0 or level1 > 100) and (level2 == 0 or level2 > 100)):
				print("cannot fix")
				print("problem at trainer", 1+trainer_array[pokemon_count][0], "getting value", level, "at", pointer_poke)
			#two ahead is good but two behind is not
			elif((level1 > 0 and level1 <= 100) and (level2 == 0 or level2 > 100)):
				print("two ahead good", level1, "replacing", level, "at trainer", 1+trainer_array[pokemon_count][0], "address", pointer_poke)
				level = level1
				pointer_poke += 2
			#two behind is good but two ahead is not
			elif((level1 == 0 or level1 > 100) and (level2 > 0 and level2 <= 100)):
				print("two behind good", level1, "replacing", level, "at trainer", 1+trainer_array[pokemon_count][0], "address", pointer_poke)
				level = level2
				pointer_poke -= 2
			#both good
			else:
				print("Both make sense, check manually", level1, level2, "error value", level, "at trainer", 1+trainer_array[pokemon_count][0], "address", pointer_poke)
				level = min(level1, level2)
		
		#level at address pokemon_count
		edit_array.append([level, pointer_poke])
		
		
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#move to the next pokemon
			pointer_poke += trainer_array[pokemon_count][1]
			#increment the pokemon count
			pokemon_count += 1
	
	
	
	#initial scaling of all Pokemon
	pokemon_count = 0
	while True:
	
		level = edit_array[pokemon_count][0]
		
		#scales level, taking into account the order in which that trainer is encountered in-game. 
		try:
		
			mult = trainer_scale_array_hgss[trainer_array[pokemon_count][0]]
			mult /= 100
			mult += 1
			new_level = round(mult*level)
			
			if(new_level == level):
				new_level += 1
			
			#ensures that the level is at least the minimum level
			while True:
				if(new_level + trainer_bump[trainer_array[pokemon_count][0]] < trainer_min_level_array_hgss[trainer_array[pokemon_count][0]]):
					trainer_bump[trainer_array[pokemon_count][0]] += 1
				else:
					break
			#print("Trainer number", trainer_array[pokemon_count][0], "Bumped by", trainer_bump[trainer_array[pokemon_count][0]])
				
			level = min(new_level, 100)
			
		except:
			print("exception")
			level = 100
		
		edit_array[pokemon_count][0] = level
		
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#increment the pokemon count
			pokemon_count += 1
		
		
		
	#add to each trainer to satisfy min level, evolve if needed, then write back to array
	pokemon_count = 0
	while True:
	
		pointer_poke = edit_array[pokemon_count][1]
		level = min(edit_array[pokemon_count][0] + trainer_bump[trainer_array[pokemon_count][0]], 100)
		
		print(trainer_array[pokemon_count][0], trainer_bump[trainer_array[pokemon_count][0]], level)
		
		#evolve the Pokemon if it is above the level it evolves at (or set value for other kinds of evolutions)
		
		#get index number
		low_digits = trpoke[pointer_poke + 2]
		high_digits = trpoke[pointer_poke + 3]*256
		
		index_number = low_digits + high_digits
		
		new_number = index_number
		
		#get the level that Pokemon should be evolved above. recurse in case a non-evolved pokemon is high enough to evolve twice
		while True:
			#get the level this Pokemon should evolve by
			try:
				evolve_level = evolve_level_barrier_array_hgss[new_number]
			except:
				print("Error at", trainer_array[pokemon_count][0] + 1)
				break
				
			#if it's high enough, grab the index number of the next stage
			if(level >= evolve_level):
				new_number = evolve_array_hgss[new_number]
			else:
				break
			if(new_number == evolve_array_hgss[new_number]):
				break
		
		#write new index number if different
		if(new_number != index_number):
			# as max in gen IV is 507, this is either 0x00 or 0x01. Only need to write either 0 or 1 
			if(new_number > 256):
				trpoke[pointer_poke + 3] = 1
				new_number -= 256
			else:
				#write 0 to the high digit
				trpoke[pointer_poke + 3] = 0
			#low digit
			trpoke[pointer_poke + 2] = new_number
					

		#write level back to the byte
		trpoke[pointer_poke] = level
		#if this is the last Pokemon, break
		if(pokemon_count + 1 >= total_pokemon):
			break
		else:
			#increment the pokemon count
			pokemon_count += 1
	return(trpoke)

#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = "", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)

		
#write backup of the file to be modified to local directory
def save_backup(data, name):
	try:
		current_directory = os.getcsd()
		file_name = os.path.join(current_directory, 'backup', name, '.',time.strftime("%y/%m/%d %H:%M"),'.bak')
		with open(file_name, 'wb') as f:
			f.write(output_binary)
	except:
		print("Could not save backup")

		
def get_files():

	#for HGSS, trdata is a055, trpoke is a056
	
	#get hex file locations:
	root = Tk()
	root.update()
	trdata_location = askopenfilename(filetypes = (("Select a/0/5/5", "*.*"), ("All Files", "*.*")))
	trpoke_location = askopenfilename(filetypes = (("Select a/0/5/6", "*.*"), ("All Files", "*.*")))
	root.destroy()
	
	
	trdata = bytearray()
	trpoke = bytearray()
	
	#get the data
	with open(trdata_location, 'rb') as f:
		trdata_bin = f.read()
	
	with open(trpoke_location, 'rb') as f:
		trpoke_bin = f.read()
	
	save_backup(trpoke_bin, 6)

	
	#convert the binary data into bytearrays. each index is one hex-pair
	trdata = bytearray(trdata_bin)
	trpoke = bytearray(trpoke_bin)
	
	return(trdata, trpoke, trpoke_location)
	
def main():
	#get the data files and the output path
	trdata, trpoke, output_path = get_files()
	
	trpoke = calc(trdata, trpoke)
	
	#seperates the file name (always a single character from HGSS on) from path
	file_name = output_path[-1]
	output_path = output_path[:-1]
	
	save_binary_file(trpoke, file_name, output_path)
		
		
main()

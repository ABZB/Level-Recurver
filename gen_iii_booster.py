from first_thing import *
evolve_array_iii = [0,2,3,3,5,6,6,8,9,9,11,12,12,14,15,15,17,18,18,20,20,22,22,24,24,26,26,28,28,30,31,31,33,34,34,36,36,38,38,40,40,42,169,44,45,45,47,47,49,49,51,51,53,53,55,55,57,57,59,59,61,62,62,64,65,65,67,68,68,70,71,71,73,73,75,76,76,78,78,80,80,82,82,83,85,85,87,87,89,89,91,91,93,94,94,208,97,97,99,99,101,101,103,103,105,105,106,107,108,110,110,112,112,242,114,115,117,230,119,119,121,121,122,123,124,125,162,127,128,130,130,131,132,134,134,135,136,137,139,139,141,141,142,143,144,145,146,148,149,149,150,151,153,154,154,156,157,157,159,160,160,162,162,164,164,166,166,168,168,169,171,171,25,35,39,175,176,178,178,180,181,181,182,184,184,185,186,188,189,189,190,192,192,193,195,195,196,197,198,199,200,201,202,203,205,205,206,207,208,210,210,211,212,213,214,215,217,217,219,219,220,221,222,224,224,225,226,227,229,229,230,232,232,233,234,235,237,237,124,125,126,241,242,243,244,245,247,248,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,278,279,279,281,282,282,284,285,285,287,287,289,289,291,292,292,294,294,296,297,297,299,300,300,302,302,303,305,305,307,307,308,310,310,312,312,314,314,316,316,317,319,319,313,321,322,324,324,325,327,327,329,329,331,331,333,334,334,336,336,338,338,340,340,342,343,343,345,345,347,347,348,349,12,352,352,353,354,355,357,357,359,359,202,346,347,341,365,366,366,368,368,369,371,372,372,374,374,375,376,378,378,379,380,381,383,384,384,385,386,387,389,389,391,391,393,394,394,396,397,397,399,400,400]

evolve_level_barrier_array_iii = [0,16,32,0,16,36,0,16,36,0,7,10,0,7,10,0,18,36,0,20,0,20,0,22,0,100,0,22,0,16,21,0,16,21,0,5,0,50,0,5,0,22,27,21,26,0,24,0,31,0,26,0,28,0,33,0,28,0,5,0,25,30,0,16,21,0,28,33,0,21,26,0,30,0,25,30,0,40,0,37,0,30,35,0,31,0,34,0,38,0,5,0,25,30,0,5,26,0,28,0,30,0,5,0,28,0,0,0,5,35,0,42,47,52,57,0,32,37,33,0,5,0,0,0,0,5,10,0,0,20,0,0,0,0,0,0,0,30,40,0,40,0,0,0,0,0,0,30,55,0,0,0,16,32,0,14,36,0,18,30,0,15,0,20,0,18,0,22,0,0,27,0,10,10,10,10,30,25,0,15,30,0,0,18,0,0,0,18,27,0,40,5,0,5,40,0,0,0,40,0,40,0,0,0,31,0,0,40,0,23,0,0,0,0,0,30,30,0,38,0,33,38,0,25,0,0,0,0,24,0,0,25,0,40,0,0,20,0,30,30,30,0,0,0,0,0,30,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,36,0,16,36,0,16,36,0,18,0,20,0,7,10,0,10,0,14,19,0,14,19,0,20,0,0,22,0,23,0,0,25,0,22,0,40,0,20,0,0,36,0,30,0,0,30,0,0,30,0,5,0,30,0,35,45,0,24,0,26,0,33,0,32,44,0,32,0,42,0,0,0,15,32,0,0,0,0,37,0,35,0,15,37,42,36,18,36,0,26,0,0,20,40,0,5,0,0,0,37,0,0,0,0,32,42,0,0,0,0,40,0,40,0,20,30,0,30,50,0,20,45,0]


doubles_set = {261,262,263,264,265,266,267,268,269,270,271,272,335,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801}


def calc_iii(em):
	
	#current integer byte-offset for TRdata
	#TRdata, start from 0x310058 = 3211352
	trainer_pointer = 3211352
	#0x30B62C
	pokemon_pointer =  3192364
	trainer_number = 1
	
	#iterate over trainers
	while True:
		#get the number of Pokemon the trainer has
		number_pokemon = em[trainer_pointer + 32]
		
		#Do the Pokemon have hold items? Custom moves?
		extra_type = em[trainer_pointer]
		
		#none or only hold items
		if(extra_type == 0 or extra_type == 1):
			pokemon_length = 8
		#custom moves but no items
		elif(extra_type == 2):
			pokemon_length = 14
		#hold items and custom moves
			pokemon_length = 16
		
		#If a trainer has 4 or more pokemon, or is a Gym Leader or E4 member, make it a double battle
		
		if(number_pokemon >= 4 or trainer_number in doubles_set):
			em[trainer_pointer + 24] = 1
		
		
		#iterate over that trainer's Pokemon
		while True:
			#get level
			level = em[pokemon_pointer + 2]
			#use level * (1 + level/50) = (level + (level^2/50)) = (50 * level + level ^2)/50. Level 10 has (500 + 100)/50 = 600/50 = 60/5 = 12, level 20 has 20*1.4 = 28, level 30 has 30*1.6 = 48, level 40 has 40*1.8 = 72, 50*2 = 100
			level = min(round(level * (1 + level/50)),100)
			#write new level
			em[pokemon_pointer + 2] = level
			
			
			#If the Pokemon should be evolved, evolve it. Will evolve any unevolved Pokemon that is 5 or more levels above the minimum level
			low_digits = em[pokemon_pointer + 4]
			high_digits = em[pokemon_pointer + 5]
			
			index = low_digits + 256*high_digits
			
			#last Pokemon that can evolve by internal index number in gen III is Metang, at 399
			if(index < 400):
				#If the Pokemon is past the level it evolves at by level-up
				if(level >= evolve_level_barrier_array_iii[index]):
					new_index = evolve_array_iii[index]
					if(new_index != index):
						
						#convert back to hex pairs
						low_digits = new_index%256
						high_digits = int((new_index - low_digits)/256)
						
						#write
						em[pokemon_pointer + 4] = low_digits
						em[pokemon_pointer + 5] = high_digits
			
			
		
			#move pointer to next Pokemon
			pokemon_pointer += pokemon_length
			
			#decrement party count of current trainer
			number_pokemon -= 1
			
			#checks if finished with current trainer, if so, break. If not, everything is set up for next iteration
			if(number_pokemon == 0):
				break
			
		
		trainer_pointer += 40 #0x28
		trainer_number += 1
		#actual last trainer index is 854, but the last four seem to be dummies, so will not change them
		if(trainer_number == 850):
			break
	return(em)
	
def get_files_gen_iii():

	#for Emerald, modify .gba directly
	
	#get hex file locations:
	root = Tk()
	root.update()
	rom_location = askopenfilename(filetypes = (("Select Emerald GBA file", "*.*"), (".GBA", "*.gba")))
	root.destroy()
	
	
	rom = bytearray()
	
	#get the data
	with open(rom_location, 'rb') as f:
		rom_bin = f.read()
	
	
	#convert the binary data into bytearrays. each index is one hex-pair
	rom = bytearray(rom_bin)
	
	return(rom, rom_location)
from gen_iii_booster import *
from gen_iv_booster import *
from gen_v_booster import *

#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = "", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)


#warns user if no options were chosen
def nothing_selected():
	#Msgbox = tk.messagebox.askquestion('Nothing Selected', 'No options were selected, returning to Main Menu', icon = 'warning')
	print("Nothing Selected")

def main(gen_number, double_bool, double_all_bool, mix_it_up_bool, scale_bool):
	
	#return to main menu if no options were selected
	if(not(double_bool or scale_bool)):
		nothing_selected()
		return(False)
	
	try:
		gen_number = int(gen_number)
	except:
		try:
			gen_number = float(gen_number)
		except:
			print("Problem with Gen number:", gen_number, type(gen_number))
	
	#errors
	if(double_all_bool and gen_number == 4.1 or gen_number == 4.2):
		print("Does not work in Gen IV (Causes freezing)")
		return(False)
		
	if(double_all_bool and mix_it_up_bool):
		print("These two conflict")
		return(False)
	
	if(mix_it_up_bool and gen_number < 5):
		print("Options selected do not work for this generation")
		return(False)
	
	if(double_bool and gen_number == 4.2):
		print("Double Battle Inducer not currently implented for HGSS")
		return(False)
	
	#Gen III
	if(gen_number == 3.2):
		em, output_path = get_files_gen_iii()
		
		em = calc_iii(em, double_bool, double_all_bool, scale_bool)
		file_name = "Emerald Scaled.gba"
		
		save_binary_file(em, file_name, output_path)

	#Gen IV
	elif(gen_number == 4.1 or gen_number == 4.2):
		
		
	
		#get the data files and the output path
		trdata, trpoke, output_path = get_files_gen_iv(gen_number)
	
		trpoke, trdata = calc_iv(trdata, trpoke, double_bool, scale_bool)
		
		if(gen_number == 4.2):
			save_binary_file(trdata, '/a/0/5/5', output_path)
			
			save_binary_file(trpoke, '/a/0/5/6', output_path)
		elif(gen_number == 4.1):
			save_binary_file(trdata, 'root/poketool/trainer/trdata', output_path)
			
			save_binary_file(trpoke, 'root/poketool/trainer/trpoke', output_path)
			
	
	elif(gen_number == 5.1):
	
		trdata, trpoke, output_path = get_files_gen_v(gen_number)
		trpoke, trdata = calc_v(trdata, trpoke, double_bool, double_all_bool, mix_it_up_bool, scale_bool)
	
		if(double_bool or double_all_bool or mix_it_up_bool):
			save_binary_file(trdata, '1.narc', output_path)
		if(scale_bool):
			save_binary_file(trpoke, '2.narc', output_path)
		
	#merge below into Gen IV and Platinum
	else:
		return(False)
		#get the data files and the output path
		trdata, output_path = get_files_gen_iv(gen_number)
		
		print('working 1')
	
		#trpoke = calc_iv(trdata, trpoke)
		
		print(len(trdata))
		trdata = doublify(trdata)
	
		#seperates the file name (always a single character from HGSS on) from path
	
		save_binary_file(trdata, 'trdata.narc', output_path)
		

def main_menu():
	global master
	master = Tk()
	row_iter = 0
	#frame_main_menu = Frame(master)
	#frame_main_menu.pack()
	master.title('Select Game to modify & modifications to apply')
	
	#Mods to apply
	
	#booleans variables for checkboxes
	double_bool = BooleanVar()
	double_all_bool = BooleanVar()
	mix_it_up_bool = BooleanVar()
	scale_bool = BooleanVar()
	
	#checkboxes and accompanying text
	Label(master, text = 'Options', font = (16)).grid(row = row_iter)
	
	row_iter += 1
	
	Checkbutton(master, text = 'Make Gym Leaders, E4 members, etc. Double Battles', variable = double_bool, onvalue = True, offvalue = False).grid(row = row_iter, sticky = W)
	
	row_iter += 1
	
	Checkbutton(master, text = 'Make as many battles as possible double battles (Gen III and V only)', variable = double_all_bool, onvalue = True, offvalue = False).grid(row = row_iter, sticky = W)
	
	row_iter += 1
	
	Checkbutton(master, text = 'Make as many battles as possible Double, Triple, or Rotation battles. (Gen V only)', variable = mix_it_up_bool, onvalue = True, offvalue = False).grid(row = row_iter, sticky = W)
	
	row_iter += 1
	
	Checkbutton(master, text = 'Rescale Level Curve', variable = scale_bool, onvalue = True, offvalue = False).grid(row = row_iter, sticky = W)
	
	row_iter += 1
	
	#game selection
	Label(master, text = 'Select Game', font = (16)).grid(row = row_iter, pady = 4)
	
	row_iter += 1
	
	Button(master, text = 'Emerald', command = lambda: main('3.2', double_bool.get(), double_all_bool.get(), mix_it_up_bool.get(), scale_bool.get()), height = 2, width = 50, pady = 1).grid(row = row_iter)
	
	row_iter += 1
	
	Button(master, text = 'Heart Gold/Soul Silver (Currently only scaling is available)', command = lambda: main('4.1', double_bool.get(), double_all_bool.get(), mix_it_up_bool.get(), scale_bool.get()), height = 2, width = 50, pady = 1).grid(row = row_iter)
	
	row_iter += 1
	
	Button(master, text = 'Platinum', command = lambda: main('4.2', double_bool.get(), double_all_bool.get(), mix_it_up_bool.get(), scale_bool.get()), height = 2, width = 50, pady = 1).grid(row = row_iter)
	
	row_iter += 1
	
	Button(master, text = 'Black2/White2', command = lambda: main('5.1', double_bool.get(), double_all_bool.get(), mix_it_up_bool.get(), scale_bool.get()), height = 2, width = 50, pady = 1).grid(row = row_iter)
	
	row_iter += 1
	
	Button(master, text="Exit", command = master.destroy, height = 2, width = 25, pady = 1).grid(row = row_iter)
	
	master.mainloop()
	
		
main_menu()

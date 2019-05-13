from gen_iii_booster import *
from gen_iv_booster import *

#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = "", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)


#warns user if no options were chosen
def nothing_selected():
	Msgbox = tk.messagebox.askquestion('Nothing Selected', 'No options were selected, returning to Main Menu', icon = 'warning')
		

def main(gen_number, double_bool, scale_bool):
	
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
	
	#Gen III
	if(gen_number == 3.2):
		em, output_path = get_files_gen_iii()
		
		em = calc_iii(em, double_bool, scale_bool)
		file_name = "Emerald Scaled.gba"
		
		save_binary_file(em, file_name, output_path)

	#Gen IV
	elif(gen_number == 4.1 or gen_number == 4.2):
		
		
	
		#get the data files and the output path
		trdata, trpoke, output_path = get_files_gen_iv(gen_number)
	
		trpoke = calc_iv(trdata, trpoke)
	
		#seperates the file name (always a single character from HGSS on) from path
		file_name = output_path[-1]
		output_path = output_path[:-1]
	
		save_binary_file(trpoke, file_name, output_path)
		
	elif():
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

	#frame_main_menu = Frame(master)
	#frame_main_menu.pack()
	master.title('Select Game to modify & modifications to apply')
	
	#Mods to apply
	
	#booleans variables for checkboxes
	double_bool = BooleanVar()
	scale_bool = BooleanVar()
	
	#checkboxes and accompanying text
	Label(master, text = 'Options', font = (16)).grid(row = 0)
	Checkbutton(master, text = 'Make Gym Leaders, E4 members, etc. Double Battles?', variable = double_bool, onvalue = True, offvalue = False).grid(row = 1, sticky = W)
	
	Checkbutton(master, text = 'Rescale Level Curve', variable = scale_bool, onvalue = True, offvalue = False).grid(row = 2, sticky = W)
	
	#game selection
	Label(master, text = 'Select Game', font = (16)).grid(row = 3, pady = 4)
	Button(master, text = 'Emerald', command = lambda: main('3.2', double_bool, scale_bool), height = 2, width = 50, pady = 1).grid(row = 4)
	
	Button(master, text = 'Heart Gold/Soul Silver', command = lambda: main('4.1', double_bool, scale_bool), height = 2, width = 50, pady = 1).grid(row = 5)
	
	Button(master, text = 'Platinum', command = lambda: main('4.2', double_bool, scale_bool), height = 2, width = 50, pady = 1).grid(row = 6)
	
	Button(master, text="Exit", command = master.destroy, height = 2, width = 25, pady = 1).grid(row = 7)
	
	master.mainloop()
	
		
main_menu()

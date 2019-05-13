from gen_iii_booster import *
from gen_iv_booster import *


#takes in bytearray, saves bytes to file
def save_binary_file(data, file_name, path):
	
	output_path = asksaveasfilename(initialdir = path,  defaultextension = "", initialfile = file_name)
	
	output_binary = bytes(data)
	
	with open(output_path, 'wb') as f:
		f.write(output_binary)
	
def main(gen_number):

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
		
		em = calc_iii(em)
		file_name = "Emerald Scaled.gba"
		
		save_binary_file(em, file_name, output_path)

	#Gen IV
	elif(gen_number == 4.1):
		#get the data files and the output path
		trdata, trpoke, output_path = get_files_gen_iv(4.1)
	
		trpoke = calc_iv(trdata, trpoke)
	
		#seperates the file name (always a single character from HGSS on) from path
		file_name = output_path[-1]
		output_path = output_path[:-1]
	
		save_binary_file(trpoke, file_name, output_path)
		
	elif(gen_number == 4.2):
		#get the data files and the output path
		trdata, output_path = get_files_gen_iv(4.2)
		
		print('working 1')
	
		#trpoke = calc_iv(trdata, trpoke)
		
		print(len(trdata))
		trdata = doublify(trdata)
	
		#seperates the file name (always a single character from HGSS on) from path
	
		save_binary_file(trdata, 'trdata.narc', output_path)
		

def main_menu():
	global root_main_menu
	root_main_menu = Tk()

	frame_main_menu = Frame(root_main_menu)
	frame_main_menu.pack()
		
	root_main_menu.title('Select Game to modify')
	
	Button(frame_main_menu, text = 'Emerald', command = lambda: main('3.2'), height = 2, width = 50, pady = 1).pack()
	
	Button(frame_main_menu, text = 'Heart Gold/Soul Silver', command = lambda: main('4.1'), height = 2, width = 50, pady = 1).pack()
	
	Button(frame_main_menu, text = 'Platinum (doublify only)', command = lambda: main('4.2'), height = 2, width = 50, pady = 1).pack()
	
	Button(frame_main_menu, text="Exit", command = root_main_menu.destroy, height = 2, width = 25, pady = 1).pack()
	
	root_main_menu.mainloop()
	
		
main_menu()

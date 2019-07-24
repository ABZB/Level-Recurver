import io
import string
import math
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import binascii
import os
from statistics import median

def array_equality(x, y, length_matters_bool = True):
	#if the arrays are of different length and we care about that, return false now
	if((len(x) != len(y)) and length_matters_bool):
		return(False)
	else:
		#choose the least length, if we only care if those elements match
		for j in range(min(len(x), len(y))):
			if(x[j] != y[j]):
				return(False)
		
		#if we exited the above for loop without returning False, then they match, so:
		return(True)
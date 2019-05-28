# Trainer Expander/

Section I: Purpose

	* The instructions in Section III set every trainer in the base Black2/White2 game to have a team of at least 3 Pokemon. This both enhances the difficulty of the game, and in combination with the Level Recurver, allows for setting all battles to be Double, Triple, or Rotation battles.
	
	* Setting all trainers to a full party of 6 tends to result in a degree of tediousness, as well as making the level curve far to easy. As such, party sizes range from 3 to 6
	
	* This ONLY works for Black 2 and White 2
	
	* I do not reccomend using this unless you have experience with BWTE 2, and are comfortable with rebuilding narc files and nds files (using tools such as kiwi.ds and dsbuff)

Section II: Description of edits

	* Every trainer in the game Pokemon now has at least 3 Pokemon, with the size of their parties changing as follows:
		* 1 or 2 -> 3
		* 3 -> 4
		* 4 -> 5
		* 5 -> 6
		* 6 -> 6 (unchanged)
	* However, trainers that are intended to be battled as True Double Battles have all been set to have 3 Pokemon (The game otherwise crashes at some point in the battle. I suspect this occurs when the game tries to do display the enemy-team pokeball symbol corresponding to a Pokemon beyond the 3rd, (as the game freezes at the start-of-turn menu where that is displayed, and not when that Pokemon is sent out at the end of the previous turn).
	
	* The additional Pokemon are added randomly as follows:
		* If all the previous Pokemon of that trainer have a type or types in common, a Pokemon sharing at least one of those types will be selected at random.
		* If there is no such common type, a Pokemon that has none of those types in common will be selected at random.

Section III: Instructions 

	* Part A: Setup
	
		(1) Download and install AutoHotKey (https://www.autohotkey.com/).
		(2) Download BWTE 2 (Black White Trainer Editor 2)
	
	* Part B: Setting party sizes to minimum 3
	
		(1) Extract a/0/9/1 and a/0/9/2
		
		(2) Run BWTE2, and select a/0/9/1 for trdata, and a/0/9/2 for trpoke
		
		(3) Run Set_to_6.ahk (double-click on it)
		
		(4) Place your cursor in the 'Select Trainer' field of BWTE2
		
		(5) Hit CTRL+j
		
		(6) When the script finishes (it will keep running for several iterations past #813 Colress), you can close BWTE2.
		
		(7) Use a tool such as kiwi.ds to rebuild a/0/9/1 and a/0/9/2
		
		(8) a/0/9/1 is finished, all party sizes are now set to at least 3.
		
	* Part C: Filling in the blank party slots
		
		(1) Run Trainer_Expander.exe
		(2) Select the a/0/9/2 you rebuilt in step B-7
		(3) Save the output file

	* Part D: Recurving (optional but highly recommended)
		(1) Run Trainer_Level_Booster.exe, selecting the a/0/9/1 and a/0/9/2 files you modified in the previous steps.
		
	* Part E: Rebuilding the .nds file
		(1) Since the size of a/0/9/2 has increased greatly, simply reinserting the .narc will cause the game to not function. (I rebuilt the entire ROM using the ndsbuff tool).
# Trainer Expander/

Section I: Purpose

	* The instructions in Section III set every trainer in the base Black2/White2 game to have a team of 6 Pokemon. This both enhances the difficulty of the game, and in combination with the Level Recurver, allows for setting all battles to be Double, Triple, or Rotation battles.
	
	* This ONLY works for Black 2 and White 2
	
	* I do not reccomend using this unless you have experience with BWTE 2, and are comfortable with rebuilding narc files and nds files (using tools such as kiwi.ds and dsbuff)

Section II: Description of edits

	* Every trainer in the game that has fewer than 6 Pokemon now has 6 Pokemon.
	
	* The additional Pokemon are added randomly as follows:
		* If the nth slot is blank:
			* From the (n-1)th slot, the following is copied:
				* custom moves or hold items, if any (even if they make no sense)
				* Difficulty setting, gender/abilility setting, etc.
				* level, plus or minus 2
			* The species of Pokemon is chosen as follows:
				* A list is constructed of all the base-form Pokemon, excluding the >600 BST legendaries that share at least one type with the (n-1) Pokemon.
				* One of those Pokemon is chosen out of that list to be the nth Pokemon.
				* For example, if the Joey originaly has a 3-Pokemon team, with the 3rd Pokemon being a Raticate, the following is a possible filling-in of the rest of his team:
					* Slot 4 - Pidgey (shares Normal with Raticate)
					* Slot 5 - Tropius (share Flying with Pidgey)
					* Slot 6 - Lotad (shares Grass with Tropius.
				* The intent is that this will create variety while at least somewhat preserving theming of teams.

Section III: Instructions 

	* Part A: Setup
	
		(1) Download and install AutoHotKey (https://www.autohotkey.com/).
		(2) Download BWTE 2 (Black White Trainer Editor 2)
	
	* Part B: Setting party sizes to 6
	
		(1) Extract a/0/9/1 and a/0/9/2
		
		(2) Run BWTE2, and select a/0/9/1 for trdata, and a/0/9/2 for trpoke
		
		(3) Run Set_to_6.ahk (double-click on it)
		
		(4) Place your cursor in the 'Select Trainer' field of BWTE2
		
		(5) Hit CTRL+j
		
		(6) When the script finishes (it will keep running for several iterations past #813 Colress), you can close BWTE2.
		
		(7) Use a tool such as kiwi.ds to rebuild a/0/9/1 and a/0/9/2
		
		(8) a/0/9/1 is finished, all party sizes are now set to 6.
		
	* Part C: Filling in the blank party slots
		
		(1) Run Trainer_Expander.exe
		(2) Select the a/0/9/2 you rebuilt in step B-7
		(3) Save the output file

	* Part D: Recurving (optional but highly recommended)
		(1) Run Trainer_Level_Booster.exe, selecting the a/0/9/1 and a/0/9/2 files you modified in the previous steps.
		
	* Part E: Rebuilding the .nds file
		(1) Since the size of a/0/9/2 has increased greatly, simply reinserting the .narc will cause the game to not function. (I rebuilt the entire ROM using the ndsbuff tool).
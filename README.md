# Level Recurver

Section I: Purpose

	This program increases the level curve of enemy trainers.

	It currently works for the following games:

	Emerald
	HeartGold
	Soulsilver

	I plan to extend its functionality to at least Black2/White2.

	I do not plan to extend it to work with games from Generation VI onward, as tools to do so for those games already exist.

Section II: Description of edits

	FireRed (Beta):
	
	* Level curve rescaled so the Elite 4 has Pokemon at level 100 the first time (Need to rework level curve formula to mirror the one I made for later Gens).

	Emerald:
	
	* Level curve rescaled so the Elite 4 has Pokemon starting in the mid-90s. Gym Leaders and Team bosses are up to 20 levels higher than surrounding trainers.
	
	HGSS:

	* Level curve rescaled so the Elite 4 is roughly at the level it is in Generation I games, and Kanto trainers scale from there through level 100 (Kanto Gym Leaders will be leveled in the 90s).
	
	Platinum:

	* Level curve scaled so that Pokemon 5 levels less than the maximum level are at level 100.
	
	B2W2:
	
	* Level curve scaled so that Pokemon 5 levels less than the maximum level are at level 100. Note that this will affect all difficulty modes (the Key System). 
	

	All:

	* All trainer's Pokemon that could evolve at their new level are evolved one stage.
	* Please note that for any mod that adds trainers past the last indexed trainer of the base game, those additional trainers will not be modified, except in Gen IV, where I have been able to locate a fixed sequence that is always a fixed offset from the first values.

Section III: Options:

	* Rescale Level Curve - as per section II above.

	* Make Gym Leaders, E4 members, etc. Double Battles - All major story battles become double battles. This is the only battle-style changing option for Gen IV, as the game will crash if a singleton trainer sees the player and tries to step forward to initiate a double battle.
	
	* Make as many battles as possible double battles - All trainers with at least 2 Pokemon will now initiate Double Battles. This is only available for Emerald.
	
	* Make as many battles as possible Double, Triple, or Rotation battles (Black2/White2 only):
		* All Trainers with exactly 1 Pokemon are unchanged.
		* Non-stationary Trainers with exactly 1 or 2 Pokemon are unchanged.
		* Trainers that already challenge you to a Double, Triple, or Rotation battle are unchanged.
		* Stationary Trainers (such as Gym Leaders) with exactly 2 Pokemon now challenge you to Double Battles.
		* Stationary Trainers with at least 3 Pokemon now challenge you to a Double, Triple, or Rotation Battle with a 1/3 chance of each per trainer (each one is set when this program is run, not when you actually battle them in-game).
		* Non-stationary Trainers with 3 or more Pokemon now challenge you to a Single, Triple, or Rotation with a 1/3 chance of each per trainer (each one is set when this program is run, not when you actually battle them in-game).
		
	* Custom Offset:
		* Allows entry of custom offset for Trainer Data for mods with shifted offsets. The user can also select to enter the offset in either Decimal or Hexadecimal.
	* Custom Trainer count:
		* Allows entry of custom numbe of trainers for mods with extended trainer lists. The entry must be a positive decimal integer.

Section IV: Instructions

	1) Decompress the NDS file using an appropriate tool.

	2) Run Trainer Level Booster

	3) Select the target game

	4) Select the appropriate files as instructed:

			* FireRed/Emerald: Select the .gba file
			* HGSS: root/a/0/5/5 (Trdata) then root/a/0/5/6 (Trpoke)
			* Platinum: root/poketool/trainer/trdata then root/poketool/trainer/trpoke
			* B2W2: root/a/0/9/1 (Trdata) then root/a/0/9/2 (Trpoke)
	
	5) A prompt will appear to save the edited file.
	
	6) NDS games only: Rebuild the NDS file.
	
Section IV: Be aware of the following:

	1) If your trdata or trpoke were edited in a way that changes the offset of the first trainer or Pokemon, the program will (probably) run, but the output will not be good. As this program does not alter any offsets, try running this before applying any other patches, if possible.

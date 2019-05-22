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

	Emerald (beta):
	
	* Level curve rescaled so the Elite 4 has Pokemon starting in the mid-90s. Gym Leaders and Team bosses are up to 20 levels higher than surrounding trainers.

	HGSS:

	* Level curve rescaled so the Elite 4 is roughly at the level it is in Generation I games, and Kanto trainers scale from there through level 100 (Kanto Gym Leaders will be leveled in the 90s).
	
	B2W2:
	
	* Level curve scaled so that Pokemon 5 levels less than the maximum level are at level 100. Note that this will affect all difficulty modes (the Key System). 
	

	All:

	* All trainer's Pokemon that could evolve at their new level are evolved one stage.
	* Please note that for any mod that adds trainers past the last indexed trainer of the base game, those additional trainers will not be modified, except in Gen IV, where I have been able to locate a fixed sequence that is always a fixed offset from the first values.

Section III: Options:

	* Rescale Level Curve - as per section II above.

	* Make Gym Leaders, E4 members, etc. Double Battles - All major story battles become double battles. This is the only battle-style changing option for Gen IV, as the game will crash if a singleton trainer sees the player and tries to step forward to initiate a double battle.
	
	* Make as many battles as possible double battles - All trainers with at least 2 Pokemon will now initiate Double Battles. This is only available for Emerald.
	
	* Make as many battles as possible Double, Triple, or Rotation battles - All trainers with non-stationary trainer classes (such as Gym Leaders) and at least 3 Pokemon are randomly assigned one of Triple or Rotation battles (this is done when the program is run, every time it is run it will generate a different spread). Stationary trainer classes with at least three Pokemon are randomly assigned one of Double, Triple, or Rotation battles. Stationary trainer classes with exactly two Pokemon are assigned Double battles. All other trainers (including those that are already not single battles) are unchanged.

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

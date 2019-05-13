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


	All:

	* All trainer's Pokemon that could evolve at their new level are evolved one stage.


Section III: Instructions

	1) Decompress the NDS file using an appropriate tool.

	2) Run Trainer Level Booster

	3) Select the target game

	4) Select the appropriate files as instructed:

			* FireRed/Emerald: Select the .gba file
			* HGSS: root/a/0/5/5 (TRdata) then root/a/0/5/6 (TRpoke)
	
	5) A prompt will appear to save the edited file.
	
	6) NDS games only: Rebuild the NDS file.
	
Section IV: Be aware of the following:

	1) If your trdata or trpoke were edited in a way that changes the offset of the first trainer or Pokemon, the program will (probably) run, but the output will not be good. As this program does not alter any offsets, try running this before applying any other patches, if possible.

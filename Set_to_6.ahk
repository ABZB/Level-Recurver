#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.



; ctrl + j to start

^j::
Loop, 813
{

	;First, check if the trainer is a single battle type with a Double Battle AI, if so, set their number of Pokemon to 3
	
	;if the trainer is the first rival battle, don't add anything (otherwise you end up in a one-on-three or a glitch)

	;get trainer name
	Send ^{c}
	Sleep 2
	trainer_name := Trim(clipboard)
	Sleep 2
	
	; 1 tab backward to AI
	

		Send +{tab}
		Sleep 2

	
	; get AI into clipboard
	Send ^{c}
	Sleep 2
	ai := Trim(clipboard)
	Sleep 2
	if(ai = "128" or ai = "129" or ai = "135" or ai = 128 or ai = 129 or ai = 135)
	{
		Sleep 2
		; go back 2 to Battle Type
		Send +{tab}
		Sleep 2
		Send +{tab}
		Sleep 2
		
		; get Battle Type into clipboard
		Send ^{c}
		Sleep 2
		bttl_typ := Trim(clipboard)
		Sleep 2
		if(bttl_typ = "Single Battle")
		{
			;go back to party count
			Loop, 6
			{
				Send {tab}
				Sleep 2
			}
			
			;set to 3
			Send {3}
		}
	}
	else
	{
		; otherwise set party count as follows: {1,2} -> 3, {3} -> 4, {5} -> 6
			Loop, 4
			{
				Send {tab}
				Sleep 2
			}
		
		Send ^{c}
		Sleep 2
		prty_cnt := Trim(clipboard)
		;MsgBox % prty_cnt
		
		;if it's the first rival battle, do nothing
		if(prty_cnt = 1 or prty_cnt = 2 or prty_cnt = "1" or prty_cnt = "2")
		{
			if(trainer_name = "Hugh - 161" or trainer_name = "Hugh - 162"  or trainer_name = "Hugh - 163" or trainer_name= "N - 6" or trainer_name= "N - 5")
			{
				Sleep 2
			}
			else
			{
				Send {3}
				Sleep 2
			}
		}
		else if(prty_cnt = 3 or prty_cnt = "3")
		{
			Send {4}
			Sleep 2
		}
		else if(prty_cnt = 4 or prty_cnt = "4")
		{
			Send {5}
			Sleep 2
		}
		else if(prty_cnt = 5 or prty_cnt = "5")
		{
			Send {6}
			Sleep 2
		}
		
	
	}
	
	; move to save trainer button and save
	Send +{tab 2}
	Sleep 2
	
	Send {Space}
	Sleep 2	
	
	; return to trainer selection dropdown and move down by one
	Send +{tab}
	Sleep 10
	
	Send {Down}
	Sleep 5
	
}
return
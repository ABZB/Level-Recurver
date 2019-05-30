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
	trainer_name := Trim(clipboard)
	
	
	; 13 tabs to AI numberdo it in pieces b/c otherwise BWTE gets upset
	
	Loop, 13
	{
		Send {tab}
		Sleep 1
	}
	
	; get AI into clipboard
	Send ^{c}
	
	ai := Trim(clipboard)
	
	if(ai = "128" or ai = "129" or ai = "135" or ai = 128 or ai = 129 or ai = 135)
	{
		; go back 2 to Battle Type
		Send +{tab}
		
		; get Battle Type into clipboard
		Send ^{c}
		bttl_typ := Trim(clipboard)

		if(bttl_typ = "Single Battle")
		{
			;go back to party count
			Loop, 8
			{
				Send +{tab}
				Sleep 1
			}
			
			;set to 3
			Send {3}
		}
	}
	else
	{
		; otherwise set party count as follows: {1,2} -> 3, {3} -> 4, {5} -> 6
			Loop, 10
			{
				Send +{tab}
				Sleep 1
			}
		
		Send ^{c}
		Sleep 1
		prty_cnt := Trim(clipboard)
		;MsgBox % prty_cnt
		
		;if it's the first rival battle, do nothing
		if(prty_cnt = 1 or prty_cnt = 2 or prty_cnt = "1" or prty_cnt = "2")
		{
			if(trainer_name = 'Hugh - 161' or trainer_name = 'Hugh - 162'  or trainer_name = 'Hugh - 163')
			{
				Sleep 1
			}
			else
			{
				Send {3}
				Sleep 1
			}
		}
		else if(prty_cnt = 3 or prty_cnt = "3")
		{
			Send {4}
			Sleep 1
		}
		else if(prty_cnt = 4 or prty_cnt = "4")
		{
			Send {5}
			Sleep 1
		}
		else if(prty_cnt = 5 or prty_cnt = "5")
		{
			Send {6}
			Sleep 1
		}
		
	
	}
	
	; move to save trainer button and save
	Send +{tab 2}
	Sleep 1
	
	Send {Space}
	Sleep 1
	
	; return to trainer selection dropdown and move down by one
	Send +{tab}
	Sleep 20
	
	Send {Down}
	Sleep 1
	
}
return
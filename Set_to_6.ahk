#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.



^j::
Loop, 850
{
	Send {tab 3}
	Sleep, 1
	
	Send {6}
	Sleep, 1
	
	Send +{tab 2}
	Sleep, 1
	
	Send {Space}
	Sleep, 1
	
	Send +{tab}
	Sleep, 1
	
	Send {Down}
	Sleep, 1
	
}
return
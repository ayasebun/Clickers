#SingleInstance
winclass = i)LOST.*ARK
SetTitleMatchMode, 2
SetKeyDelay 20,10 ;Change the values here if you think its going too fast. [Delay,PressDuration]

;CTRL + Middle mouse button will start this section 
^MButton::

; Send Spacebar input n times based on SetKeyDelay parameter above
Send {Space 15}
return

;SHIFT+q closes AHK app entirely
+q::ExitApp    ;exits this script
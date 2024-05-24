#SingleInstance
winclass = i)LOST.*ARK
SetTitleMatchMode, 2
SetKeyDelay 20,10 ;Change the values here if you think its going too fast. [Delay,PressDuration]

;CTRL+SPACE to start 
^Space::
winetrigger=0
while winetrigger=0
{
    sleep, 100
    ; Update these x/y values to match your screen
    Click 940 530 3 Right
    sleep, 100
    ; Update these x/y values to match your screen
    Click 940 920 3 Left
    sleep, 61000
}
return        ;ends wine purchase part of the script

;CTRL+q to stop the script
^q::winetrigger=1    ;sets winetrigger=1 to end loop

;CTRL + Middle mouse button will start this section 
^MButton::

; Send Spacebar input n times based on SetKeyDelay parameter above
Send {Space 15}
return

;SHIFT+q closes AHK app entirely
+q::ExitApp    ;exits this script
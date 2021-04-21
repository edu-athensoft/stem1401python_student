"""
reverse engineering
1. evaluate the product/result (observe)
   outlook, metric, functionality
2. analyze the result
3. reproduce
4. assembly
5. test
6. deliver

engineering
1. idea
2. design/plan
3. implement
4. test
5. deliver
"""

"""
precisely and completely
"""

"""
Kevin
1. First there is a label with a number as text
2. below, there is 3 buttons
3. The most right button is the exit button, which closes the widget when pressed
4. In the middle, when pressed, the button increases the number on the label by 2
5. At the most left, the button reduces the number on the label by 2 when clicked
6. The limit to increase is 10 and to decrease is -10. When it reaches 10, the + button becomes disabled.
When it reaches -10, the - button becomes disabled.
"""

"""
Yuhao
One label and three buttons :
In the label : Start number : 0 
There are 3 buttons in the bottom side: 
first one is for -2, second one is for +2, third one is for exit the program
If you click for fist button : start number will be -2, ...
The minimum of the number will be -10, and the max will be 10
### missing description of button state [+]button and [-]button
"""

"""
Zeyue
1. There is a label with 3 buttons below. 
2. The buttons are on the bottom of the label, with -, +, and Exit on them respectively from the left. 
Label starts with 0, goes down by -2 each time the - button is pressed to a maximum of -10 which disables the - button 
when reached and goes up by 2 each time the + button is pressed to a maximum of 10, which disables the + button when 
reached. 
3. Exit button terminates the program. 
4. Buttons have the same x padding but are different in size due to length of 
the content.
"""


"""
Guangzhu 
There is a window with a 0 on it and 3 buttons: add, decrease and exit
1. when you press the add button, the number on the window is increased by 2
2. when you press the minus button, the number on the window is decreased by 2
3. when the number reaches 10 you can't add anymore and the add button is disabled
4. when the number reaches -10 you can't decrease anymore and the minus button is disabled
5. when you press the exit button, the window will disappear and the program is ended
### missing label
"""


"""
Chengjun
1----there is a label with 3 buttons
2---button : two button with the+ or-,and each time we click on it,
it will-or+2,
3---and there is a button of exit,it will exit if you click on
4---the maximum of the num is10 and the minimum is -10
### missing state of buttons
"""




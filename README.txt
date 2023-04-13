Program works on Windows (may work on other platforms, but didn't test it)
Any emulator is required, for example Bluestacks
---------------------------------------------------
(I recommend: in the game click Option -> Save -> Yes -> Go Back)
After every unsuccessful class research (almost every try), program loads data from cloud to retrieve gems
Every time you use the program, you have to:
1. Enter Shop and click Research Data for 20 gems (they will be retrieved by game's load feature)
2. Take screenshot of a brighter box with any class that appeared (check screenshot_area.png in this folder)
3. Save it exactly as "cords.png" in this folder (in current directory)
4. Run MSClassGetter.exe (by double clicking it)
5. Pay attention to don't allow any program window cover game window while MSClassGetter.exe is working
(program constantly takes screenshot of the middle game area to recognize classes)
Screenshot which you saved at the beginning is used as source of information about screen coordinates,
so you have to take it and save before every program start (or you can set static coordinates).
---------------------------------------------------
How to solve problems:
If program clicks in wrong places, it probably means that screenshot was taken unprecisely (check screenshot_area.png in this folder)
---------------------------------------------------
Additional info:
Don't resize or change game window position when program is running.
You can change them after stopping program.
To stop running program, click program's window and from keyboard Ctrl + C
You have to do it quickly;)
Program will also stop when given requirements are met.
If you run emulator with admin persmissions, then you have to run MSClassGetter.exe also with admin permissions,
to allow it click on program (emulator) with admin permissions.
(NN_save.txt keeps saved neural network data and .exe needs it to work)
You can see whole program if you want to know how it works (MSClassGetter.py). 
It's in this folder an hidden file. Feel free to change and compile for personal use.
Program's repository: https://github.com/firstas/magic_survival_AI_class_getter
Thanks for using my program, feedback is appreciated;)
---------------------------------------------------
Additional info about config_yourself.txt:
Changing its content is optional.
The DELAYS section affects program directly.
Changing delays is fully reversible, but better test without saving classes (type 0 in MSClassGetter.exe window)
while experimenting because e. g. when time "between clicking "LOAD" and "Return":" is to low,
program will try to recognize screen with "Successfully loaded." message and "Return" button
as a class, which seems most similiar to druid among all classes, which will buy druid if
it is the class the program is searching for.
In my tests when "between clicking "Return" (after LOAD) and "Shop":" was too low, astronomer or druid were "recognized".
When "waiting for class image to set its colors from white flash after clicking "Research Data":" was too low,
usually "game has lagged" or druid (once again) were recognized.
If program already works properly, increasing values won't change anything
besides increasing stability (good) and average time needed to get classes (bad).
It's about balance, as always.

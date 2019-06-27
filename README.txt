1 2 3 Learn! is an interactive learning game for young children, to help them learn math, focus on handwriting, and improve analytical skills. The main module is the Bubble Game, where bubbles containing addition, subtraction, and multiplication problems fall from the top of the screen. The user draws the answer which, if correct, results in the bubble popping. If the user needs to work on a certain topic, there is an algorithm such that he or she will receive more questions regarding that specific topic and be asked questions he or she previously got wrong. There are two additional modules, as well. One allows the user to choose a topic and practice with more advanced problems in addition, subtraction, multiplication, and basic division in the style of flashcards. The other presents the user with an adventure and a task that he or she must complete, giving the user a more real life application of these mathematical topics. The story mode also introducing the concept of fractions, addition with negative numbers, and computation with more than two numbers. 

How to run:
Make sure the following files are in the same directory:
	main_.py
	ml_main.py
	bubble_game.py
	flashcards_.py
	leaderboard_.py
	progress_rep.py
	start_screen.py
	divide_.py
	orchard_.py
	recipe_.py
	module_manager.py
	mnist.pkl
	leaderboard_data.txt
	images (folder, which contains: flashcards (folder, 1 item), large_bubble (folder, 7 items), login (folder, 3 items), story (folder, 41 items), title (folder, 4 items), chart.png, ldbrd.png, prgr.png)

If all these files are in one directory, running main_.py in the editor will launch the game. 


Libraries:
You will need the following libraries: sklearn, PIL, matplotlib.pyplot, numpy, _pickle, and gzip. _pickleand gzip are built in modules in Python 3+. For the rest, running Austin’s module manager will prompt you to install any of these libraries that are not on your computer. If it does not, however, you can install them in the terminal with the following commands:
	pip install numpy
	pip install -U scikit-learn (after numpy is installed)
	pip install PIL
	python -m pip install -U matplotlib

Shortcut Commands:
Pressing “c” in the Bubble Game mode automatically bursts the bubble and records the answer as correct. Hence, if you comment out the training of the classifier in timerFired( ) and change data.mode = “loading” to data.mode = “input”, you can skip the machine learning part but still test everything else.
Pressing “p” in the recipe aspect of the Story mode automatically completes all tasks. 
Pressing “o” in the apple orchard mode automatically removes the apple tree and allows Chris to move forward, so again training the classifier is not necessary. 



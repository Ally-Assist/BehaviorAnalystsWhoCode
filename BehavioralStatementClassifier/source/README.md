# Setup of Project BehavioralStatementClassifier

Python project under PyCharm for a presentation on Sunday 25 September 2021 @ 12:00 to the Slack channel, [Behavior Analysts Who Code (BAWC)](https://www.codingbehavioranalysts.org)

For an overview of the project and the demo, see the [README.md](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode/tree/main/BehavioralStatementClassifier) one level up.

***This will change frequently up to the presentation date***


Tom Donaldson

tom.donaldson@performanceally.com

Created: Saturday 11 September 2021


# How I Set Up the Project

***If you download the project from GitHub, all of this is done.*** 

I do almost all of my work on a Mac, with forays to other forms of Unix, particularly the Ubuntu Linux variety commonly used within [Docker containers](https://www.docker.com/resources/what-container). Do I ever use MS Windows? Maybe once a year or so. Just often enough that I end up renewing my annual license for [Parallels Desktop](https://www.parallels.com/). That will probably come to an end, as Microsoft has announced that they will not support Apple's new M1 processor.

I will illustrate part of the setup process. I make no guarantee that this will work. Perhaps in future presentations I can pair with you to get your installation working to show others what is involved (and update these online docs accordingly). One issue is that the setup is different if you are starting from scratch. I have been using PyCharm on and off for around two years now.

But, I will recreate the steps that I can as best as I can here, for now.

# Starting Point

Starting with local copy of the [Ally-Assist/For-BehaviorAnalystsWhoCode repository](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode), this is how *(I think)* I, initialized to the PyCharm Python project. 

Install the free [Community version of PyCharm](https://www.jetbrains.com/pycharm/download/) for your machine. I cannot describe the process for installing and setting it up because (a) I already have it, and (b) it has been installed for years. As I remember it, the process is very simple on Mac.

I have my local work directories for GitHub repositories under my home directory. The full path to my local project folder for this project on my Mac is:

	~/LocalDevelopment/AllyAssist/BehaviorAnalystsWhoCode/BehavioralStatementClassifier

# Basic Project PyCharm Startup

1. Update to the [latest version of Python](https://www.python.org/downloads/), which as of Friday 17 September 2021, was v3.9.7.

1. Start PyCharm

1. In the `File` menu, select `New Project...`

1. A dialog pops up. In case you have not already noticed, this is not a native Mac app. It is probably written in Java. In any case, 

	1. `Pure Python` should be selected on the left.
	
	1. To the far right of the `Location` field, I clicked the tiny folder icon.
	
	1. Now a native file menu appears. I navigated to the location where I wanted to create the actual PyCharm Python code project:
	
		- `~/LocalDevelopment/AllyAssist/BehaviorAnalystsWhoCode/BehavioralStatementClassifier`
	
	1. I clicked `New Folder`, and entered `source` as the new folder name.
	
	1. I clicked the `Create` button, followed by the`Open` button.
	
	1. From here on out, all files managed by PyCharm for the project will be under this `source` directory.

1. Set up the Python interpreter.

	1. Under `Location` you should see `Python Interpreter`.
	
	1. There should be a couple of choices under it, click the little triangle just on the left of `Python Interpreter`
	
	1. Choose `New environment using`, then choose `Pipenv` from the pulldown menu.
	
	1. From the pulldown menu for `Base interpreter`, select the most recent version of Python.

1. Click the `Create` button at the bottom right of the dialog.

1. If you look at the contents of the `source` directory, you will now find a hidden folder named `.idea`. This is the folder in which PyCharm saves all of its settings for your project. If you delete the `.idea` directory you will have to completely reconfigure the project. Not a big deal now, but later ...

1. At this point you will just need to explore a bit on your own to find your way around. Here is a good starting point: [PyCharm: Overview of the user interface](https://www.jetbrains.com/help/pycharm/guided-tour-around-the-user-interface.html)


# Activate Python environment in Terminal

In PyCharm's Terminal (see tabs at bottom of the window), type this command, to see what version of Python is enabled there. It ***should*** be the one you set above, but probably will not be. The default Python on macOS is v2.7, which is kept around for compatibility with legacy software. 

If you are using the terminal app without a Python virtual environment, here is what you will likely see:

	>which python
	
	/usr/bin/python
	
	>python --version
	
	Python 2.7.16

To get it to use the correct Python environment, enter this command. You should see something like the output shown for the command, but ignore it for the moment.

	>pipenv shell
	
	Launching subshell in virtual environment...

	The default interactive shell is now zsh.
	To update your account to use zsh, please run `chsh -s /bin/zsh`.
	For more details, please visit https://support.apple.com/kb/HT208050.
	bash-3.2$  . /Users/tompadonaldson/.local/share/virtualenvs/BehavioralStatementClassifier-KAKETNmX/bin/activate
	(BehavioralStatementClassifier) bash-3.2$ exit

Now if ask "which Python installation am I using", you should see something like this. This is the private virtual environment that you set up for the project. You can freely update it (more on that later) without affecting any other project.
	
	>which python
	
	~/.local/share/virtualenvs/BehavioralStatementClassifier-KAKETNmX/bin/python
	
	>python --version
	
	Python 3.9.7

You should not have to set the Python environment like this again, but that is all there is to it if you do. The terminal will now have access to all Python packages installed in the project, by default.

If as above you see this output from `pipenv shell`, and you have already set your default shell to `zsh`, the solution is in the preferences for the project:

	The default interactive shell is now zsh.
	To update your account to use zsh, please run `chsh -s /bin/zsh`.

To fix it, go back to Preferences, then `Tools > Terminal`. Just under the `Application Settings` heading is `Shell path:`. Enter this in the text box, and apply: `/bin/zsh`. Go back to the Terminal pane in PyCharm, and enter a non-existent command. `Zsh` should complain, versus `bash` complaining:

	>fubar --snafu
	
	zsh: command not found: fubar

Note that if you go to PyCharm's preferences, select `Project: BehavioralStatementClassifier`, then `Project Interpreter`, you will see the same path shown for the interpreter.

Also note the window below the `Python Interpreter` line. That panel shows all of the Python packages that are already install for the project. If you click the `+` on the toolbar for the pane, you can add packages. You will only affect this project, and no other.

	


# BehavioralStatementClassifier Package

A [Python package](https://docs.python.org/3/tutorial/modules.html#packages) is code module that can be referenced by name, usually as a means of importing functionality. Our top level package will be `BehavioralStatementClassifier`. 

1. In PyCharm open `BehaviorStatementClassifier`. All files under the [main project directory](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode/tree/main/BehavioralStatementClassifier) will be present.

1. Create the top level Python package by selecting the `source` directory in the PyCharm navigator, and control-click that `source` directory. Choose `New>Python Package`. Type `BehavioralStatementClassifier`. This is the top level Python "library". The `source` directory should have a sub-directory named `BehavioralStatementClassifier`, and there should be a file under that directory named `__init__.py`. We will ignore the file, for now.

Within the `BehavioralStatementClassifier` package we will have at least two sub-packages that can be used by name:

1. ***Model:*** The guts of the application, as described above as the "M" in "MVC".

1. ***DesktopGui:*** A desktop graphical user interface. This will be one possible set of view controllers, the "VC" in "MVC". We will create this package, but leave it empty for now.

I leave this up to you. Creating a package under an existing package follows the same process as above, except that you create the sub-packages under `BehavioralStatementClassifier` instead of `source`.

Now, we need to correctly identify the top level content (source) of the project.

1. In project preferences (Cmd-, on Mac), 

1. under Project > Project Structure, 

1. delete whatever content root is shown on the right (click the 'x' on the far right). 

1. Click `Add Content Root`, and navigate to the top level package directory, `BehavioralStatementClassifier`. 

1. Click open. 

Python import statements should now find the modules of the project.


# PyTest

Be sure these PyTest packages are installed. See Preferences (i.e., Cmd-,) under Project > Python Interpreter. If these packages are not listed, click the `+` above the `Package` column and search for them:

1. pytest

1. pytest-cov

1. pytest-forked

1. pytest-xdist


Do this command in the terminal window to run all of your tests in parallel:

	>pytest -n auto
	
You should see output something like this, which shows no errors:

	====================================================================================================================== test session starts ======================================================================================================================
	platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
	rootdir: /Users/tompadonaldson/LocalDevelopment/AllyAssist/BehaviorAnalystsWhoCode/BehavioralStatementClassifier/source/BehavioralStatementClassifier
	plugins: cov-2.12.1, xdist-forked-0.0.1, forked-1.3.0
	gw0 [1] / gw1 [1] / gw2 [1] / gw3 [1] / gw4 [1] / gw5 [1] / gw6 [1] / gw7 [1] / gw8 [1] / gw9 [1] / gw10 [1] / gw11 [1] / gw12 [1] / gw13 [1] / gw14 [1] / gw15 [1] / gw16 [1] / gw17 [1] / gw18 [1] / gw19 [1] / gw20 [1] / gw21 [1] / gw22 [1] / gw23 [1]
	.                                                                                                                                                                                                                                                         [100%]
	======================================================================================================================= 1 passed in 2.54s =======================================================================================================================



Run this command in the terminal window to see how much of your code is covered by the tests you have so far:

	> pytest -n auto --cov=Model/ --cov=DesktopGui/ --cov=WebGui

You should see something along the lines of this:

	====================================================================================================================== test session starts ======================================================================================================================
	platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
	rootdir: /Users/tompadonaldson/LocalDevelopment/AllyAssist/BehaviorAnalystsWhoCode/BehavioralStatementClassifier/source/BehavioralStatementClassifier
	plugins: cov-2.12.1, xdist-forked-0.0.1, forked-1.3.0
	gw0 [1] / gw1 [1] / gw2 [1] / gw3 [1] / gw4 [1] / gw5 [1] / gw6 [1] / gw7 [1] / gw8 [1] / gw9 [1] / gw10 [1] / gw11 [1] / gw12 [1] / gw13 [1] / gw14 [1] / gw15 [1] / gw16 [1] / gw17 [1] / gw18 [1] / gw19 [1] / gw20 [1] / gw21 [1] / gw22 [1] / gw23 [1]
	.                                                                                                                                                                                                                                                         [100%]

	---------- coverage: platform darwin, python 3.9.7-final-0 -----------
	Name                                           Stmts   Miss  Cover
	------------------------------------------------------------------
	DesktopGui/__init__.py                             0      0   100%
	Model/Statement.py                                18      0   100%
	Model/__init__.py                                  0      0   100%
	Model/tests/__init__.py                            0      0   100%
	Model/tests/fixture_raw_statements_subset.py      18     18     0%
	Model/tests/test_Statement.py                     25      1    96%
	WebGui/__init__.py                                 0      0   100%
	------------------------------------------------------------------
	TOTAL                                             61     19    69%

	======================================================================================================================= 1 passed in 3.17s =======================================================================================================================



# End, for now.





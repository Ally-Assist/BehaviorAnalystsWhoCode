# Setup of Project BehavioralStatementClassifier

Python project under PyCharm for a presentation on Sunday 25 September 2021 @ 12:00 to the Slack channel, [Behavior Analysts Who Code (BAWC)](https://www.codingbehavioranalysts.org)

For an overview of the project and the demo, see the [README.md](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode/tree/main/2021_09_25%20Pinpointing%20Behavior%20Statements) one level up.

***This will change frequently up to the presentation date***


Tom Donaldson

tom.donaldson@performanceally.com

Created: Sunday 22 August 2021


# Project Setup

***If you download the project from GitHub, all of this is done.*** I just want to illustrate this part of the setup process.

I am starting with a local copy of the repository, initialized to the point at which it is ready to create the PyCharm Python project. We can cover how to get to this starting point elsewhere and elsewhen.

Install the free [Community version of PyCharm](https://www.jetbrains.com/pycharm/download/) for your machine. I cannot describe the process for installing and setting it up because (a) I already have it, and (b) it has been installed for years. As I remember it, the process is very simple on Mac.

I have my local work directories for GitHub repositories under my home directory. The full path to the project folder for this project is:

	"LocalDevelopment/AllyAssist/BehaviorAnalystsWhoCode/2021_09_25 Pinpointing Behavior Statements"

Here is what I did:

1. Updated to the [latest version of Python](https://www.python.org/downloads/), which was v3.9.7.

1. Started PyCharm

1. In the `File` menu, select `New Project...`

1. A dialog pops up. In case you have not already noticed, this is not a native Mac app. It is probably written in Java. In any case, 

	1. `Pure Python` should be selected on the left.
	
	1. To the far right of the `Location` field, I clicked the tiny folder icon.
	
	1. Now a native file menu appears. I navigated to the location where I wanted to create the actual PyCharm Python code project (I am regretting the long directory names):
	
		- `LocalDevelopment/AllyAssist/BehaviorAnalystsWhoCode/2021_09_25 Pinpointing Behavior Statements/2021_09_25 Pinpointing%20Behavior Statements`
	
	1. I clicked `New Folder`, and entered `source` as the new folder name.
	
	1. I clicked the `Create` button, followed by the`Open` button.
	
	1. From here on out, all files managed by PyCharm for the project will be under this `source` directory.

1. Set up the Python interpreter.

	1. Under `Location` you should see `Python Interpreter`.
	
	1. There should be a couple of choices under it, click the little triangle just on the left of `Python Interpreter`
	
	1. Choose `New environment using`, then choose `Pipenv` from the pulldown menu.
	
	1. From the pulldown menu for `Base interpreter`, select the most recent version of Python.

1. Click the `Create` button at the bottom right of the dialog.

1. If you look at the contents of the `source` directory, you will now find a hidden folder named `.idea`. This is the folder in which PyCharm saves all of its settings for your project. If you delete the `.idea` directory you will have to completely reconfigure the project. Now a big deal now, but later ...

1. At this point you will just need to explore a bit on your own to find your way around. Here is a good starting point: [PyCharm: Overview of the user interface](https://www.jetbrains.com/help/pycharm/guided-tour-around-the-user-interface.html)


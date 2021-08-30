# 2021_09_25 Pinpointing: Is It A Behavior?

Subtitle: **A Quick Overview of Professional-Style Software Development in Python**

Material related to a presentation on Sunday 25 September 2021 @ 12:00 to the Slack channel, [Behavior Analysts Who Code](https://www.codingbehavioranalysts.org)

***This will change frequently up to the presentation date***


Tom Donaldson

tom.donaldson@performanceally.com

Created: Sunday 22 August 2021

---

# Overview

During a lengthy [discussion with the Slack channel owner, David Cox](https://behavioranaly-yw87919.slack.com/archives/D02APN949UL), I agreed to do one presentation to the Behavior Analysts Who Code (BAWC) Slack channel on Sunday 25 September 2021 @ 12:00 eastern USA time.

What the presentation will be is evolving. Will it be a simple presentation (unlikely)? A live programming demo (probable)? A workshop (probably not this time)?  In any case, the focus of the presentation/demo/workshop will be software development practices wrapped up in a behavior analytic scenario.

The long term goal is to help foster a deeper understanding of software development among behavior analysts to facilitate their own coding as well as make their interactions with professional software development groups more effective. Or something.

If participants are interested, the project may be included in future Saturday workshops outside the usual BAWC meetup schedule. Again, the purpose is to promote software development skills within the behavior analytic community. Such "workshops" would include online participation by attendees, including taking part in writing and debugging code (see "[pair programming](https://en.wikipedia.org/wiki/Pair_programming)").

***Formatting Note:*** As above, I have included links throughout this page to more in depth information. So much information, so little time.

### Rationale

David and I discussed options. The basic drivers in developing the presentation will be:

1. Software development skills of the audience are all over the place.

	1. Just starting.
	
	2. Computer science background.
	
	3. Professional (or retired) software developers? I may be the only one.

2. Given the audience experience with software development, or the lack of it, this first presentation needs to be very general, and perhaps skimpy on details.

3. The "software development project" must be in some way relevant to behavior analysis. 

3. For the project to be intrinsically interesting to me, and to maintain my responding, it should be in some way relevant to my current work. That is, applied behavior analysis in general, or OBM in particular (vs basic experimental or neural nets).

4. After discussion with, and the approval of, Julie Smith, I will use some sort of classification of textual statements as behavioral (or not) as the initial scenario.


### General Format

Duration of the presentation: At David's suggestion, I considered going for up to 90 minutes. Sounded good at the time, but realistically I simply cannot do it. So: max of 60 minutes, and I will try to spend most of that time on the live-programming-demo.

Therefore, I will cover the following topics superficially to provide a context for the demo. The text here includes numerous links to more in depth information for those who want it.

1. ***[Scenario](#1-scenario):*** Behavior analytic scenario as the motivation for the project.

2. ***[Development Strategy](#2-development-strategy):*** Overall (basic) development strategy in terms of incremental phases shaping the functionality of the code toward the overall goal.

3. ***[Basic Requirements of Prototype](#3-basic-requirements-of-prototype):*** What will the first prototype phase do?

4. ***[Major Software Components](#4-major-software-components):*** The logical units of software which implement specific behaviors. Taken as a whole, an application (or model) can be viewed as an emergent arising from all of the components interacting.

5. ***[Tools](#5-tools):*** Software that will be used in the initial "simple prototype" phase, plus some possible tools for future directions.

6. ***[A Development Process](#6-a-development-process):*** A tentative set of steps in using the tools to meet the requirements specified for the application scenario. 

7. ***[Demo: Continuous-Feedback Development](#7-demo-continuous-feedback-development):*** Demo with live development project (will have basic framework in place, then do some coding to illustrate one important concept in more detail, e.g., test driven design)

8. Where to go from here? What might a next step be? Do it in another presentation?

---


# 1. Scenario

***What is the behavior analytic purpose?***

Collecting and evaluating statements of behavior as part of identifying behaviors important in producing some result, otherwise known as, "pinpointing vital behaviors".

### General Need

Would like software that would facilitate the process of training people to do the classification, and to collect classifications of large volumes of behavior statements.

The general criteria. To be a behavior, for our purposes:

1. Measurable: Must be observable by others than the performer: seen, heard, felt, smelled, tasted.

2. Objective: Must be confirmable by others.

3. Active: Only a living organism can do it (see also: Dead Man Test)

4. Neutral: Non-biased, non-judgmental, non-emotional.

A few relevant articles:

1. A "must read" by Critchfield and Shue: [The Dead Man Test: a Preliminary Experimental Analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6269387/pdf/40617_2018_Article_239.pdf)

2. [How to Pinpoint Behavior Effectively](https://centralreach.com/how-to-pinpoint-behavior-effectively/): More inclusive than our current project. We will focus on the "Movement Cycle" (action verb and object).

3. [Vital Behaviors](https://sourcesofinsight.com/vital-behaviors/)


---

# 2. Development Strategy

***How to break it down into digestible chunks?***


### 2.1 A Possible End Goal

A system that can be used by large numbers of users evaluating large numbers of statements, marking them as to their behavioral/non-behavioral characteristics. Statistics automatically collected to decide which statements are behavioral in what ways; which statements might be modified to be behavioral, and in what ways. Inter-observer agreements by statement and characteristic. Graphs of various types to analyze quality of classifications, training needs, etc.

System would, itself learn to make such classifications and corrections, with feedback from well trained humans.

### 2.2 A Practical Starting Point

A simple prototype, single-user, desktop app. Present statements and classification criteria, and collects user responses per statement. Goal: development of overall interaction style.

### 2.3 A Practical Enhancement

Add user login and record/track responses to each stimuli per user in a local database. Simple graphs and tables showing results.

### 2.4 Next?


---

# 3. Basic Requirements of Prototype

***How will I know when I am done?***

This will be an exceedingly simple initial version:

1. A set of predefined statements as test data.

2. A GUI to present statements, and collect categorization responses.

3. Simple data collection to record responses per statement.

4. Simple table and/or graph to summarize results.


---

# 4. Major Software Components

***What code will I develop?***

Software components may go by many names. We will focus on objects, as in [Object-Oriented Programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming).

## 4.1 Design Pattern: MVC

The most common, and most basic, application software design pattern over the past few decades is known as [Model-view-controller (MVC)](https://en.wikipedia.org/wiki/Model–view–controller).  It goes hand-in-hand with [object oriented programming](https://medium.com/javascript-scene/the-forgotten-history-of-oop-88d71b9b2d9f), and seems to originate with the development of the Smalltalk language in the late 1960s.

### Model: The behaving organism

The "model" encapsulates all of the data and the behavior. It defines the full set of possible interactions with, or actions on, the data. It is generally embodied as a code module (a.k.a., a library, a package). Thus, the primary user user for a model is generally a programmer, and the interface is an [application programming interface (API)](https://en.wikipedia.org/wiki/API).

#### Functional model: as simulation

The model owns, encapsulates, protects, provides access to, all data. The model provides all behaviors that affect the internal state of the model, and which provide services to the "outside world".

The behavior requests are generally referred to as messages, but more commonly as  [methods](https://en.wikipedia.org/wiki/Method_(computer_programming)), which should be viewed as short for "method by which some action is accomplished". We might also consider a method as a form of vital behavior that impacts some particular outcomes.

The model defines:

1. Under what conditions (previous behaviors, request parameters, etc.) a particular behavior can be requested.

2. The effect on the application state/environment if the request succeeds (or does not).

3. The values returned in response to the request, if any.

#### Data model: the proverbial "Dead Man"

Besides behavior, the model includes data, which is the internal state of the organism, its "guts". These guts are part of the functional model, but are frequently externalized as a storage format, such as a [relational database entity-relationship model](https://en.wikipedia.org/wiki/Entity–relationship_model).

The data model only defines a bare outline of the data items in the model, and to some extent, how the data items are related. It does not, and cannot, define behavior. Just be aware that the ***data*** *model* is not ***the*** *model*; it does not include behavior.

That is, the data model is structural; the overall model is functional.

### View-Controller: The User Interface

In our case, the "view-controller" components of the MVC pattern will be combined into a simple [graphical user interface (GUI)](https://en.wikipedia.org/wiki/Graphical_user_interface). This intermixing is pretty standard, unless you are developing the individual "views" and "controllers" (and sometimes even then).

Note that the user interface could take different forms, such as:

1. a [command line (CLI)](https://en.wikipedia.org/wiki/Command-line_interface), 

2. an [application programming interface (API)](https://en.wikipedia.org/wiki/API), or 

3. multiple [graphical user interfaces (GUIs)](https://en.wikipedia.org/wiki/Graphical_user_interface) on a variety of platforms (e.g., iOS, macOS, tvOS, watchOS, MS Windows, Xamarin, browser interfaces). All of these interfaces could be implemented against the same model.

## 4.2 Model Components

***TO BE DONE***

*statements, responses, ...*

## 4.3 View-Controller Components

***TO BE DONE***

*window containing view of current statement, possible categorization choices, controls to make responses and traverse statements; data displays*


---

# 5. Tools

***What software will I use to develop?***

There is a very large number of choices among development tools. I will focus on the ones that I use, and which serve well in a "pro" environment. But the choice of tools is often dictated by an organization, and if not, then is a very personal and idiosyncratic choice.

## Current Phase

This is a very cursory overview of the tools I will use in this current simple prototype. They are also the tools I use the most in any Python project. 

1. ***[PyCharm](https://www.jetbrains.com/pycharm/):*** This is a full featured [integrated development environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment). It includes editors, project management (technical, not business admin), debuggers, and so on. 

	1. As for many such "pro" level tools, it is highly customizable. It makes complex tasks easy (and some would say, vice versa). 
	
	2. PyCharm is on a par with [Apple's Xcode](https://developer.apple.com/xcode/) and [Microsoft's Visual Studio](https://visualstudio.microsoft.com).
	
	3. The free "community version" is very capable. If you do use it on a continual basis, you may find that there are features that require the paid version. The individual license is very reasonable: $89/year. 

2. ***[GitHub](https://github.com/):*** GitHub is an online means of sharing *versioned* project materials. It is one of the many cloud versions of the popular [git source control system](https://git-scm.com). It has features to support parallel work on the code by different team members and even separate teams in a controlled, yet flexible manner.

	1. This is where the materials for this presentation are stored: [Ally-Assist/For-BehaviorAnalystsWhoCode](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode/tree/main/2021_09_25%20Pinpointing%20Behavior%20Statements). If you are reading this online, you are probably already on the GitHub site.
	
	2. Note that this source code repository is a public, open source, space under the Performance Ally, LLC, account. All materials in this repository are licensed under the [Apache License version 2](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode/blob/main/2021_09_25%20Pinpointing%20Behavior%20Statements/LICENSE).
	
	3. You ***CAN*** use command line tools, but I do not. If you have to ask what a command line tool is, then command line tools are probably not well suited to your purposes. Instead, try [GitHub Desktop](https://desktop.github.com). 

3. ***[PyTest](https://docs.pytest.org/):*** PyTest is a testing framework that is integrated into the PyCharm environment. There are other testing tools that could be used with PyCharm, but PyTest is the one that I use. I call it out because the demo, '[7. Demo: Test Driven Design (TDD)](#7-demo-test-driven-design-tdd)', is based on PyTest. Note that most "pro" level development environments will have [some sort of testing framework](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks).

4. ***Others:*** As the project progresses, other Python packages will be pulled in for specific purposes. A rule in Python, and many other languages, is that before designing and writing new code, check to see what is available first. There is a large quantity of high quality free code available through the [Python Package Index (PyPI)](https://pypi.org). PyCharm has [facilities that make adding such packages very very easy](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html) (this is also a typical IDE feature).

## Future Directions

1. ***[SQLAlchemy](https://www.sqlalchemy.org):*** This is a fairly high level Python [Object Relational Mapper (ORM)](https://en.wikipedia.org/wiki/Object–relational_mapping) relational database API that provides access to a variety of relational database products. In addition to providing access to remote database servers, it also works with SQLite for local storage.

2. ***[SQLite](https://www.sqlite.org/index.html):*** Local relational database storage. You use SQLite every time you interact with your mobile devices, desktop computers, almost any web browser, and maybe even your refrigerator. It is used almost universally for local storage of complex (and even not so complex) application data. We would use SQLAlchemy to work with SQLite, but Python has a much lower-level interface built in, also: [sqlite3](https://www.sqlite.org/index.html).

2. ***[Matplotlib](https://matplotlib.org):*** Graphing. [Examples](https://matplotlib.org/stable/gallery/index.html)

3. ***[Pandas](https://pandas.pydata.org/docs/index.html):*** Data analysis tools. If we use Pandas, it will most likely be for its [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) which can read from the SQLite database, and which can be fed to Matplotlib graphing objects.


---

# 6. A Development Process

***TO BE DONE***

***What are the steps in using the tools to develop the major components and verifying that they work and will continue working?***


---

# 7. Demo: Continuous-Feedback Development

***TO BE DONE***

***How will I use the tools to create "provably correct" software?***

I have yet to come up with a satisfactory name for this development technique that really captures its essence from a behavioral point of view.

The traditional name (if such can be said of a term that was recently coined) is [Test Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development). It is a set of decades old practices bundled under a catchy new name, but more importantly, with support for it baked into most software development environments these days. For example, see Pytest in the Tools section of this doc.

The basic idea is: when developing a unit of code, break the overall requirement(s) for the unit into "micro-goals" *(my term)*, and achieve those goals quickly and provably in code. Once the coding is done, keep the "test" for the unit as part of a suite of tests to confirm that functioning of the entire system whenever there is a change or a problem.

## Main Demo

Most of the code will already exist as a Python in the [project repository](https://github.com/Ally-Assist/For-BehaviorAnalystsWhoCode/tree/main/2021_09_25%20Pinpointing%20Behavior%20Statements).

I will leave at least one critical model component, and one view-controller component, unfinished. I will have a set of behavioral requirements for that component that the component must satisfy. As part of demonstrating test driven design, I will incrementally complete the components using the Pytest [unit testing framework](https://en.wikipedia.org/wiki/Unit_testing).

1. At each increment, 

	1. I will set a goal specifying a sub-requirement for the component in the form of a [Python assertion in a test under Pytest](https://docs.pytest.org/en/6.2.x/assert.html). 

	2. The assertion will fail until I produce the code that satisfies that goal.

	3. I will set another goal (i.e., assertion), then engage in software development behaviors that will be reinforced by passing the criterial specified as an assertion.

	4. Rinse repeat until all behavioral application requirements for the component are satisfied.
	
2. The full test suite for the project will be run to find any other problems I introduced during implementation of the component. Any errors must be fixed before we can say that the component is complete.

3. Once the project is error free, the test coverage analyzer will be run.

## Optional

Assuming Ryan Cole is present, Ryan and I may demonstrate "[paired programming](https://martinfowler.com/articles/on-pair-programming.html)", which might better be thought of as cooperative problem solving.

If Ryan is not available, might this be time for "audience participation"?


---

# 8. Where to From Here?

***TO BE DONE***

***Is the end goal still the same? What is the next enhancement toward the goal?***
























# 2021_09_25 Pinpointing: Is It A Behavior?

Subtitle: **A Quick Overview of Professional-Style Software Development in Python**

Material related to a presentation on Sunday 25 September 2021 @ 12:00 to the Slack channel, [Behavior Analysts Who Code](https://www.codingbehavioranalysts.org)

***This will change frequently up to the presentation date***


Tom Donaldson

tom.donaldson@performanceally.com

Created: Sunday 22 August 2021

---

# Overview

During a lengthy [discussion with the Slack channel owner, David Cox](https://behavioranaly-yw87919.slack.com/archives/D02APN949UL), I agreed to do one presentation to the Behavior Analysts Who Code Slack channel on Sunday 25 September 2021 @ 12:00 eastern USA time.

The focus of the presentation, or way or another, will be software development practices wrapped up in a behavior analytic scenario.

The long term goal is to help foster a deeper understanding of software development among behavior analysts to facilitate their own coding as well as make their interactions with professional software development groups more effective. Or something.

### Rationale

David and I discussed options. The basic drivers in developing the presentation will be:

1. Software development skills of the audience are all over the place.

	1. Just starting.
	
	2. Computer science background.
	
	3. Any professional (or retired) software developers? I may be the only one.

2. Given the audience experience with software development, or the lack of it, this first presentation needs to be very general.

3. The "software development project" must be in some way relevant to behavior analysis. 

3. For the project to be intrinsically interesting to me, and to maintain my responding, it should be in some way relevant to my current work. That is, applied behavior analysis in general, or OBM in particular (vs basic experimental or neural nets).

4. After discussion with, and the approval of, Julie Smith, I will use some sort of classification of textual statements as behavioral (or not) as the initial scenario.


### General Format

Each of these topics will be addressed briefly. Goal is to keep it down to about 45 minutes. Step 7, the demo, will be longest.

1. Behavior analytic scenario as the motivation for the project.

2. Overall (basic) development strategy.

3. Basic requirements for the first prototype.

4. Major software components to satisfy the requirements

5. Tools that will be used (including download links) in the initial "simple prototype" phase.

6. Present the development process.

7. Demo with live development project (will have basic framework in place, then do some coding to illustrate one important concept in more detail, e.g., test driven design)

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

3. [Seleting a Pinpoint](https://centralreach.com/how-to-pinpoint-behavior-effectively/).


---

# 2. Development Strategy

***How to break it down into digestible chunks?***


### A Possible End Goal

A system that can be used by large numbers of users evaluating large numbers of statements, marking them as to their behavioral/non-behavioral characteristics. Statistics automatically collected to decide which statements are behavioral in what ways; which statements might be modified to be behavioral, and in what ways. Inter-observer agreements by statement and characteristic. Graphs of various types to analyze quality of classifications, training needs, etc.

System would, itself learn to make such classifications and corrections, with feedback from well trained humans.

### A Practical Starting Point

A simple prototype, single-user, desktop app. Present statements and classification criteria, and collects user responses per statement. Goal: development of overall interaction style.

### A Practical Enhancement

Add user login and record/track responses to each stimuli per user in a local database. Simple graphs and tables showing results.

### Next?


---

# 3. Basic Requirements of Prototype

***How will I know when I am done?***

This will be an exceedingly simple initial version:

1. A set of predefined statements as test data.

2. A GUI to present statements, and collect categorization responses.

3. Simple data collection to record responses per statement.

4. Simple table and/or graph to summarize results.


---

# 4. Major Components (i.e., Objects) in the Software

***What code will I develop?***

## 4.1 Design Pattern: MVC

The most common, and most basic software design pattern over the past few decades is known as [Model-view-controller (MVC)](https://en.wikipedia.org/wiki/Model–view–controller). 

### Model: the Simulation

The "model" encapsulates all of the data and the behavior. It defines the full set of possible interactions with, or actions on, the data. It is generally embodied as a code module (a.k.a., a library, a package). Thus, the primary user user for a model is generally a programmer, and the interface is an [application programmers' interface (API)](https://en.wikipedia.org/wiki/API).

#### It is a model in the sense of "simulation". It is a functional model. The model defines:

1. Under what conditions (previous behavior, request parameters, etc.) a particular behavior can be requested.

2. The effect on the application state/environment if the request succeeds (or does not).

3. The values returned in response to the request, if any.

#### Data model: the proverbial "Dead Man"

In contrast, within the software development environment, you will also hear the phrase "data model", which normally refers to a storage format in a relational database management system. It only defines a bare outline of the data items in the model, and to some extent, how the data items are related. It does not, and cannot, define behavior. That is, the data model is structural; the overall model is functional.


### View-Controller: The User Interface



For our purposes, we will separate out the basic data and the actions permitted on that data into the "model", but we will combine the "view-controller" into a simple [graphical user interface (GUI)](https://en.wikipedia.org/wiki/Graphical_user_interface). 

Note that the user interface could take different forms, such as a command line (CLI), an application programmers' interface (API), or multiple GUIs on a variety of platforms (e.g., iOS, macOS, tvOS, watchOS, MS Windows, Xamarin). All of these interfaces could be implemented against the same model.



---

# 5. Tools

***What software will I use to develop?***

---

# 6. Development Process

***What are the steps in using the tools to develop the major components and verifying that they work and will continue working?***


---

# 7. Demo: Test Driven Design (TDD)

***How will I use the tools to create "provably correct" software?***


---

# 8. Where to From Here?

***Is the end goal still the same? What is the next enhancement toward the goal?***
























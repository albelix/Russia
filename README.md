# Public and Private Goods - Behavioural Experiment

Welcome to the code for this collective risk behavioural experiment. Participants have a budget and can solve a problem by contributing to either a public or private pot. The public pot is cheaper but requires cooperation. If they fail to solve the problem either way, then they lose all their money. If they manage to solve it, they get to keep their unspent funds. 

Participants play in groups of 4. In each group, 2 participants start off with a lower amount of funds than the other 2 participants. In three treatments, the wealth distribution is decided either by a lottery, participants' performance in a mental arithmetic task, or a mix of both. 

# Getting Setup

We recommend that you set the experiment up on your own computer first, then deploy it to heroku or a server of your choice. For heroku, you can either deploy it using the heroku Command Line Interface. Or use oTree hub. 

Let us know if anything is not clear or missing.

## Getting Started - Local

The commands here are all to be run in a terminal window. 

The experiment was built and tested using python 3.9. For best results, please use this same version. 

1. We recommend that you create a virtual environment to run the experiment. Create a vitual environment with python 3.9. We recommend virtualenv-wrapper. If you have virtualenv-wrapper, then you can create a virtual environment with the correct python version by running

	`mkvirtualenv colrisk --python-python3.9`

	Note: This command will only work if you already have virtualenv-wrapper installed (https://virtualenvwrapper.readthedocs.io/en/latest/install.html). Setting up virtual environments is a whole process, and potentially complicated, so unfortunately we cannot give a step by step guide here. It depends on your OS etc.  

	If you have trouble with virtual environments then you can skip this step and just run it in the python environment on your computer. If you run the command `python3 --version` it will tell you the version. Ideally this should be 3.9, but 3.8 or 3.10 should be ok. 

2. Download a copy of this repository. 

	`git clone git@github.com:chasmani/behav_experiment_public_and_private_solutions_to_risk.git`

	Or we might have emailed you a zip.

3. Navigate to the main folder in the terminal, e.g.

	`cd behav_experiment_public_and_private_solutions_to_risk`

4. Install the necessary requirements

	`pip3 install -r requirements.txt`

5. Run a local server on your machine

	`otree devserver`

6. Click on the link shown in terminal, usually it is http://localhost:8000/

7. From there, you can run individual demos of the experiment or the full experiment. 

8. You can create a room with a session for any number of players by clicking on "Rooms" in the navigation bar.


## Getting Started - Running Online on Heroku using the Command Line

Deployment to heroku can be handled using the heroku CLI. This gives the most control but will be tricky if you are not familiar with using the command line and git. In which case, you can skip ahead to the next section to deploy with oTree hub.

To setup, download the heroku CLI, create the heroku git branch and push the changes to heroku. Here are the step by step instructions. Some of this may seem difficult if you are not familiar with the command line, but if you follow the steps then you should get it working:

1. Open a heroku account if you don't already have one. 

2. From the heroku account dashboard click on "New" -> "Create new app". Give it a name e.g. `collective-risk-experiment`. Choose the region closest to you (US or Europe). And then click "Create app".

3. Install the heroku CLI on your computer. Follow the instructions here https://devcenter.heroku.com/articles/heroku-cli (this depends on your Operating System).

4. In a terminal window, run `heroku login`. A browser window should pop up and allow you to login. 

5. In a terminal window, navigate to your project directory. If you downloaded the code by cloning the repo then it will already be a git repository. If you did not then you need to make a git repository by typing the command `git init`. If you get an error message saying that you don't have git then you need to install that (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

6. Update the git repo to include any changes you have made

	`git add -A`
	
	`git commit -m"Latest changes"`

5. Now link the repo to heroku 

	`heroku git:remote -a <your app name you selected at creation e.g. collective-risk-experiment>`

6. Push the code from your computer to heroku

	`git push heroku main` 

(If you get an error saying something along the lines of 'branch main doesn't exist'. Then you can instead try `git push heroku master`. This depends on how you setup your git repository initially).

7. You will need to reset the database. To do this you can run `heroku run "otree resetdb"` from terminal on your local machine. WARNING: THIS STEP WILL ERASE THE ENTRIE DATABASE, MAKE SURE YOU HAVE DOWNLOADED ANY DATA YOU NEED BEFORE RUNNING THIS. 

COMMON ISSUES:

1. It fails and somewhere it says 'Requested runtime .... is not available for this stack (heroku-22)'. You need to open up runtime.txt and then change that to `python-3.9.16`. Save it. Then also add that change to git by running `git add -A` and then `git commit -m"Updated runtime"`. Then try to push the code to heroku again. 

## Getting Started - Running Online on Heroku with oTreeHub

If you are not familar with git and command lines then an easier option is to deploy using oTree hub. This youtube video does a good job of guiding you through step by step:
https://www.youtube.com/watch?v=H8Do08ub8bM

There is a step at about 6:30 where the presenter looks for a zip file. He creates his using pycharm - you don't need that. Instead you can open a terminal, navigate to the main project folder and type `otree zip`. That will create the zip file ready to upload to oTreehub. 

In the video at about 7:30 the Configuration page is a bit out of date. In the Configuration settings, put postgres on standard-0, set OTREE_PRODUCTION to On, set OTREE_AUTH_LEVEL to DEMO, and set Dyno Size to Standard-2x. Do not check the papertrail or sentry boxes. 

Once you have gotten to the end of the video, you should have your app live on heroku. 

In the app, try navigating to "Rooms". It should ask you for a password. You need to create your own password. To do this, login to the heroku dashboard (https://dashboard.heroku.com/). Click on your app, then click on the "Settings" tab, scroll down to "Config Vars" and click on "Reveal Config Vars". Here you need to add a config vars at the bottom by inputting the Key of OTREE_ADMIN_PASSWORD and a Value of the password of your choice. Once you have your password go back to "Rooms" in your app. The username is "admin" and the password should be whatever you just set it to. 

Now you can create a Room with a number of participants. Set the "Session Config" to "Full Experiment" and the Number of participants to a multiple of 4. Congratulations! The experiment is now live. You can test it here and play around with it to familiarise yourself with running rooms, downloading data etc.

## Resources

At heroku you have to pay for resources. We recommend that you use at least:

- Postgres. Standard-0 ($50 per month)
- Dyno. Standard-2x. ($50 per month)

If you followed the setup above with otree hub then these resources will be turned on. They charge you at a pro-rata rate until you turn them off. There is a resources tab in the heroku dashboard for your app. 

Make sure you turn them all off when you finish gathering data (once you have securely downloaded the data of course). 

# How It Works

## Participant Labels

In the current setup, users are prompted for a "participant label" when clicking the link for the app. These need to match participant labels in `"_rooms/participant_labels.txt"`. If you want to set these to e.g. student IDs then change the txt file. Alternatively, we can setup the experiment to run without participant labels, but this will cause 2 participant instances to start if a user opens up two browsers with the link. 

## Grouping

Users are grouped upon arrival in the effort task. Once they have a group, this group persists across apps and rounds (although the group id may change over the apps). 

This wil generally work smoothly but will not work if there are small groups of less than 4 or a player drops out. 

### Not enough players to form a group

On occasion there won't be enough participants to form a group of 4. E.g. if there are 41 participants then there is 1 left over. In this case, the system waits for 20 minutes to try and group the players. After 20 minutes, the player grouping is abandoned. Players are put in their own group of 1, and the participant is given the `participant.is_dropout=True`. This effectively skips the rest of the app by not displaying any pages.

### Dropouts

Players may drop out of a group during the experiment. The rest of the group will continue util they hit a WAitPage at the start of an app. They will then wait there until the WAIT_PAGE_TIME_OUT hits. Once that hits the participants are given the `participant.is_dropout=True`. This effectively skips the rest of the app by not displaying any pages. 

In the main Game app, there is also a wait page while everyone Contributes. The Contribution page therefore has a timeout. If a player doesn't submit a contribution within the timeout then they contribute zero and are set as a dropout. The rest of the group continues without the player. 

In either of the above conditions (group not formed or player dropped out), the final page will display a message to tell the user that there was a problem with the experiment due to waiting too long, and that the experiment was stopped early. 


## Testing

### Automated Testing A

Otree includes some basic testing functionality with bots. The experiment includes tests to check that it all runs smoothly under basic conditions, with bots acting 

You can run this for each of the app with one of these commands

	otree test consent
	otree test effort
	otree test quiz
	otree test game
	otree test payment

This will catch any serious errors with the experiment crashing or not getting to the end under basic bot behaviour. 

Note that this won't work with `otree test full_experiment`. It fails on the effort task. This failure is expected and is not a problem with the app, but is a limitation of the otree browser bots. Specifically, the effort task has a 5 minute timer and this is difficult to incorporate into the otree test bots. 

### Automated Testing B

Otree's browser bots are limited so we also wrote some of your own for testing. These can be found and run in browser_bots.py. There are options for testing on a local machine and heroku.  And you can test for dropouts etc.


### Manual Testing

Before running an experiment, we recommend testing some edge cases manually. The test criteria is whether the experience is what we want for the participants, that the game outcome is correct and that data is recorded properly. The tests can be checked by simply playing through and checking it all makes sense, and checking the data under the Export tab on otree. 

Things to test include:

1. Having one player drop out from a group. Is that handled gracefully for other participants?
2. Having multiple players drop out from a group. 
3. Session with multiple groups. Are the groups consistent across rounds? Especially check what happens if groups arrive at apps at different times, and with players in combinations of orders within and between groups. Also check that the individual group data is not being influenced by players outside of the group. 
4. Sessions with as many participants as the experiment will have. More participants require more resources, which may be adjusted on heroku (database, memory, processor etc). More participants also may increase chances of bugs due to request scheduling on the server, if lots of requests are being received together. Do these bugs arise and if so are they handled gracefully? 

The app is fully tested and we don't expect there to be issues but inevitably as code is passed around and small cahnges are made there is the possibility of bugs. And there may be differences in operating environments. 

### Translation

There are 3 different types of text to translate.

1. Text that is a part of Otree's core functionality. E.g. Waiting time messages

Change the LANGAUGE_CODE in settings.py
 e.g. `LANGUAGE_CODE = 'fr'`

2. Bits of text that are in python code e.g. the text for questions in forms

Translate by making a copy of "lexicon_en.py" and naming it in your language. 

Add to the "if" statement at the top of all the __init__.py files for each app to load in the correct lexicon file. 

3. Templates

To translate text in templates, create an "if" statement to check for the LANGUAGE_CODE. Rewrite the main content block below that. See the consent app tempaltes for examples of how to do it. 






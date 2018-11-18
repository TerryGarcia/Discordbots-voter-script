# Discordbots voter script
## What is this?
This repository contains a script that can be run which will essentially vote for any bot on discordbots.org. This can be useful because there are bots on discordbots.org which will give certain benefits to users for voting for that bot on discordbots.org. It is because of this that a user can set up some sort of process which allows for a computer to vote for them automatically after some specified amount of time indefinitely. This is exactly what I have used this script for a certain discord bot so that I may receive a card every 12hrs without any interaction from me.

## Requirements
* Python 3
* Download the Selenium and ConfigParser packages from pip
  * You can use the following commands:
    * `pip install ConfigParser`
    * `pip install selenium`
* Chrome
* Have already logged into discord from the chrome profile you will provide to the script.
  * The script uses a chrome profile specified by you.
  * To know if you have met this requirement, go to this page <https://discordapp.com/channels/@me> using the chrome profile you are going to provide to the script and if you don't see a prompt for you to log in and you are able to access your PMs and channels, you are good to go for this requirement.

## How do I use it?
First, I would like to say that I will use this section to show you how to set up the script so that you can run it and it votes for whatever bot specified. How to automate this, I will show how I do it in a later section.

1. Download the repository and unzip the contents in whatever directory you like.
2. In that directory, there should be a file called `config.txt`. Open it in your favorite text editor.
3. For the variable `profile_folder_path`, set it equal to the path to the chrome profile you want the script to use.
  * You can find the path by going to `chrome://version/` using the chrome profile you want to use.
4. Next, you want to set the variable `bot_id` in the file to the id of the bot you want the script to vote for.
  * You can find this id by going to the voting page for the bot, clicking on "vote", and when you see the button "Vote for this bot", look at the URL of the page. The long chain of numbers surrounded by "/" is the bot's id.
    * Example: The id for a bot with the URL "https://discordbots.org/bot/365975655608745985/vote" is "365975655608745985"
5. Now, you should be done. You can run the script and it should vote for whatever bot specified.

## How I automate the script
Here, I will explain how I have the script run automatically.

First, this method isn't perfect. The method results in a noticeable time drift (like ~3 mins usually). This means that if my script is supposed to run every 12hrs, and it finishes a run at 12:34 pm then if perfect, it should run at 12:34 am but, because of there is the time drift, it actually runs at 12:37 am. This results in a loss of time in terms of efficiency. Some people might not really care about this though, I know I don't really care.

Before I start explaining, if anything here is unclear, Google is your friend. If you still cannot figure out your problem, make an issue on the repository or email me at "davina_the_arena@protonmail.com"; I'll answer if I have time to. Anyways, I'll start. I have a small laptop, which is running Windows 7, that I leave plugged in and running 24/7. On the laptop, I have windows set up so that when the laptop is turned on, it boots into windows and windows will just automatically log in to the only windows account on the computer. It does so without even asking for a password. By the way, if you are going to do this, make sure the laptop is in a physically safe location or it has no sensitive information vulnerable to attackers with physical access to the laptop otherwise, you are risking that sensitive information from being exposed. In most cases, this is overly dramatic, but I say so just to be a responsible software developer notifying you of potential risks to my software. Oh yeah, be careful not to get banned by discord or by the bot developers. I have not seen examples of this happening but I don't see why that couldn't happen. Anyways, Windows 7 has this thing called "Task Scheduler" which can set tasks for windows to do according to specified triggers. I have a task set up that I will describe, not all that I describe (I think) is necessary to accomplish the intended goal here; You can experiment if you like. I have the task run only when the user is logged on and run with highest privileges as well as being triggered at logon of any user. After being triggered, the task is repeated every 12hrs and 3mins. The 3 mins is due to how I have seen the Task Scheduler begin its timer for when running the next task when the previous task began its run. Ex: Task runs at 12:00 pm and finishes at 12:03 pm. The next task runs at 12:00 am when it should run at 12:03 am because DiscordBots got the vote at 12:03 pm, not 12:00 pm so 12hrs later after the vote when it should run, would be 12:03 am. So, the 3mins is so that it doesn't run too early. Okay, next, for the action, I tell it to run a program with a path pointing to the .bat file I created (and included in the repo) which just runs the script. Why did I do this? I don't remember but, I think it was due to the menu not wanting to accept the command in the .bat file itself. I have the task restart every minute up to 3 times if the task fails. And for safety, I have the Task Scheduler stop the task if it runs for longer than 1hr for some reason. That is basically it, after that, I just let the laptop keep running and if it restarts for some reason (windows updates, probably) then it will recover, although some time will probably be lost.

# Discordbots voter script
## What is this?
This repository contains a script that can be run which will essentially vote for any bot on discordbots.org. This can be useful because there are bots on discordbots.org which will give certain benefits to users for voting for that bot on discordbots.org. It is because of this that a user can set up some sort of process which allows for a computer to vote for them automatically after some specified amount of time indefinitely. This is exactly what I have used this script for for a certain discord bot so that I may recieve a card every 12hrs without any interaction from me.

## Requirements
* Python 3
* Download the selenium and configparser packages from pip
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

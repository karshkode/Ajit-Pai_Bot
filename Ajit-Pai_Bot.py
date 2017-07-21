version="0.24"

import pdb
import os
import subprocess as sp
import configparser
from subprocess import call
import importlib
import praw # Reddit

# Bot stuff
import updateable
import redditBot

# Entry point
#-------------------------------------------------------------------------------------------------------

while True:

	# Setup the reddit bot
	bot = redditBot.redditBot()

	# Setup the bot feedback interface
	os.system('cls')
	sp.call('clear',shell=True)
	print('logged in as: ', reddit.user.me(), '\n')

	# Main program
	while True:

		# Run a redditBot cycle
		bot.runCycle()

		# Check for paibot updates
		try:
			for message in reddit.inbox.messages(limit=10):
				if message.author.name in paibot.admins and "UPDATE" in message.body:
					print("Recieved update command from " + message.author.name + "...")
					try:
						print("Pulling repository...")
						call("git pull")
						importlib.reload(updateable)
						#message.reply("Successfully updated!")
						print("Successfully updated!")
					except Exception as e:
						#message.reply("Error updating!")
						print("Error updating!")
						print(e)
					break

		except Exception as e:
			print("---------------------------------\n")
			print("An exception was thrown while updating")
			print(e)
			print("---------------------------------\n")
			time.sleep(30)

print("Something went horribly wrong.")
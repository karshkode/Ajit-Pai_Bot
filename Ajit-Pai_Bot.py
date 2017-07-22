version="0.26"

import pdb
import os
import time
import subprocess as sp
from subprocess import call
import importlib

# Bot stuff
import updateable
import redditBot
import CnC

# Entry point
#-------------------------------------------------------------------------------------------------------

while True:

	# Setup the reddit bot
	bot = redditBot.redditBot()
	c2 = CnC.CnC(bot.reddit)
	updated = False

	# Setup the bot feedback interface
	os.system('cls')
	sp.call('clear',shell=True)

	# Main program
	while updated == False:

		# Run a redditBot cycle
		bot.runCycle()

		# Check for updates
		updated = c2.cnc()

	importlib.reload(updateable)
	importlib.reload(CnC)

print("Something went horribly wrong.")
version="0.28"

import pdb
import os
import time
import subprocess as sp
from subprocess import call
import importlib
import threading

# Bot stuff
import updateable
import redditBot
import CnC

class bot_thread(threading.Thread):
	def __init__(self, threadID):
		self.bot_id = threadID

	def run(self):
		while True:

			# Setup the reddit bot
			bot = redditBot.redditBot(self.bot_id)
			c2 = CnC.CnC(bot)
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

			print("Updated, restarting...")
			importlib.reload(updateable)
			importlib.reload(CnC)

		print("Something went horribly wrong in thread " + self.bot_id)

# Entry point
#-------------------------------------------------------------------------------------------------------

configFile = configparser.ConfigParser()
configFile.read('praw.ini')
num_threads = configFile['threading']['num_threads']

for i in xrange(1,num_threads):
	thread = bot_thread(i)
	thread.start()

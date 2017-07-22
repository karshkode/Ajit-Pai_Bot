import time
import configparser
import praw # Reddit
import git

class CnC:

	def __init__(self, reddit):

		self.reddit = reddit

		configFile = configparser.ConfigParser()
		configFile.read('praw.ini')
		self.c2 = configFile['admins']['c2']
		self.admins = configFile['admins']['admin'].split(",")
		self.botnum = configFile['admins']['botnum']
		self.gitDir = configFile['admins']['gitdir']

		return

	def __del__(self):
		return

	def parseCommands(self, commands, submission):
		commands = commands.splitlines()
		for command in commands:
			if str.lower("all") in command or self.botnum in command:
				if str.lower("update") in command:
					g = git.cmd.Git(self.gitDir)
					g.pull()
					self.reddit.reply(self.botnum + ": Affirm, updating")
					return True

				if str.lower("ping") in command:
					self.reddit.reply(self.botnum + ": Pong")

				with open('cncLog.txt', 'w') as log:
					log.write(str(submission.id))

		return False

	def cnc(self):
		try:
			for submission in self.reddit.subreddit(self.c2).new(limit=1):
				if submission.author in self.admins and submission.id not in open('cncLog.txt', 'r').read():
					if self.parseCommands(submission.body, submission) == True:
						return True
					else:
						return False
				else:
					return False
		except Exception as e:
			print("CnC failure")
			print(e)
			return False
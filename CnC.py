import time
import configparser
import praw # Reddit
import git

class CnC:

	def __init__(reddit):

		self.reddit = reddit

		configFile = configparser.ConfigParser()
		configFile.read('praw.ini')
		self.c2 = configFile['admins']['c2']
		self.admins = configFile['admins']['admin'].split(",")
		self.botnum = configFile['admins']['botnum']
		self.gitDir = configFile['admins']['gitdir']

		return

	def __del__():
		return

	parseCommands(self, commands):
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
					log.write(str(comment.id))

		return False

	cnc():
		try:
			for submission in reddit.subreddit(c2).new(limit=1):
				if submission.author in self.admins and submission.id not in open('cncLog.txt', 'r').read():
					if parseCommands(submission.body): == True:
						return True
					else:
						return False
				else:
					return False
		except Exception as e:
			print("CnC failure")
			print(e)
			return False
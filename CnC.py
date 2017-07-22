import configparser
import git

class CnC:

	def __init__(self, reddit):

		self.reddit = reddit

		configFile = configparser.ConfigParser()
		configFile.read('praw.ini')
		self.c2 = configFile['admins']['c2']
		self.admins = configFile['admins']['admin'].split(",")
		self.botname = configFile['admins']['botname']

		return

	def __del__(self):
		return

	def parseCommands(self, commands, submission):
		commands = commands.splitlines()
		restart = False
		for command in commands:
			if str.lower("all") in command or self.botname in command:
				if str.lower("update") in command:
					g = git.cmd.Git()
					g.pull()
					submission.reply(self.botname + ": Affirm, updating")
					restart = True

				if str.lower("ping") in command:
					submission.reply(self.botname + ": Pong")

				with open('cncLog.txt', 'w') as log:
					log.write(str(submission.id))

		if restart == True:
			return True

		return False

	def cnc(self):
		try:
			for submission in self.reddit.subreddit(self.c2).new(limit=1):
				if submission.author in self.admins and submission.id not in open('cncLog.txt', 'r').read():
					if self.parseCommands(submission.selftext, submission) == True:
						return True
					else:
						return False
				else:
					return False
		except Exception as e:
			print("CnC failure")
			print(e)
			return False
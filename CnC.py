import configparser
import git

class CnC:

	def __init__(self, bot):

		self.reddit = bot.reddit

		configFile = configparser.ConfigParser()
		configFile.read('praw.ini')
		self.c2 = configFile['admins']['c2']
		self.admins = configFile['admins']['admin'].split(",")
		self.bot = bot

		return

	def __del__(self):
		return

	def parseCommands(self, commands, submission):
		commands = commands.splitlines()
		restart = False
		for command in commands:
			if str.lower("all") in command or self.bot.id in command:
				if str.lower(" update ") in command:
					g = git.cmd.Git()
					g.pull()
					submission.reply(self.bot.id + " - Affirm, updating")
					restart = True

				if str.lower(" subreddit-add ") in command:
					cmd = command.split()
					success = 0
					subreddit = ""
					for i in xrange(0, cmd.length-1):
						if tmp[i] == "subreddit-add":
							subreddit = cmd[i+1]
							add = self.bot.paibot.add_subreddit(subreddit)
							if add:
								success = 1
							else:
								success = -1
							break
					if success == -1:
						submission.reply(self.bot.id + "- WARNING: Subreddit already included")
					elif success == 0:
						submission.reply(self.bot.id + " - ERROR: Unable to identify subreddit")
					else:
						submission.reply(self.bot + " - SUCCESS: " + subreddit + " added")

				if str.lower(" subreddit-remove ") in command:
					cmd = command.split()
					success = 0
					subreddit = ""
					for i in xrange(0, cmd.length-1):
						if tmp[i] == "subreddit-remove":
							subreddit = cmd[i+1]
							remove = self.bot.paibot.remove_subreddit(subreddit)
							if remove:
								success = 1
							else:
								success = -1
							break
					if success == -1:
						submission.reply(self.bot.id + "- WARNING: Subreddit already not included")
					elif success == 0:
						submission.reply(self.bot.id + " - ERROR: Unable to identify subreddit")
					else:
						submission.reply(self.bot + " - SUCCESS: " + subreddit + " removed")


				if str.lower(" ping ") in command:
					submission.reply(self.bot.id + " - Pong")

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

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
		self.subList = configFile['admins']['subreddits']

		return

	def __del__(self):
		return

	def parseCommands(self, commands, submission):
		commands = commands.splitlines()
		restart = False
		for command in commands:
			command = command.split(" ")
			if str.lower("all") in command[0] or self.botname in command[0]:
				if str.lower("update") in command[1]:
					g = git.cmd.Git()
					g.pull()
					submission.reply(self.botname + " - Affirm, updating")
					restart = True

				if str.lower("edit") in command[1]:
					configFile = configparser.ConfigParser()
					configFile.read('praw.ini')
					try:
						configFile.set(command[2], command[3], command[4])
						with open('praw.ini', 'wb') as cfg:
							configFile.write(cfg)
							submission.reply(self.botname + " - Affirm editing " + command[2])
						restart = True
					except Exception as e:
						submission.reply(self.botname + " - Instructions unclear, dick stuck in ceiling fan")
						print(e)

				if str.lower("add") in command[1]:
					configFile = configparser.ConfigParser()
					configFile.read('praw.ini')
					existingVar = configFile[command[2]][command[3]]
					try:
						configFile.set(command[2], command[3], existingVar + "," + command[4])
						with open('praw.ini', 'wb') as cfg:
							configFile.write(cfg)
							submission.reply(self.botname + " - Affirm, adding " + command[4])
						restart = True
					except Exception as e:
						submission.reply(self.botname + " - Instructions unclear, dick stuck in ceiling fan")
						print(e)

				if str.lower("remove") in command[1]:
					configFile = configparser.ConfigParser()
					configFile.read('praw.ini')
					existingVar = configFile[command[2]][command[3]]
					if ("," + command[3]) in existingVar:
						existingVar = "," + existingVar
					elif (command[3] + ",") in existingVar:
						existingVar = existingVar + ","
					existingVar = existingVar.replace(command[3], "")
					try:
						configFile.set(command[2], command[3], existingVar)
						with open('praw.ini', 'wb') as cfg:
							configFile.write(cfg)
							submission.reply(self.botname + " - Affirm, removing " + command[4])
						restart = True
					except Exception as e:
						submission.reply(self.botname + " - Instructions unclear, dick stuck in ceiling fan")
						print(e)

				if str.lower("status") in command[1]:
					submission.reply(self.botname + " - Alive\n\n" + self.subList)

				if str.lower("die") in command[1]:
					submission.reply(self.botname + " - Shutdown")
					exit()

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

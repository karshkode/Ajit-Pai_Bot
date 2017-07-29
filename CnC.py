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
			try:				
				command = command.split(" ")
				if str.lower("all") in command[0] or self.botname in command[0]:

					file = ""
					if "praw" in command[2]:
						file = "praw.ini"
					elif "config" in command[2]:
						file = "config.cfg"

					if str.lower("update") in command[1]:
						g = git.cmd.Git()
						g.pull()
						submission.reply(self.botname + " - Affirm, updating")
						restart = True

					if str.lower("edit") in command[1]:
						configFile = configparser.ConfigParser()
						configFile.read(file)
						configFile.set(command[3], command[4], command[5])
						with open(file, 'w') as cfg:
							configFile.write(cfg)
						submission.reply(self.botname + " - Affirm editing " + command[4])
						restart = True

					if str.lower("add") in command[1]:
						configFile = configparser.ConfigParser()
						configFile.read(file)
						existingVar = configFile[command[3]][command[4]]
						configFile.set(command[3], command[4], existingVar + "," + command[5])
						with open(file, 'w') as cfg:
							configFile.write(cfg)
						submission.reply(self.botname + " - Affirm, adding " + command[5])
						restart = True

					if str.lower("remove") in command[1]:
						configFile = configparser.ConfigParser()
						configFile.read(file)
						existingVar = configFile[command[3]][command[4]]
						replaceable = True

						if ("," + command[5]) in existingVar:
							replaceStr = "," + command[5]
						elif (command[5] + ",") in existingVar:
							replaceStr = command[5] + ","
						else:
							replaceable = False

						if replaceable == True:
							existingVar = existingVar.replace(replaceStr, "")
							configFile.set(command[3], command[4], existingVar)
							with open(file, 'w') as cfg:
								configFile.write(cfg)
							submission.reply(self.botname + " - Affirm, removing " + command[5])
							restart = True
						else:
							submission.reply(self.botname + " - Error, " + command[5] + " not found")

					if str.lower("status") in command[1]:
						submission.reply(self.botname + " - Alive\n\n" + self.subList)

					if str.lower("die") in command[1]:
						submission.reply(self.botname + " - Shutdown")
						exit()

					with open('cncLog.txt', 'w') as log:
						log.write(str(submission.id))

				except Exception as e:
					submission.reply(self.botname + " - Instructions unclear, dick stuck in ceiling fan")
					print(e)

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

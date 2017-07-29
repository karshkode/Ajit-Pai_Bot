import configparser
import git

class CnC:

	def __init__(self, reddit):

		self.reddit = reddit

		configFile = configparser.ConfigParser()
		configFile.read('praw.ini')
		self.c2 = configFile['admins']['c2']
		self.status = configFile['admins']['status']
		self.admins = configFile['admins']['admin'].split(",")
		self.botname = configFile['admins']['botname']
		self.subList = configFile['admins']['subreddits']
		self.backupc2 = configFile['admins']['backupc2']

		return

	def __del__(self):
		return

	def parseCommands(self, commands, submission):
		commands = commands.splitlines()
		restart = False
		for command in commands:
			try:				
				command = command.split(" ")
				replyStr = ""
				if str.lower("all") in command[0] or self.botname in command[0]:

					file = ""
					if "praw" in command[2]:
						file = "praw.ini"
					elif "config" in command[2]:
						file = "config.cfg"

					if str.lower("update") in command[1]:
						g = git.cmd.Git()
						g.pull()
						replyStr += (self.botname + " - Affirm, updating" + "\n\n")
						restart = True

					elif str.lower("edit") in command[1]:
						configFile = configparser.ConfigParser()
						configFile.read(file)
						configFile.set(command[3], command[4], command[5])
						with open(file, 'w') as cfg:
							configFile.write(cfg)
						replyStr += (self.botname + " - Affirm editing " + command[4] + "\n\n")
						restart = True

					elif str.lower("add") in command[1]:
						configFile = configparser.ConfigParser()
						configFile.read(file)
						existingVar = configFile[command[3]][command[4]]
						configFile.set(command[3], command[4], existingVar + "," + command[5])
						with open(file, 'w') as cfg:
							configFile.write(cfg)
						replyStr += (self.botname + " - Affirm, adding " + command[5] + "\n\n")
						restart = True

					elif str.lower("remove") in command[1]:
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
							replyStr += (self.botname + " - Affirm, removing " + command[5] + "\n\n")
							restart = True
						else:
							replyStr += (self.botname + " - Error, " + command[5] + " not found" + "\n\n")

					elif str.lower("status") in command[1]:
						replyStr += (self.botname + " - " + self.status + "\n" + self.subList + "\n\n")

					elif str.lower("idle") in command[1]:
						configFile.set('status', 'idle')
						with open(file, 'w') as cfg:
							configFile.write(cfg)
						replyStr += (self.botname + " - Affirm, idling "+ "\n\n")

					elif str.lower("resume") in command[1]:
						configFile.set('status', 'alive')
						with open(file, 'w') as cfg:
							configFile.write(cfg)
						replyStr += (self.botname + " - Affirm, idling "+ "\n\n")

					elif str.lower("die") in command[1]:
						replyStr += (self.botname + " - Shutdown"  + "\n\n")
						exit()

				if submission != None:
					with open('cncLog.txt', 'w') as log:
						log.write(str(submission.id))
					submission.reply(replyStr)

			except Exception as e:
				if submission != None:
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

			try:
				headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
				self.parseCommands(requests.get(self.backupc2, headers=headers).content, None)
			except Exception as e:
				print("Total CnC Failure")
				print(e)
			return False
import pdb
import re
import os
import subprocess as sp
import datetime
import time
import random
import re
import configparser
import random
import _thread

from subprocess import call

import importlib
import updateable

import praw # Reddit

class redditBot:

	# Constructor
	def __init__(self):
		
		# Create the reddit instance
		self.reddit = praw.Reddit('bot1')

		# Setup the bot feedback interface
		os.system('cls')
		sp.call('clear',shell=True)
		print('logged in as: ', self.reddit.user.me(), '\n')

		# Setup the bot
		random.seed(a=None)
		configFile = configparser.ConfigParser()
		configFile.read('praw.ini')
		subList = configFile['admins']['subreddits']
		threadList = configFile['admins']['threads']
		threadSubsList = configFile['admins']['threadsubs']
		self.status = configFile['admins']['status']
		self.xPost = configFile['admins']['xpost']
		self.subreddits = subList.split(",")
		self.threads = threadList.split(",")
		self.threadSubs = threadSubsList.split(",")
		bottype = configFile['admins']['bottype']
		self.paibot = updateable.updateable(bottype)

		return
		
	# Destructor
	def __del__(self):
		return

	# Parse content text and decide to act upon it
	def parseText(self, comment, body, post):
		"Parses the text of a comment and decides"

		#############################################
		# Parse for potential content to reply to 	#
		#############################################
		try:

			# AMA mode
			if "ama" in self.status:
				if any(keyString in str.lower(body) for keyString in self.paibot.questionKeyStrings):
					reply = self.generateReply(self.paibot.answer)
					self.replyContent(comment, reply)

			# Comment is related to net neutrality
			elif any(keyString in str.lower(body) for keyString in self.paibot.netNeutralityKeyStrings):

				# Pro net neutrality scan
				proNN = 0
				for word in self.paibot.proNetNeutralityStrings:
					if word in str.lower(body):
						proNN += 1

				# Anti net neutrality scan
				antiNN = 0
				for word in self.paibot.antiNetNeutralityStrings:
					if word in str.lower(body):
						antiNN += 1

				reply = ""

				# Pro net neutrality comment
				if proNN >= antiNN:
					reply = self.generateReply(self.paibot.negative)
					if random.randint(1,10) == 5:
						reply += "YOU JUST GOT PIED."

				# Anti net neutrality comment
				else:
					reply = self.generateReply(self.paibot.positive)

				self.replyContent(comment, reply)

		except Exception as e:
			print(e)

		return True

	def generateReply(self, reply_array):
		reply = ""
		if random.randint(1,20) == 17:
			reply = random.choice(reply_array[-1])
			return self.parsePhrase(reply, reply_array)
		for branch in reply_array[2:]:
			phrase = random.choice(branch)
			reply += self.parsePhrase(phrase, reply_array)
		return reply

	def parsePhrase(self, phrase, reply_array):
		parsed_phrase = ""
		if "[ADJECTIVE]" in phrase:
			words = phrase.split("[ADJECTIVE]")
			parsed_phrase += words[0] + " "
			for word in words[1:]:
				parsed_phrase += random.choice(reply_array[0]) + " "
				parsed_phrase += word + " "
		elif "[ADVERB]" in phrase:
			words = phrase.split("[ADVERB]")
			parsed_phrase += words[0] + " "
			for word in words[1:]:
				parsed_phrase += random.choice(reply_array[1]) + " "
				parsed_phrase += word + " "
		else:
			parsed_phrase = phrase + " "
		return parsed_phrase


	# Bot operation functions
	#-------------------------------------------------------------------------------------------------------

	# Throw an exception to the subreddit
	def throwException(self, title, string):
		"Throws an exception to the subreddit as a self post"
		subreddit.submit("Exception: " + title, selftext=string, resubmit=False, send_replies=False)
		return "Exception"

	# Reply to content function
	def replyContent(self, comment, text):
		"Replys to content"

		if str(comment.id) in open("replyLog.txt", "r").read():
			return
		else:
			text = text[:-1]
			rText = ""
			if text[-1] == '~':
				rText = text[:-1] + "\n\n> I am a parody bot. Feel free to block me."
			else:
				rText = text + "\n\nAjit Pai - Chairman FCC;  ajit.pai@fcc.gov;  (1) 202-418-2000\n\n> I am a parody bot. Feel free to block me."
			with open('replyLog.txt', 'a') as replyLog:
				comment.reply(rText)
				try:
					print("Replying to comment: " + comment.body + "\n", text)
				except Exception:
					print("Replying to post: " + comment.title + "\n", text)
				replyLog = open("replyLog.txt", "a")
				replyLog.write(str(comment.id))
				replyLog.write("\n")
				replyLog.close()
				self.truncateLogFile("replyLog.txt")
		return

	# Reports content for review
	def reportContent(self, comment, reasons):
		"Reports content for the moderation queue"
		if str(comment.id) in open("reportLog.txt", "r").read():
			return
		else:
			reasonstring = "|| "
			for reason in reasons:
				reasonstring = reasonstring + reason + " || "

			with open('reportLog.txt', 'a') as reportLog:
				comment.report(reasonstring)
				print("| Reporting comment: ", comment.id, " for ", reasonstring)
				reportLog = open("reportLog.txt", "a")
				reportLog.write(str(comment.id))
				reportLog.write("\n")
				reportLog.close()
				self.truncateLogFile("reportLog.txt")
		return

	# Check if content is in a hostile tone
	def hostileCheck(self, body):
		"Checks for hostility in content body"
		upperCount = 0
		for word in body.split():
			if len(word) > 2:
				if word.isupper() == True:
					upperCount += 1
		if upperCount >= 3:
			return True
		return False


	# Truncate the log file so the bot doesn't eat itself digging through 9000 lines of logs
	def truncateLogFile(self, logFile):
		"Trucates the input log file"
		FILELEN = 100

		with open(logFile) as f:
			for i, l in enumerate(f):
				pass
			lineCount = i + 1

		while lineCount > FILELEN:
			with open(logFile, 'r') as fin:
				data = fin.read().splitlines(True)
			with open(logFile, 'w') as fout:
				fout.writelines(data[1:])
			lineCount -= 1
		return

	# X-Post thread
	def thread_xpost(self, threadURLs):

		cfg = configparser.ConfigParser()
		cfg.read("config.cfg")
		threadTitle = cfg['thread']['xtitle']
		# threadSelfText = cfg['thread']['xselftext']
		# threadSelfText.replace("\\n\\n", "\n\n")
		# urlText = ""
		# for url in threadURLs:
		# 	if len(urlText) <= 1:
		# 		urlText = url
		# 	else:
		# 		urlText = urlText + ", " + url
		# threadSelfText.replace("[URL]", urlText)

		print("Launched X-Post code thread")

		for subredditName in self.subreddits:
			time.sleep(720) # 12 minutes
			subreddit = self.reddit.subreddit(subredditName)
			thread = subreddit.submit(threadTitle, url=threadURLs[0], resubmit=True, send_replies=False)
			threadURL = "https://www.reddit.com" + thread.permalink
			print("X-Posted new thread: " + threadTitle + " -> " + threadURL)

		return

	# Main function
	def runCycle(self):

		print('\n')
		print("------------New Cycle------------\n")

		if "idle" in self.status:
			print("idle\n")
			time.sleep(30)
			return

		# Self post and store link in var for AMA.
		if "startthread" in self.status:
			try:
				cfg = configparser.ConfigParser()
				cfg.read("config.cfg")
				threadTitle = cfg['thread']['title']
				threadSelfText = cfg['thread']['selftext']
				threadSelfText.replace("\\n\\n", "\n\n")
				listOfThreads = ""

				for subredditName in self.threadSubs:
					subreddit = self.reddit.subreddit(subredditName)

					thread = subreddit.submit(threadTitle, selftext=threadSelfText, resubmit=True, send_replies=False)
					threadURL = "https://www.reddit.com" + thread.permalink
					print("Posted new thread: " + threadTitle + " -> " + threadURL)
					if len(listOfThreads) == 0:
						listOfThreads += threadURL
					else:
						listOfThreads = listOfThreads + "," + threadURL

				configFile = configparser.ConfigParser()
				configFile.read("praw.ini")
				configFile.set('admins', 'status', 'ama')
				configFile.set('admins', 'threads', listOfThreads)
				
				with open("praw.ini", 'w') as file:
					configFile.write(file)
				
				self.status = "ama"
				self.threads = listOfThreads.split(",")
				
				if self.xPost == "true":
					_thread.start_new_thread(self.thread_xpost, (self.threads,))
				
				print("\nEntered status ama")
			except Exception as e:
				print(e)

		if "ama" in self.status:
			try:
				for submission in self.threads:
					submission = self.reddit.submission(url=submission)

					# Parse thread comments
					try:
						for comment in submission.comments:
							if comment.author is not None and comment.author != self.reddit.user.me():
								self.parseText(comment, comment.body, False)
					except Exception as e:
						print(e)
			except Exception as e:
				print(e)

		else:
			try:
				# Cycle through subreddits
				for subredditName in self.subreddits:
					subreddit = self.reddit.subreddit(subredditName)

					# Parse subreddit comments
					try:
						for comment in subreddit.comments(limit=100):
							if comment.author is not None and comment.author != self.reddit.user.me():
								self.parseText(comment, comment.body, False)
					except Exception as e:
						print(e)

					# Parse submisssions
					try:
						for submission in subreddit.new(limit=10):

							# Ignore stickied posts
							if submission.stickied == True:
								continue

							if submission.author is not None and submission.author != self.reddit.user.me():
								self.parseText(submission, submission.title, True)
								if submission.domain.split(".")[0] is not "self":
									self.parseText(submission, submission.url, True)
								elif submission.body is not None:
									self.parseText(submission, submission.body, True)
					except Exception as e:
						pass

			except Exception as e:
				print("An exception was thrown, trying again in 30 seconds")
				print(e)
				time.sleep(30)

		return
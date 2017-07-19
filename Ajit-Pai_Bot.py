version="0.23"

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

from subprocess import call

import importlib
import updateable


import praw # Reddit

# Parse content text and decide to act upon it
def parseText(comment, body, post):
	"Parses the text of a comment and decides"

	#################
	# Kill switch 	#
	#################
	try:
		if comment.parent().author == reddit.user.me() and "ModBotCode:" in body:
			killcfg = configparser.ConfigParser()
			killcfg.read('praw.ini')
			killcode = killcfg['bot1']['killcode']

			if body == "ModBotCode:" + killcode and comment.author in killcfg['admins']['admin']:
				replyContent(comment, "Copy that, I'm super broken! --> Terminating!!!")
				return False
	except Exception:
		pass

	#############################################
	# Parse for potential content to reply to 	#
	#############################################
	try:

		# Comment is related to net neutrality
		if any(keyString in str.lower(body) for keyString in paibot.netNeutralityKeyStrings):

			print("valid comment found")

			# Pro net neutrality scan
			proNN = 0
			for word in paibot.proNetNeutralityStrings:
				if word in str.lower(body):
					proNN += 1

			# Anti net neutrality scan
			antiNN = 0
			for word in paibot.antiNetNeutralityStrings:
				if word in str.lower(body):
					antiNN += 1

			reply = ""

			# Pro net neutrality comment
			if proNN >= antiNN:
				print("pro nn comment")
				reply = generateReply(paibot.negative)
				if random.randint(1,10) == 5:
					reply += "YOU JUST GOT PIED."

			# Anti net neutrality comment
			else:
				print("anti nn comment")
				reply = generateReply(paibot.positive)

			replyContent(comment, reply)

	except Exception:
		pass

	return True

def generateReply(reply_array):
	reply = ""
	if randint(1,20) == 17:
		reply = random.choice(reply_array[-1])
		return parsePhrase(reply, reply_array)
	for branch in reply_array[2:]:
		phrase = random.choice(branch)
		reply += parsePhrase(phrase, reply_array)
	return reply

def parsePhrase(phrase, reply_array):
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
def throwException(title, string):
	"Throws an exception to the subreddit as a self post"
	subreddit.submit("Exception: " + title, selftext=string, resubmit=False, send_replies=False)
	return "Exception"

# Reply to content function
def replyContent(comment, text):
	"Replys to content"
	if str(comment.id) in open("replyLog.txt", "r").read():
		return
	else:
		text = text[:-1]
		rText = ""
		if text[-1] == '~':
			rText = text[:-1] + "\n\n> I am a parody bot. Feel free to block me, or [PM me](https://www.reddit.com/message/compose/?to=Ajit-Pai) to add your subreddit to my blacklist."
		else:
			rText = text + "\n\nAjit Pai - Chairman FCC;  ajit.pai@fcc.gov;  (1) 202-418-2000\n\n> I am a parody bot. Feel free to block me, or [PM me](https://www.reddit.com/message/compose/?to=Ajit-Pai) to add your subreddit to my blacklist."
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
			truncateLogFile("replyLog.txt")
	return

# Reports content for review
def reportContent(comment, reasons):
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
			truncateLogFile("reportLog.txt")
	return

# Check if content is in a hostile tone
def hostileCheck(body):
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
def truncateLogFile(logFile):
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

# Entry point
#-------------------------------------------------------------------------------------------------------

# Create the reddit instance
reddit = praw.Reddit('bot1')

# Setup the bot feedback interface
os.system('cls')
sp.call('clear',shell=True)
print('logged in as: ', reddit.user.me(), '\n')

# Setup the bot
random.seed(a=None)
configFile = configparser.ConfigParser()
configFile.read('praw.ini')
subList = configFile['bot1']['subreddits']
subreddits = subList.split(",")
paibot = updateable.updateable()


# Main program
while True:
	try:
		print('\n')
		print("------------New Cycle------------\n")

		# Cycle through subreddits
		for subredditName in subreddits:
			subreddit = reddit.subreddit(subredditName)

			# Parse comments
			try:
				for comment in subreddit.comments(limit=100):
					if comment.author is not None and comment.author != reddit.user.me():
						rtnVal = parseText(comment, comment.body, False)

						# Kill switch
						if rtnVal == False:
							messageContent = "This is a notification that I received the kill code and self-terminated.  If you or another mod initiated the termination then ignore this message.  Otherwise it is possible someone is trolling the bot and this should be investigated immediately."
							reddit.redditor("/r/KeepOurNetFree").message("Bot Termination Notice", messageContent)
							print("Received kill code.  Terminating...")
							exit()
			except Exception:
				pass

			# Parse submisssions
			try:
				for submission in subreddit.new(limit=10):

					# Ignore stickied posts
					if submission.stickied == True:
						continue

					if submission.author is not None and submission.author != reddit.user.me():
						parseText(submission, submission.title, True)
						if submission.domain.split(".")[0] is not "self":
							parseText(submission, submission.url, True)
						elif submission.body is not None:
							parseText(submission, submission.body, True)
			except Exception:
				pass

		# Parse for paibot
		for message in reddit.inbox.messages(limit=10):
			if message.author.name in paibot.admins and "UPDATE" in message.body:
				print("Recieved update command from " + message.author.name + "...")
				try:
					print("Pulling repository...")
					call("git pull")
					importlib.reload(updateable)
					message.reply("Successfully updated!")
					print("Successfully updated!")
				except Exception:
					message.reply("Error updating!")
					print("Error updating!")
				break

	except Exception as e:
		print("---------------------------------\n")
		print("An exception was thrown, trying again in 30 seconds")
		print(e)
		print("---------------------------------\n")
		time.sleep(30)

print("Something went horribly wrong.")

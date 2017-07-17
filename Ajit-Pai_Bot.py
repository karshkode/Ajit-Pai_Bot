# Ajit-Pai_Bot
version="0.06"

import pdb
import re
import os
import subprocess as sp
import datetime
import time
import random
import re
import configparser

import praw # Reddit

# Message Content
# Positive: Pai supports the comment
# Negative: Pai dislikes the comment
positive_adjective = ["exquisite", "magnificent", "breathtaking", "orgasmic", "heartwarming", "perfect", "valiant"] # Generic stuff
positive_adverb = ["humbly", "sincerely", "truthfully", "from the bottom of my heart"]
positive_openers = ["My dear", "Good", "Honorable", "Fellow"]
positive_titles = ["sir,", "redditor,", "patriot,", "hero,", "king among men,"]
positive_introduction_1 = ["you have been graced by", "I am"]
positive_introduction_2 = ["the honorable", "the marvelous", "Saint"]
positive_introduction_3 = ["Ajit Pai", "Ajit \"I have a Reese's Cup\" Pai", "Ajit \"Ajit Pai\" Pai"]
positive_body_start = ["I commend you for your [ADJECTIVE]", "Thank you for your [ADJECTIVE]", "I completely agree with this [ADJECTIVE]"]
positive_body_continuation_1 = ["idea.", "wording.", "comment."]
positive_body_continuation_2 = ["Please,", "I [ADVERB] hope that you", "It is my only wish that you"]
positive_body_continuation_3 = ["continue spreading this [ADJECTIVE] message.", "keep sharing this message of good will."]
positive_conclusion_1 = ["If you ever chance upon me IRL,", "Should we meet again"]
positive_conclusion_2 = ["please do not hesitate to continue this conversation.", "regale me once more with your [ADJECTIVE] thoughts."]

# Parse content text and decide to act upon it
def parseText(comment, body, post):
	"Parses the text of a comment and decides"

	#################
	# Kill switch 	#
	#################
	if comment.parent().author == reddit.user.me() and "ModBotCode:" in body:
		killcfg = configparser.ConfigParser()
		killcfg.read('praw.ini')
		killcode = killcfg['bot1']['killcode']

		if body == "ModBotCode:" + killcode and comment.author in killcfg['admins']['admin']:
			replyContent(comment, "Copy that, I'm super broken! --> Terminating!!!")
			return False

	#############################################
	# Parse for potential content to reply to 	#
	#############################################
	try:
		
		# Pro net neutrality comment
		if "" in body:
			pass

		# Anti net neutrality comment
		elif "" in body:
			pass

	except Exception:
		pass

	return True

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
		rText = text + "\n\n>ajit.pai@fcc.gov\n>202-418-2000)."
		with open('replyLog.txt', 'a') as replyLog:
			comment.reply(rText)
			try:
				print("| Replying to comment: " + comment.body, text)
			except Exception:
				print("| Replying to post: " + comment.title, text)
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

# Main program
while True:
	try:
		print('\n')
		print("------------New Cycle------------\n")

		# Cycle through subreddits
		for subreddit in subreddits:

			# Parse comments
			for comment in subreddit.comments(limit=100):
				if comment.author is not None and comment.author != reddit.user.me():
				    rtnVal = parseText(comment, comment.body, False)

				    # Kill switch
				    if rtnVal == False:
				    	messageContent = "This is a notification that I received the kill code and self-terminated.  If you or another mod initiated the termination then ignore this message.  Otherwise it is possible someone is trolling the bot and this should be investigated immediately."
				    	reddit.redditor("/r/KeepOurNetFree").message("Bot Termination Notice", messageContent)
				    	print("Received kill code.  Terminating...")
				    	exit()

			# Parse submisssions
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

	except Exception as e:
		print("---------------------------------\n")
		print("An exception was thrown, trying again in 30 seconds")
		print(e)
		print("---------------------------------\n")
		time.sleep(30)

print("Something went horribly wrong.")

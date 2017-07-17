# Ajit-Pai_Bot
version="0.03"

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

# Parse content text and decide to act upon it
def parseText(comment, body, post):
	"Parses the text of a comment and decides"

	#############################################
	# Parse for potential comments to reply to 	#
	#############################################
	if not post:
		pass

	#################################################
	# Parse for potential submissions to reply to 	#
	#################################################
	else:
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
			print("=================================\n")
			print("| Replying to comment: ", text)
			print("=================================\n")
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
			print("=================================\n")
			print("| Reporting comment: ", comment.id, " for ", reasonstring)
			print("=================================\n")
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
				    if comment.body is not None:
				    	print("Comment in thread --> ", comment.submission)
				    	print("By user --> ", comment.author)
				    	print("Text: ", comment.body)
				    else:
				    	print("Text: ", None)
				    print("Score: ", comment.score)
				    rtnVal = parseText(comment, comment.body, False)

				    # Kill switch
				    if rtnVal == False:
				    	messageContent = "This is a notification that I received the kill code and self-terminated.  If you or another mod initiated the termination then ignore this message.  Otherwise it is possible someone is trolling the subreddit and this should be investigated immediately."
				    	reddit.redditor("/r/KeepOurNetFree").message("Bot Termination Notice", messageContent)
				    	print("Received kill code.  Terminating...")
				    	exit()

			# Parse submisssions
			for submission in subreddit.new(limit=10):
				print("Submission in subreddit --> ", subreddit)
				print("By user --> ", submission.author)
				print("Title --> ", submission.title)

				# Ignore stickied posts
				if submission.stickied == True:
					continue

				if submission.author is not None and submission.author != reddit.user.me():
					parseText(submission, submission.title, True)
					if submission.domain.split(".")[0] is not "self":
						parseText(submission, submission.url, True)
						print("Link post --> ", submission.url)
					elif submission.body is not None:
						parseText(submission, submission.body, True)
						print("Self post --> ", submission.body)

				if submission.over_18:
					removeContent(submission, "Flagged NSFW")

	except Exception as e:
		print("---------------------------------\n")
		print("An exception was thrown, trying again in 30 seconds")
		print(e)
		print("---------------------------------\n")
		time.sleep(30)

print("Something went horribly wrong.")

import configparser

class updateable:

	# Message Content
	# Elements in the array are delimited with the | character in config.cfg
	# FORMATTING:
	# [ADJECTIVE]: Replace with adjective from the _adjective array
	# [ADVERB]: Replace with adverb from the _adverb array
	# ~: Only include bot message in signature (ie don't give contact details)

	# Constructor
	def __init__(self):
		self.readConfig()

	# Destructor
	def __del__(self):
		return

	# Update from file
	def readConfig(self):

		# Some config parsers to parse configs with
		cfg = configparser.ConfigParser()
		cfg.read('config.cfg')

		# Positive: Pai supports the comment
		self.positive_adjective = cfg['paibot']['positive_adjective'].split("|")
		self.positive_adverb = cfg['paibot']['positive_adverb'].split("|")
		self.positive_openers = cfg['paibot']['positive_openers'].split("|")
		self.positive_titles = cfg['paibot']['positive_titles'].split("|")
		self.positive_introduction_1 = cfg['paibot']['positive_introduction_1'].split("|")
		self.positive_introduction_2 = cfg['paibot']['positive_introduction_2'].split("|")
		self.positive_introduction_3 = cfg['paibot']['positive_introduction_3'].split("|")
		self.positive_body_start = cfg['paibot']['positive_body_start'].split("|")
		self.positive_body_continuation_1 = cfg['paibot']['positive_body_continuation_1'].split("|")
		self.positive_body_continuation_2 = cfg['paibot']['positive_body_continuation_2'].split("|")
		self.positive_body_continuation_3 = cfg['paibot']['positive_body_continuation_3'].split("|")
		self.positive_conclusion_1 = cfg['paibot']['positive_conclusion_1'].split("|")
		self.positive_conclusion_2 = cfg['paibot']['positive_conclusion_2'].split("|")
		self.positive_signature = cfg['paibot']['positive_signature'].split("|")
		self.positive_complete = cfg['paibot']['positive_complete'].split("|")

		self.positive = [self.positive_adjective,
				self.positive_adverb,
				self.positive_openers,
				self.positive_titles,
				self.positive_introduction_1,
				self.positive_introduction_2,
				self.positive_introduction_3,
				self.positive_body_start,
				self.positive_body_continuation_1,
				self.positive_body_continuation_2,
				self.positive_body_continuation_3,
				self.positive_conclusion_1,
				self.positive_conclusion_2,
				self.positive_signature,
				self.positive_complete]

		# Negative: Pai dislikes the comment
		self.negative_adjective = cfg['paibot']['negative_adjective'].split("|")
		self.negative_adverb = cfg['paibot']['negative_adverb'].split("|")
		self.negative_titles = cfg['paibot']['negative_titles'].split("|")
		self.negative_introduction_1 = cfg['paibot']['negative_introduction_1'].split("|")
		self.negative_introduction_2 = cfg['paibot']['negative_introduction_2'].split("|")
		self.negative_introduction_3 = cfg['paibot']['negative_introduction_3'].split("|")
		self.negative_body_start = cfg['paibot']['negative_body_start'].split("|")
		self.negative_body_continuation_1 = cfg['paibot']['negative_body_continuation_1'].split("|")
		self.negative_body_continuation_2 = cfg['paibot']['negative_body_continuation_2'].split("|")
		self.negative_body_continuation_3 = cfg['paibot']['negative_body_continuation_3'].split("|")
		self.negative_conclusion_1 = cfg['paibot']['negative_conclusion_1'].split("|")
		self.negative_conclusion_2 = cfg['paibot']['negative_conclusion_2'].split("|")
		self.negative_conclusion_3 = cfg['paibot']['negative_conclusion_3'].split("|")
		self.negative_signature =  cfg['paibot']['negative_signature'].split("|")
		self.negative_complete = cfg['paibot']['negative_complete'].split("|")

		self.negative = [self.negative_adjective,
				self.negative_adverb,
				self.negative_titles,
				self.negative_introduction_1,
				self.negative_introduction_2,
				self.negative_introduction_3,
				self.negative_body_start,
				self.negative_body_continuation_1,
				self.negative_body_continuation_2,
				self.negative_body_continuation_3,
				self.negative_conclusion_1,
				self.negative_conclusion_2,
				self.negative_signature,
				self.negative_complete]

		# Question answer strings
		self.answer_adjective = cfg['paibot']['answer_adjective'].split("|")
		self.answer_adverb = cfg['paibot']['answer_adverb'].split("|")
		self.answer_titles = cfg['paibot']['answer_titles'].split("|")
		self.answer_introduction_1 = cfg['paibot']['answer_introduction_1'].split("|")
		self.answer_introduction_2 = cfg['paibot']['answer_introduction_2'].split("|")
		self.answer_introduction_3 = cfg['paibot']['answer_introduction_3'].split("|")
		self.answer_body_start = cfg['paibot']['answer_body_start'].split("|")
		self.answer_body_continuation_1 = cfg['paibot']['answer_body_continuation_1'].split("|")
		self.answer_body_continuation_2 = cfg['paibot']['answer_body_continuation_2'].split("|")
		self.answer_body_continuation_3 = cfg['paibot']['answer_body_continuation_3'].split("|")
		self.answer_conclusion_1 = cfg['paibot']['answer_conclusion_1'].split("|")
		self.answer_conclusion_2 = cfg['paibot']['answer_conclusion_2'].split("|")
		self.answer_conclusion_3 = cfg['paibot']['answer_conclusion_3'].split("|")
		self.answer_signature =  cfg['paibot']['answer_signature'].split("|")
		self.answer_complete = cfg['paibot']['answer_complete'].split("|")

		self.answer = [self.answer_adjective,
				self.answer_adverb,
				self.answer_titles,
				self.answer_introduction_1,
				self.answer_introduction_2,
				self.answer_introduction_3,
				self.answer_body_start,
				self.answer_body_continuation_1,
				self.answer_body_continuation_2,
				self.answer_body_continuation_3,
				self.answer_conclusion_1,
				self.answer_conclusion_2,
				self.answer_signature,
				self.answer_complete
		]

		# List of strings to identify a valid comment to reply to
		self.questionKeyStrings = cfg['paibot']['questionKeyStrings'].split("|")
		self.netNeutralityKeyStrings = cfg['paibot']['netNeutralityKeyStrings'].split("|")
		self.proNetNeutralityStrings = cfg['paibot']['proNetNeutralityStrings'].split("|")
		self.antiNetNeutralityStrings = cfg['paibot']['antiNetNeutralityStrings'].split("|")

		return

	def add_subreddit(self, subreddit):
		if subreddit in self.subreddits:
			return False
		self.subreddits.append(subreddit)
		return True

	def remove_subreddit(self, subreddit):
		if not subreddit in self.subreddits:
			return False
		self.subreddits.remove(subreddit)
		return True

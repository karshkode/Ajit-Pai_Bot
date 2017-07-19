import configparser

class updateable:

	# Message Content
	# Elements in the array are delimited with the | character in config.cfg
	# FORMATTING:
	# [ADJECTIVE]: Replace with adjective from the _adjective array
	# [ADVERB]: Replace with adverb from the _adverb array
	# ~: Only include bot message in signature (ie don't give contact details)

	positive_adjective = []
	positive_adverb = []
	positive_openers = []
	positive_titles = []
	positive_introduction_1 = []
	positive_introduction_2 = []
	positive_introduction_3 = []
	positive_body_start = []
	positive_body_continuation_1 = []
	positive_body_continuation_2 = []
	positive_body_continuation_3 = []
	positive_conclusion_1 = []
	positive_conclusion_2 = []
	positive_signature = []
	positive_complete = []

	positive = [positive_adjective,
				positive_adverb,
				positive_openers,
				positive_titles,
				positive_introduction_1,
				positive_introduction_2,
				positive_introduction_3,
				positive_body_start,
				positive_body_continuation_1,
				positive_body_continuation_2,
				positive_body_continuation_3,
				positive_conclusion_1,
				positive_conclusion_2,
				positive_signature,
				positive_complete]

	# Negative: Pai dislikes the comment
	negative_adjective = []
	negative_adverb = []
	negative_titles = []
	negative_introduction_1 = []
	negative_introduction_2 = []
	negative_introduction_3 = []
	negative_body_start = []
	negative_body_continuation_1 = []
	negative_body_continuation_2 = []
	negative_body_continuation_3 = []
	negative_conclusion_1 = []
	negative_conclusion_2 = []
	negative_conclusion_3 = []
	negative_signature =  []
	negative_complete = []

	negative = [negative_adjective,
				negative_adverb,
				negative_titles,
				negative_introduction_1,
				negative_introduction_2,
				negative_introduction_3,
				negative_body_start,
				negative_body_continuation_1,
				negative_body_continuation_2,
				negative_body_continuation_3,
				negative_conclusion_1,
				negative_conclusion_2,
				negative_signature,
				negative_complete]

	# List of strings to identify a valid comment to reply to
	netNeutralityKeyStrings = []
	proNetNeutralityStrings = []
	antiNetNeutralityStrings = []

	# Misc
	subreddits = []
	admins = []

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

		# List of strings to identify a valid comment to reply to
		self.netNeutralityKeyStrings = cfg['paibot']['netNeutralityKeyStrings'].split("|")
		self.proNetNeutralityStrings = cfg['paibot']['proNetNeutralityStrings'].split("|")
		self.antiNetNeutralityStrings = cfg['paibot']['antiNetNeutralityStrings'].split("|")

		# Misc
		self.subreddits = cfg['paibot']['subreddits'].split("|")
		self.admins = cfg['paibot']['admins'].split("|")

		return
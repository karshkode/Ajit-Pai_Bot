import configparser

class updateable:

	# Constructor
	def __init__(self):
		self.readConfig()
		return

	# Destructor
	def __del__(self):
		return

	# Update from file
	def readConfig(self):

		# Some config parsers to parse configs with
		cfg = configparser.ConfigParser()
		cfg.read('config.cfg')

		# Debug
		print(positive_adjective)
		print(cfg['paibot']['positive_adjective'].split("|"))
		print(positive_adjective)

		# Positive: Pai supports the comment
		positive_adjective = cfg['paibot']['positive_adjective'].split("|")
		positive_adverb = cfg['paibot']['positive_adverb'].split("|")
		positive_openers = cfg['paibot']['positive_openers'].split("|")
		positive_titles = cfg['paibot']['positive_titles'].split("|")
		positive_introduction_1 = cfg['paibot']['positive_introduction_1'].split("|")
		positive_introduction_2 = cfg['paibot']['positive_introduction_2'].split("|")
		positive_introduction_3 = cfg['paibot']['positive_introduction_3'].split("|")
		positive_body_start = cfg['paibot']['positive_body_start'].split("|")
		positive_body_continuation_1 = cfg['paibot']['positive_body_continuation_1'].split("|")
		positive_body_continuation_2 = cfg['paibot']['positive_body_continuation_2'].split("|")
		positive_body_continuation_3 = cfg['paibot']['positive_body_continuation_3'].split("|")
		positive_conclusion_1 = cfg['paibot']['positive_conclusion_1'].split("|")
		positive_conclusion_2 = cfg['paibot']['positive_conclusion_2'].split("|")
		positive_signature = cfg['paibot']['positive_signature'].split("|")
		positive_complete = cfg['paibot']['positive_complete'].split("|")

		# Negative: Pai dislikes the comment
		negative_adjective = cfg['paibot']['negative_adjective'].split("|")
		negative_adverb = cfg['paibot']['negative_adverb'].split("|")
		negative_titles = cfg['paibot']['negative_titles'].split("|")
		negative_introduction_1 = cfg['paibot']['negative_introduction_1'].split("|")
		negative_introduction_2 = cfg['paibot']['negative_introduction_2'].split("|")
		negative_introduction_3 = cfg['paibot']['negative_introduction_3'].split("|")
		negative_body_start = cfg['paibot']['negative_body_start'].split("|")
		negative_body_continuation_1 = cfg['paibot']['negative_body_continuation_1'].split("|")
		negative_body_continuation_2 = cfg['paibot']['negative_body_continuation_2'].split("|")
		negative_body_continuation_3 = cfg['paibot']['negative_body_continuation_3'].split("|")
		negative_conclusion_1 = cfg['paibot']['negative_conclusion_1'].split("|")
		negative_conclusion_2 = cfg['paibot']['negative_conclusion_2'].split("|")
		negative_conclusion_3 = cfg['paibot']['negative_conclusion_3'].split("|")
		negative_signature =  cfg['paibot']['negative_signature'].split("|")
		negative_complete = cfg['paibot']['negative_complete'].split("|")

		# List of strings to identify a valid comment to reply to
		netNeutralityKeyStrings = cfg['paibot']['netNeutralityKeyStrings'].split("|")
		proNetNeutralityStrings = cfg['paibot']['proNetNeutralityStrings'].split("|")
		antiNetNeutralityStrings = cfg['paibot']['antiNetNeutralityStrings'].split("|")

		# Misc
		subreddits = cfg['paibot']['subreddits'].split("|")
		admins = cfg['paibot']['admins'].split("|")

		return

	########
	# Init #
	########

	# Message Content
	# FORMATTING:
	# [ADJECTIVE]: Replace with adjective from the _adjective array
	# [ADVERB]: Replace with adverb from the _adverb array
	# ~: Only include bot message in signature (ie don't give contact details)

	# Positive: Pai supports the comment
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
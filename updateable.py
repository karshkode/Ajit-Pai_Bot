# Message Content
# FORMATTING:
# [ADJECTIVE]: Replace with adjective from the _adjective array
# [ADVERB]: Replace with adverb from the _adverb array
# ~: Only include bot message in signature (ie don't give contact details)

# Positive: Pai supports the comment
positive_adjective = ["exquisite", "magnificent", "breathtaking", "orgasmic", "heartwarming", "perfect", "valiant"] # Generic stuff
positive_adverb = ["humbly", "sincerely", "truthfully", "from the bottom of my heart"]
positive_openers = ["My dear", "Good", "Honorable", "Fellow"]
positive_titles = ["sir,", "redditor,", "patriot,", "hero,", "king among men,"]
positive_introduction_1 = ["you have been graced by", "I am"]
positive_introduction_2 = ["the honorable", "the marvelous", "Saint"]
positive_introduction_3 = ["Ajit Pai.", "Ajit \"I have a Reese's Cup\" Pai.", "Ajit \"Ajit Pai\" Pai.", "Ajit \"Big Mug, Big Shot\" Pai."]
positive_body_start = ["I commend you for your [ADJECTIVE]", "Thank you for your [ADJECTIVE]", "I completely agree with this [ADJECTIVE]"]
positive_body_continuation_1 = ["idea.", "wording.", "comment."]
positive_body_continuation_2 = ["Please,", "I [ADVERB] hope that you", "It is my only wish that you"]
positive_body_continuation_3 = ["continue spreading this [ADJECTIVE] message.", "keep sharing this message of good will."]
positive_conclusion_1 = ["If you ever chance upon me IRL,", "Should we meet again"]
positive_conclusion_2 = ["please do not hesitate to continue this conversation.", "regale me once more with your [ADJECTIVE] thoughts."]
positive_signature = ["\n\nYours truly,", "\n\nYour friend", "\n\nYour lifelong ally,"]
positive_complete = ["Just to be clear, I'm not a professional \"FCC Chairman\". I'm just an ex-Verizon Lawyer who greatly values a closed internet and ISP monopolies over millions of silly comments written by the people I'm supposed to be helping. That being said, I am open to any and all criticism (although I might ignore it and take a sip from my Reese's cup instead).\n\n\"In this moment, I am euphoric.  Not because of any phony internet freedom. But because, I am enlightened by this [ADJECTIVE] comment.\" - Ajit Pai\n\nEh?~"]

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
negative_adjective = ["disgusting", "vile", "Satan-esque", "terrible", "nauseating", "sickening", "evil"] # Generic stuff
negative_adverb = ["humbly", "sincerely", "truthfully", "from the bottom of my heart"]
negative_titles = ["Evildoer,", "Menace,", "Idiot,", "Libtard", "Asshat"]
negative_introduction_1 = ["you have been graced by", "I am"]
negative_introduction_2 = ["the honorable", "the marvelous", "Saint"]
negative_introduction_3 = ["Ajit Pai.", "Ajit \"I have a Reese's Cup\" Pai.", "Ajit \"Ajit Pai\" Pai.", "Ajit \"Big Mug, Big Shot\" Pai."]
negative_body_start = ["You should be ashamed of your [ADJECTIVE]", "I became physically ill reading this [ADJECTIVE]", "That is one [ADJECTIVE]"]
negative_body_continuation_1 = ["idea.", "comment.", "thought."]
negative_body_continuation_2 = ["Please,", "Although you should be locked in an asylum for these thoughts, I [ADVERB] hope that you", "I am a caring person, though, so I want you to"]
negative_body_continuation_3 = ["DELET THIS.", "think long and hard about your [ADJECTIVE] ideas and change them.", "repent for these sinful ideas."]
negative_conclusion_1 = ["If you ever chance upon me IRL,", "Should we meet again"]
negative_conclusion_2 = ["I wouldn't make yourself known to me,", "you should run away,"]
negative_conclusion_3 = ["as I would immediately challenge you to a duel (which you'd lose).", "lest I unleash my squadron of ISP security guards upon you.", "unless you'd like to experience the full force of my Reese's Cup rain upon you."]
negative_signature = ["\n\nYour mortal enemy,", "\n\nSincerely,", "\n\nMay you rot in the undrained swamp,"]
negative_complete = ["I'd just like to interject for a moment. What you're referring to as Net Neutrality, is in fact, Title II/Net Neutrality, or as I've recently taken to calling it, Title II plus Net Neutrality.  Net Neutrality is not a system of regulations unto itself, but rather another component of a fully functioning Title II system made useful by the FCC, ISPs, and other government agencies comprising a full regulatory system as defined by myself.\n\nMany people rely on the Title II system every day, without realizing it.  Through a peculiar turn of events, the version of Title II which is widely discussed today is often called \"Net Neutrality\", and many of its supporters are not aware that it is basically the Title II regulations, developed by the FCC.\n\nThere really is Net Neutrality, and these people are using it, but it is just a part of the internet they use.  Net Neutrality is the idea, the principle in the regulations that tells ISPs to treat all internet services the same. The principle is an essential part of Title II, but useless by itself; it can only function in the context of a complete regulatory system. Net Neutrality is normally used in combination with the Title II regulations: all of the regulations are basically Title II with Net Neutrality added, or Title II/Net Neutrality.  All the so-called \"Net Neutrality\" regulations are really regulations of Title II/Net Neutrality.\n\nSincerely,"]

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
netNeutralityKeyStrings = ["net neutrality", "title ii", "title 2", "ajit pai", "michael o'rilley", "fcc"]
proNetNeutralityStrings = ["free", "support", "open", "consumer", "battleforthenet"]
antiNetNeutralityStrings = ["repeal", "business", "leftist", "libtard", "oppose", "cuck"]

# Subreddits
subreddits = ["BotShitposts", "KONFTesting"]

# symptoms
symp = [{'tag':'bleeding',
			'var':['bleeding', 'bled', 'blood'],
			'follow':'Is it a puncture wound?',
			'sub':['bleeding_punc', 'bleeding_cut']},
		{'tag':'burning',
			'var':['burning', 'burned', 'burnt', 'burn'],
			'follow':'Is it a chemical burn?',
			'sub':['burning_chemical', 'burning_thermal']},
		{'tag':'breathing',
			'var':['breathing', 'breathe', 'breath', 'breathed'],
			'follow':'Is the victim choking?',
			'sub':['choking_other', 'breathing_other']},
		{'tag':'chest_pain',
			'var':['chest pain', 'chest'],
			'follow':'Is the victim having a heart attack?',
			'sub':['chest_pain_heart_attack', 'chest_pain_other']},
		{'tag':'choking',
			'var':['choking', 'choked', 'choke'],
			'follow':'Is the victim having an allergy attack?',
			'sub':['choking_allergy', 'choking_other']},
		{'tag':'broken',
			'var':['broken', 'breaking', 'break'],
			'follow':'Is the victim\'s neck or back broken?',
			'sub':['broken_neck_back', 'broken_other']},
		{'tag':'overdose',
			'var':['overdose', 'over dose'],
			'follow':'',
			'sub':['overdose']},
		{'tag':'unconscious',
			'var':['unconscious', 'faint', 'fainted', 'passed out', 'knocked out'],
			'follow':'Does the victim have a heartbeat?',
			'sub':['unconscious_other', 'unconscious_abc']},
		{'tag':'pregnant',
			'var':['pregnant', 'labor', 'having a baby'],
			'follow':'',
			'sub':['pregnant']},
		{'tag':'siezure',
			'var':['siezure', 'seizing'],
			'follow':'Is the siezure impact induced?',
			'sub':['siezure_impact', 'siezure_other']},
		{'tag':'dislocation',
			'var':['dislocation', 'dislocatated'],
			'follow':'Is the victim\'s neck or back dislocated?',
			'sub':['dislocation_neck_back', 'dislocation_other']},
		{'tag':'stroke',
			'var':['stroke'],
			'follow':'Is the victim unconscious?',
			'sub':['stroke']},
		{'tag':'heat_stroke',
			'var':['heat stroke', 'too hot'],
			'follow':'',
			'sub':['heat_stroke']},
		{'tag':'hypothermia',
			'var':['hypothermia', 'too cold'],
			'follow':'',
			'sub':['hypothermia']},
		{'tag':'help',
			'var':['help', 'about'],
			'follow':'',
			'sub':['help_about']}]
# sub symptoms
sub_symp = [{'sub_tag':'bleeding_cut',
				'resp':'\n\n1. Place dressing over the cut to absorb blood.\n2. Apply direct pressure to stop bleeding.'},
			{'sub_tag':'bleeding_punc',
				'resp':'\n\n1. If the object is in the victim, do NOT remove it.\n2. Place dressing around the object to absorb blood.\n3. Apply pressure to stop bleeding, without pushing on the object.'},
			{'sub_tag':'burning_chemical',
				'resp':'\n\n1. Remove the chemical from your skin.\n2. Rinse the burned area under cool water for up to 20 minutes.'},
			{'sub_tag':'burning_thermal',
				'resp':'\n\n1. Wash under cool water for up to 10 minutes.\n2. Loosely wrap the burn in clean dressing.'},
			{'sub_tag':'breathing_other',
				'resp':'\n\n1. Find a position of rest.\n2. Attempt to take deep breathes.\n3. Drink water as able.'},
			{'sub_tag':'chest_pain_heart_attack',
				'resp':'\n\n1. Kneel next to the victim and place both hands on their chest with straight arms.\n2. Push their chest down ~ 2 inches, 100 times per minute.'},
			{'sub_tag':'chest_pain_other',
				'resp':'\n\n1. Find a position of rest.\n2. Attempt to take deep breathes.\n3. Drink water as able.'},
			{'sub_tag':'choking_allergy',
				'resp':'\n\n1. Take allergy medication as available.\n2. Find a position of rest.\n3. Attempt to take deep breathes.'},
			{'sub_tag':'choking_other',
				'resp':'\n\n1. Stand behind the victim.\n2. Place 1 fist under their sternum, grabbing it with your other hand.\n3. Quickly pull in and up, repeating until object is dislodged.'},
			{'sub_tag':'broken_neck_back',
				'resp':'\n\n1. Lie down on a flat surface.\n2. Minimize head and back movement.'},
			{'sub_tag':'broken_other',
				'resp':'\n\n1. Support the break with a rigid object.\n2. Minimize its movement.'},
			{'sub_tag':'overdose',
				'resp':'\n\n1. Place the victim on their side.\n2. Do NOT force them to vomit.\n3. Do NOT give them food or water.'},
			{'sub_tag':'unconscious_abc',
				'resp':'\n\n1. Kneel next to the victim and place both hands on their chest with straight arms.\n2. Push their chest down ~ 2 inches, 100 times per minute.'},
			{'sub_tag':'unconscious_other',
				'resp':'\n\n1. Place the victim on their side.\n2. Wait for them to wake up.'},
			{'sub_tag':'pregnant',
				'resp':'\n\n1. Have the woman lie on their back, with their feet up.\n2. Prepare to catch the baby.\n3. Do NOT pull the baby out.'},
			{'sub_tag':'siezure_impact',
				'resp':'\n\n1. Remove dangerous objects from the area.\n2. Prepare to hold their neck and back in a stable position AFTER they stop siezing.'},
			{'sub_tag':'siezure_other',
				'resp':'\n\n1. Remove dangerous objects from the area.\n2. Do NOT attempt to restrain the victim.'},
			{'sub_tag':'dislocation_neck_back',
				'resp':'\n\n1. Lie down on a flat surface.\n2. Minimize head and back movement.'},
			{'sub_tag':'dislocation_other',
				'resp':'\n\n1. Support the bones above and below the dislocation with a rigid object or sling.'},
			{'sub_tag':'heat_stroke',
				'resp':'\n\n1. Have the victim lie down, out of the heat.\n2. Cool them as quickly as possible.'},
			{'sub_tag':'hypothermia',
				'resp':'\n\n1. Warm up the victim at a slow rate, until they have stopped shivering.'},
			{'sub_tag':'help_about',
				'resp':'\n\nWelcome to Health Help. If this is an emergency, contact emergency services immediately, then describe the probem to me. I will guide you in caring for the victim until professionals arrive.'}]
# search string for tags
def get_tag(str):
	for s in symp:
		for v in s['var']:
			if v in str:
				return s['tag']
# get follow up message for symptom
def get_follow(tag):
	try:
		return [x for x in symp if x['tag'] == tag][0]['follow']
	except:
		return ''
# get sub symptom
def get_sub_tag(tag, resp):
	try:
		if resp == 'yes':
			return [x for x in symp if x['tag'] == tag][0]['sub'][0]
		if resp == 'no':
			return [x for x in symp if x['tag'] == tag][0]['sub'][1]
	except:
		return ''
# get response
def get_response(sub):
	try:
		return [x for x in sub_symp if x['sub_tag'] == sub][0]['resp']
	except:
		return 'Sorry, I didn\'t understand what you said.'
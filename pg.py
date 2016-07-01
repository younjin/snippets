# v0: pick four random words from /usr/share/dict/words

import random

with open("/usr/share/dict/words") as words:
	words = words.readlines()
	pick = random.sample(words,4)
	pick_strip = [word.strip() for word in pick]
	print "".join(pick_strip)
	
# v1: limit the potential words that are chosen
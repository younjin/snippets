# v0: pick four random words from /usr/share/dict/words
# v1: limit the potential words to those with >4 chars

import random

with open("/usr/share/dict/words") as words:
	words = words.readlines()
	words = [word for word in words if len(word) > 4]
	pick = random.sample(words,4)
	pick_strip = [word.strip() for word in pick]
	print "".join(pick_strip)
	

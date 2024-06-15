# this is an implementation of a rudimentary abbreviator
# it works by dividing a word into (hypothesized) syllables, then using the first two syllables
# args: file of terms to abbreviate
# need to do 'pip install spacy' first, and 'python -m spacy download [model]'!
# examples of models are:
#  	English: en_core_web_sm
#	Spanish: es_core_news_sm
#	French: fr_core_news_sm
#	Greek: el_core_news_sm
#	Hindi: hi_core_news_sm
#	Bengali: bn_core_news_sm
#	Arabic: ar_core_news_sm
#	Chinese: zh_core_web_sm


import spacy
import sys

model = 'en_core_web_sm'
nlp = spacy.load(model)

file = open(sys.argv[1],'r')
lines = file.readlines()
#lines = ['evaluate', 'small','abbreviator','abbrev','test_abbrev_undec','test_abbreviator_at_undecores', 'and']
file.close()
all_terms = set()
for i in lines:
	all_terms.add(i.strip())

all_abbrevs = set()
final_list = list()

lang_code = 'en'

# checks if a given word is an article, conjunction, or preposition (omitted); if so then it may be excluded from a term phrase
def is_irrelevant(word):
	pos = nlp(word)[0].pos_
	tag = nlp(word)[0].tag_
	print(word,':',pos,',',tag)
	if pos == 'DET' or pos == 'CCONJ':# or pos == 'SCONJ' or pos == 'ADP':
		# if the part of speech is either an article, conjunction, or preposition (omitted):
		return True
	elif tag == 'DT':
		return True
	else:
		return False


# for the purposes of this program, a syllable is either a vowel or consonant+vowel
def get_syllables(word):
	# vowels from Roman, Arabic, Bengali, Greek, and Hindi scripts (respectively)
	vowels = ['a','e','I','o','u','A','E','I','O','U','ا','ي'و','অ','আ','ই','ঈ','উ','ঊ','ঋ','এ', 'ঐ', 'ও', 'ঔ', অ্যা', 'া', 'ী', 'ূ', 'ৄ', 'ৣ', 'ি', 'ু', 'ৃ', 'ৢ', 'ে', 'ৈ', 'ো', 'ৌ', 'ε', 'έ', 'ὲ', 'ι', 'ί', 'ῖ', 'ῑ', 'ῗ', 'ῒ', 'ΐ', 'ῐ', 'ϊ', 'ὶ', 'ο', 'υ', 'ύ', 'ὺ', 'ῦ', 'α', 'ᾳ', 'ά', 'ὰ', 'ᾱ', 'ᾶ', 'ᾰ', 'ᾴ', 'ᾲ', 'ᾷ', 'ό', 'ὸ', 'ω', 'ῳ', 'ώ', 'ὼ', 'ῶ', 'ῴ', 'ῲ', 'ῷ', 'η', 'ῆ', 'ή', 'ὴ', 'ῃ', 'ῄ', 'ῂ', 'ῇ', 'अ', 'आ', 'इ','ई','उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं','अः', 'ऋ', 'ॠ',' ा','ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ']
	syllables = list()
	cur = ''
	for i in word:
		if i in vowels:
			# we have reached the end of a syllable
			cur += i
			syllables.append(cur)
			cur = ''
		else:
			# starting a new syllable
			cur += i
	return syllables
	

def abbreviate(word, complete):
	# if 'complete' is True, means that word is not part of a larger term with underscores
	syllables = get_syllables(word)
	if len(syllables) > 2:
		# use the first two syllables + the next consonant
		term = ''.join(syllables[0:2]) + word[len(''.join(syllables[0:2]))]		
		# check for duplicate abbreviations/terms
		if complete:
			all_terms.remove(word) # to prevent the word from being compared to itself
			print(all_terms)
			print(all_abbrevs)
			# ensures that terms do not abbreviate to other terms/abbreviations
			while term in all_terms or term in all_abbrevs:
				term += word[len(term)]
			all_terms.add(word)
		#else:
		#	# ensures that terms do not abbreviate to other terms/abbreviations
		#	while term in all_abbrevs:
		#		term += word[len(term)]
		return term
	else: # otherwise, don't need to abbreviate the word
		return word


# main
for term in lines:
	print(term.strip())
	if '_' in term:
		parts = term.strip().split('_')
		new_term = ''
		for part in parts:
			if not is_irrelevant(part):
				new_term += abbreviate(part, False) + '_'
		new_term = new_term[:-1]

		# handles any potential collisions with existing abbreviations by iteratively reverting words
		all_terms.remove(term.strip())
		k = 0
		while (new_term in all_abbrevs or new_term in all_terms) and k<len(parts): # we have a collision
			print(k)
			print(new_term)
			new_parts = new_term.split('_')
			new_parts[k] = parts[k]
			k += 1
			new_term = '_'.join(new_parts)
		all_terms.add(term.strip())

		all_abbrevs.add(new_term)
		final_list.append(new_term)
	else:
		new_term = abbreviate(term.strip(), True)
		all_abbrevs.add(new_term)
		final_list.append(new_term)

with open('abbrev_'+sys.argv[1],'w') as new_file:
	for term in final_list:
		new_file.write(term.strip() + '\n')

#print(lines)
print(final_list)

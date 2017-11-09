import re
from numbersdict import number_dict
""" 
This is the original
"""

"""
def change_string(sentence):
	words = list(sentence.split())
	for index, word in enumerate(words):
		for key in number_dict:
			for item in number_dict[key]:
				if re.search(item, word, re.IGNORECASE):
					new_word = number_dict[key + 1][0]
					string_size = (len(word)-1) - len(item)
					if len(word) != len(item):
						words[index]= new_word + word[string_size:]
					else:
						words[index]= new_word
					#words.insert(index, word)
	words = map(str, words)
	words = " ".join(words)
return words
"""

""" 
This one is refactored to use the list, but take away the regex 
(faster) I also added in capitalization, and took away the need 
for calculating the length of the word, using str.replace() 
instead.
"""

"""
def change_string(sentence):
	words = list(sentence.split())
	for key in number_dict:
		for item in number_dict[key]:
			if item != number_dict[key][0]:
				for index, word in enumerate(words):
					if item in word.lower():									
						new_word = number_dict[key + 1][0]
						if word[0].isupper():
							new_word = new_word.capitalize()
							item = item.capitalize()
						sentence = str.replace(sentence, item, new_word)
	return sentence
"""

""" 
Includes all of the above, with no enumerate
"""

"""
def change_string(sentence):
	words = list(sentence.split())
	for key in number_dict:
		for item in number_dict[key]:
			if item != number_dict[key][0]:
				for word in words:
					if item in word.lower():									
						new_word = number_dict[key + 1][0]
						if word[0].isupper():
							new_word = new_word.capitalize()
							item = item.capitalize()
						sentence = str.replace(sentence, item, new_word)
	return sentence
"""

"""
Includes all of the above, with no lists, eliminating the need
to iterate through the list of words to find a match. We let
Python do the heavy lifting here.
"""
"""
def change_string(sentence):
	for key in number_dict:
		for item in number_dict[key]:
			if item != number_dict[key][0]:
				match_index = sentence.lower().find(item)			
				if match_index > -1:
					new_word = number_dict[key + 1][0]
					if sentence[match_index].isupper():				 												
						new_word = new_word.capitalize()
						item = item.capitalize()
					sentence = str.replace(sentence, item, new_word)
	return sentence
"""
"""
Lets not rely on the dictionary to be sorted.
Instead, we will add the keys to a list and sort
them. Then we will reverse and iterate through
that list so we don't ever replace a word that's 
already been replaced
"""

def change_string(sentence):
	keys_list = []
	for key in number_dict:
		keys_list += [key]
	keys_list.sort()
	for key_num in reversed(keys_list):
		for item in number_dict[key_num]:
			if item != number_dict[key_num][0]:				
				match_index = sentence.lower().find(item)			
				if match_index > -1:
					new_key = key_num + 1
					new_word = number_dict[new_key][0]
					if sentence[match_index].isupper():				 												
						new_word = new_word.capitalize()
						item = item.capitalize()
					sentence = str.replace(sentence, item, new_word)
	return sentence


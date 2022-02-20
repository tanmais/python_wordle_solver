# How to use
# - ensure that files wordle.py and wordle_word_list.txt are in the same directory
# - 
#
#

def word_fits(new_word, check_word, score):

	boolean_word_fits = True

	counter = 0
	while counter < 5:

		# confirm greenletter
		if int(score[counter]) > 1:
			
			# it is not a green
			if new_word[counter] != check_word[counter]:
				boolean_word_fits = False
		
		# confirm orange letter
		elif int(score[counter]) == 1:
			# there is a green when we were expecting orange
			if new_word[counter] == check_word[counter]:
				boolean_word_fits = False
			elif check_word[counter] not in new_word:
				boolean_word_fits = False

		# check grey letter

		elif int(score[counter]) == 0:
			if check_word[counter] in new_word:
				boolean_word_fits = False

		counter = counter + 1


	return boolean_word_fits


# enter your guesses here
# score is 0 = grey, 1 = orange, 2 = green
# you can comment out any of the guesses by putting a # in front of it
# any guesses that do not have 5 characters in their check_word and score will be ignored

# for example in wordle 247 if your choices were chasm, under and hiker .. you will set it up as

#	guesses = []
#	guesses.append({'check_word':'chasm', 'score': '01000'})
#	guesses.append({'check_word':'under', 'score': '00022'})
#	guesses.append({'check_word':'hiker', 'score': '10022'})
#	guesses.append({'check_word':'', 'score': '00222'})
#	guesses.append({'check_word':'', 'score': '22010'})

# if you run the program with the above setting 
# you will get a shortlist of 'ether' and 'other' 
# which are the only two words that fit all the 
# scores above (other was the correct answer for wordle 247)

guesses = []
guesses.append({'check_word':'chasm', 'score': '01000'})
guesses.append({'check_word':'under', 'score': '00022'})
guesses.append({'check_word':'hiker', 'score': '10022'})
guesses.append({'check_word':'', 'score': '00222'})
guesses.append({'check_word':'', 'score': '22010'})


with open('wordle_word_list.txt', 'r') as f:
	word_list = f.readlines()

word_list = [f.replace('\n','') for f in word_list]

word_list.sort()
shortlist = []

for new_word in word_list:
	if len(new_word) == 5:

		newword_fits = True
		for guess in guesses:
			if len(guess['check_word']) == 5 and len(guess['score']) == 5:
				if not word_fits(new_word, guess['check_word'], guess['score']):
					newword_fits = False

		if newword_fits:
			shortlist.append(new_word)


print(shortlist)			

#<a href="" target="_blank">***Interactive version of the dashboard below can be seen here***</a>
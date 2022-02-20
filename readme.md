This is a small program in Python to help solve wordle riddles. It takes
your guesses and their scores, compares them against the wordle masterlist
and returns a shortlist of words that would have given the same score for all the guesses


# Usage 

- ensure that files wordle.py and wordle_word_list.txt are in the same directory
- keep updating the guesses and the scores you get in wordle in the file wordle.py
- everytime you execute wordle.py, it will give you a shortlist of words that meet all the scores correctly

- guesses and scores need to be updated in line 55 onwards
- example below

    code is 0 = grey, 1 = orange, 2 = green
    you can comment out any of the guesses by putting a # in front of it
    any guesses that do not have 5 characters in their check_word and score will be ignored

    for example in wordle 247 if your choices were 
    - **chasm** (score grey-orange-grey-grey-grey)
    - **under** (score grey-grey-grey-green-green) and 
    - **hiker** (score orange-grey-grey-green-green)
    
    .. you will set it up as
```
    guesses = []
    guesses.append({'check_word':'chasm', 'score': '01000'})
    guesses.append({'check_word':'under', 'score': '00022'})
    guesses.append({'check_word':'hiker', 'score': '10022'})
    guesses.append({'check_word':'', 'score': '00222'})
    guesses.append({'check_word':'', 'score': '22010'})
```   

if you run the program with the above setting 
you will get a shortlist of 'ether' and 'other' 
which are the only two words that fit all the 
scores above ('other' was the correct answer for wordle 247)


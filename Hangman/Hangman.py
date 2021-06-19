import random
with open('wordlist.txt', 'r') as file:
	word = random.choice(list(file)).strip()
	file.close()
template = ['_' for x in word]
used_letters = str()
remaining_turn = 6
while True:
	print('{}'.format(''.join(template)))
	user = input('Select a letter: ')
	if len(user) != 1:
		print('You should use exactly one letter per turn')
		continue
	elif user in used_letters:
		print('This letter has already been used.')
		continue
	elif not user.isalpha():
		print('Please select an alphabet')
		continue
	else:
		used_letters += user.lower()
		if user not in word:
			remaining_turn = remaining_turn - 1
			print('Incorrect. Remaining turn/s = ' + str(remaining_turn))
		elif user in word:
			current_index = 0
			while True:
				current_index = word.find(user, current_index)
				if current_index == -1:
					break
				template[current_index] = user
				current_index += 1
	if remaining_turn == 0:
		print('You lose. {} is the word.'.format(word))
		break
	elif '_' not in template:
		print('You won. {} is the word'. format(word))
		break
	elif remaining_turn > 0:
		print('Remaining turn = {}'.format(remaining_turn))
		continue


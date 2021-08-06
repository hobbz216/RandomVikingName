#Creating a random fantasy name generator
import random
import random_dict as rd

def random_name():
	"""Generating a first and last name by generating random syllables and vowels"""
	

	first_random = []
	for i in range(3):
		first_random.append(random.randint(1, 3))

	last_random = []
	for i in range(4):
		last_random.append(random.randint(1, 4))

	for rando in first_random:
		if rando == 1:
			first_name = f"{random.choice(rd.f_syl_solo).title()}"
		elif rando == 2:
			first_name = f"{random.choice(rd.f_syl1).title()}{random.choice(rd.f_syl2)}"
		elif rando == 3:
			first_name = f"{random.choice(rd.f_syl1).title()}{random.choice(rd.vowel)}{random.choice(rd.f_syl2)}"


	for rando in last_random:
		if rando == 1:
			last_name = f"{random.choice(rd.l_syl_solo).title()}"
		elif rando == 2:
			last_name = f"{random.choice(rd.l_syl1).title()}{random.choice(rd.l_syl3)}"
		elif rando == 3:
			last_name = f"{random.choice(rd.l_syl1).title()}{random.choice(rd.l_syl2)}{random.choice(rd.l_syl3)}"
		elif rando == 4:
			last_name = f"{random.choice(rd.l_syl1).title()}{random.choice(rd.vowel)}{random.choice(rd.l_syl2)}{random.choice(rd.l_syl3)}"

	print(f"{first_name} {last_name}")

def syll_name():

	
	while True:
		
		syll_name_first = int(input("How many syllables for the first name (max 3)?\n"))
		
		if syll_name_first == 1:
			first_name = (f"{random.choice(rd.f_syl_solo).title()}")
		elif syll_name_first == 2:
			first_name = (f"{random.choice(rd.f_syl1).title()}{random.choice(rd.f_syl2)}")
		elif syll_name_first == 3:
			first_name = (f"{random.choice(rd.f_syl1).title()}{random.choice(rd.vowel)}{random.choice(rd.f_syl2)}")
		else:
			print("Invalid number of syllables, try again.")
			continue
		
		syll_name_last = int(input("How many syllables for the last name (max 4)?\n"))

		if syll_name_last == 1:
			last_name = (f"{random.choice(rd.l_syl_solo).title()}")
		elif syll_name_last == 2:
			last_name = (f"{random.choice(rd.l_syl1).title()}{random.choice(rd.l_syl2)}")
		elif syll_name_last == 3:
			last_name = f"{random.choice(rd.l_syl1).title()}{random.choice(rd.l_syl2)}{random.choice(rd.l_syl3)}"
		elif syll_name_last == 4:
			last_name = f"{random.choice(rd.l_syl1).title()}{random.choice(rd.vowel)}{random.choice(rd.l_syl2)}{random.choice(rd.l_syl3)}"
		else:
			print("Invalid number of syllables, try again.")
			continue
		
		print(f"{first_name} {last_name}")
		break


while True:
	print("Type 'q' for any response to exit program.")
	prompt = input("Would you like to determine the number of syllables in the name (y/n)?\n")
	
	if prompt == 'y':
		syll_name()
		another_try = input("Try again (y/n)?\n")
		if another_try == 'y':
			continue
		elif another_try == 'n':
			break
		else:
			print("Invalid response, try again.")
			continue
	elif prompt == 'n':
		random_name()
		another_try = input("Try again (y/n)?\n")
		if another_try == 'y':
			continue
		elif another_try == 'n':
			break
		else:
			print("Invalid response, try again.")
			continue
	elif prompt == 'q':
		break
	elif prompt != 'n' or 'y' or 'q':
		print("invalid response, please enter 'y' for yes or 'n' for no.  Enter 'q' to quit.")
		continue
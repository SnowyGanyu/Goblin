from agent_descriptors import *
import random 


class Agent():

	def __init__(self):
		self.first_name = random.choice(FIRST_NAMES)
		self.last_name = random.choice(LAST_NAMES)
		self.occupation = random.choice(OCCUPATION)
		self.hair_color = random.choice(HAIR_COLOR)
		self.skin_tone = random.choice(SKIN_TONE)
		self.eye_color = random.choice(EYE_COLOR)
		self.gender = random.choice(GENDER)
		self.accesory = random.choice(ACCESSORIES)

	def show_traits(self):
		# print(self.first_name)
		# print(self.last_name)
		# print(self.occupation)
		print(self.first_name, self.last_name, ": ", self.occupation)



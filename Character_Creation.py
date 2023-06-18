'''
This code captures character customization details from the user, combines them into a sentence called character_details, and then utilizes the OpenAI API 
to generate an image based on the provided details. The resulting image URL is printed as output.
'''
import openai 
import os

openai.api_key = "sk-"
print("Describe you Charater: ")

race = input("Enter the Race of your character: ")

# Ask for Class
char_class = input("Enter the Class of your character: ")

# Ask for Background
background = input("Enter the Background of your character: ")

# Ask for Alignment
alignment = input("Enter the Alignment of your character: ")

# Ask for Equipment and Gear
equipment = input("Enter the Equipment and Gear of your character: ")

# Ask for Appearance
hair_color = input("Enter the Hair Color of your character: ")
eye_color = input("Enter the Eye Color of your character: ")
height = input("Enter the Height of your character: ")
weight = input("Enter the Weight of your character: ")
distinctive_features = input("Enter any Distinctive Features of your character: ")

# Combine user inputs into a sentence
character_details = f"\nCharacter Details\n" \
                    f"-----------------\n" \
                    f"Race: {race}\n" \
                    f"Class: {char_class}\n" \
                    f"Background: {background}\n" \
                    f"Alignment: {alignment}\n" \
                    f"Equipment and Gear: {equipment}\n" \
                    f"Hair Color: {hair_color}\n" \
                    f"Eye Color: {eye_color}\n" \
                    f"Height: {height}\n" \
                    f"Weight: {weight}\n" \
                    f"Distinctive Features: {distinctive_features}"


response = openai.Image.create(prompt=character_details, n=1, size='1024x1024')

image_url = response[ 'data' ][0]['url']
print (image_url)

import json

def open_jason(f):
'''
Opens up a json file of tweets, and extracts tweets to a text file.
'''
	with open(f) as json_file:
		data = json.load(json_file)
		# This is the output file.
		text_file = open("Output_tweets.txt", "w")
		# Loop through each element in the json file.
		for p in data:
			print('Text: ' + p["text"])
			# Extracts the text content of tweets to the text file.
			# Also adds some blank lines in between to separate tweets.
			text_file.write(p["text"].encode('utf8') + '\n' + '\n')
		text_file.close()

# Change this to the name of your json file.
open_jason('Ttweets.json')

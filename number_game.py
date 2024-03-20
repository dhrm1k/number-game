import json
import random
from rich import print
from rich.panel import Panel


f = open('data.json')
 
data = json.load(f)

def printquestion():
	random_category = random.choice(list(data.keys()))

	random_value = random.choice(list(data[random_category].values()))
	panel_content = f"Question from section: [green]{random_category}[/green]\n\n{random_value}"

	panel = Panel.fit(panel_content, padding=3)

	print(panel)



def start():
	print("You want to play number game?")
	while True:
		inpt = str(input("Y/N\n"))

		if inpt == 'y' or inpt == 'Y': 
			print(f"[bold magenta]  Welcome to the number game![/bold magenta]")
			printquestion()

		elif inpt == 'n' or inpt == 'N':
			print("Sad to see you go. :(")
			print("Hope you play again!")
			break
		
		else:
			print("Input error")


start()
#this is where program progresses

# Closing file
f.close()
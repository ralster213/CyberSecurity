#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  quotes = ["As I see it, yes.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don’t count on it.",
"It is certain.",
"It is decidedly so.",
"Most likely.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Outlook good.",
"Reply hazy, try again.",
"Signs point to yes.",
"Very doubtful.",
"Without a doubt.",
"Yes.",
"Yes – definitely.",
"You may rely on it."]
  #Prompt the user for their question.
  question = input("Ask the Magic 8Ball Something: ")
  # Answer question randomly with one of the options from your earlier list.
  answer = random.choice(quotes)
  print(answer)
main()

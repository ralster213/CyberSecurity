#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
    wins = 0
    ties = 0
    losses = 0
    #Create a loop that continues as long as the user wants to play.
    play = True
    while(play == True):

    #User can play as many games as they wish.
    
    #Randomly choose the computer between 'R', 'P', or 'S'
        cpulist = ["R", "P", "S"]
        cpu = random.choice(cpulist)
        print(cpu)
    #Prompt the user for their RPS selection
        player = input("Lets play Rock Paper Scissors! Type your selection ('R' 'P' or 'S': ")
    #Determine winner and state what happened to the user
        if((player and cpu) == "R" or (player and cpu) == "P" or (player and cpu) == "S"):
            ties+=1
            print("Its a tie! You both played "+player)
        if(player == "R" and cpu == "S" or player == "S" and cpu == "P" or player == "P" and cpu == "R"):
            wins+=1
            print("You won! "+ player + " always beats " +cpu)
        if(player == "R" and cpu == "P" or player == "P" and cpu == "S" or player == "S" and cpu == "R"):
            losses+=1
            print("Aw shucks you lost! "+ cpu + " always beats " + player)
           # if(cpu == 1):
            #    ties+=1
             #   print("It's a tie! You both played Rock!")
            #if(cpu == 2):
             #   losses+=1
              #  print("You lose! Paper beats Rock!")
            #else:
             #   wins+=1
              #  print("You win! Rock beats Scissors!")
        #if(player == "P"):
         #   if(cpu == 1):
          #      wins+=1
           #     print("Paper!")
            #if(cpu == 2):
             #   losses+=1
              #  print("You lose! Paper beats Rock!")
           # else:
             #   wins+=1
              #  print("You win! Rock beats Scissors!")
    #Ask the user if they would like to play again.
        playAgain = input("Shall we play again? Say 'yes' or 'no:' ")
        if(playAgain == "yes"):
            print("Here we go again!")
        elif(playAgain == "no"):
            play = False
    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

main()

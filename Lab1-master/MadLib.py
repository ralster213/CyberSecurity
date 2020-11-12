#MadLib.py
#Name:
#Date:
#Assignment:

#def main():
    #Ask user for words
   # NounList = input("Choose three of your favorite Nouns and type them in seperately: ")
   # NounList = NounList.split()
    #print(NounList)
    #VerbList = input("Now pick three of your most cherished Verbs and type those in seperately: ")
   # VerbList = VerbList.split()
   # print(VerbList)
    #Print the story with the user supplied words.
   # print("The " + NounList[0] + " loves to " + VerbList[0] + " and " + VerbList[1] + " " + NounList[1] + " but especially " + VerbList[2] + " " + NounList[2])
#hello
#main()
from time import sleep

def main():
    #Ask user for words
    print("Fantasy First Dates!")
    sleep(2)
    N = input("Type 6 nouns: ")
    PN = input("Type 2 plural nouns: ")
    V = input("Type 2 verbs ending 'ing': ")
    place = input("Type a place: ")
    Nu = input("Type 2 Numbers: ")
    A = input("Type 4 adjectives: ")
    liquid = input("A type of liquid: ")
    #print(N+V)

    pluralNouns = PN.split()
    numbers = Nu.split()
    adjectives = A.split()
    nouns = N.split()
    verbs = V.split()
    #Print the story with the user supplied words.
    print(
        "The best first dates involve grand romantic " + pluralNouns[0]+" like these: "
    )
    print("-Charter a private "+ nouns[0] + " and fly to (the) " + place + " --also known as the " + nouns[1] +" of Love--for a/an " + numbers[0] + "-course dinner followed by a moonlit ride in a/an "+ nouns[2] + " along the canals.")
    print("-Prepare a/an "+adjectives[0]+" gourmet picnic complete with a/an "+numbers[1]+"-dollar bottle of "+liquid+" and a quartet serenading you with "+adjectives[1]+" songs.")
    print("-Rent a space on the Jumbo-"+nouns[3]+" during a/an "+nouns[4]+"-ball game and post a super-"+adjectives[2]+" message like 'Glad we're "+verbs[0]+" together here today!'")
    print("-Send a bouquet of long-stemmed red " + pluralNouns[1] + " before and after the date and for good measure, send one to the " + adjectives[3] + " restaurant when you're winning and " + verbs[1] + "your date")
    print("-Take a nighttime hot-air "+nouns[5]+" ride to the check out the stars.")
main()
#MadLib.py
#Name:
#Date:
#Assignment:

def main():
    #Ask user for words
    NounList = input("Choose three of your favorite Nouns and type them in seperately: ")
    NounList = NounList.split()
    print(NounList)
    VerbList = input("Now pick three of your most cherished Verbs and type those in seperately: ")
    VerbList = VerbList.split()
    print(VerbList)
    #Print the story with the user supplied words.
    print("The " + NounList[0] + " loves to " + VerbList[0] + " and " + VerbList[1] + " " + NounList[1] + " but especially " + VerbList[2] + " " + NounList[2])
#hello
main()

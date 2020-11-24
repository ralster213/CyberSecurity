#WordCount.py
#Name:
#Date:
#Assignment:

def main():
    textFile = open("/Users/90305007/Developer/CyberSecurity/Lab6-master/gettysberg.txt", 'r')
    #count = 0
    #for line in textFile:
    #    currentLine = line
    #    for word in currentLine:
    #        if " " in word:
    #            count += 1

        #print(line)
    #print(count)
    words = []    
    numWords = 0    
    for line in textFile:        
        words.append(line.split())    
    for line in words:        
        for word in line:            
            numWords = numWords + 1    
            print(numWords)

main()

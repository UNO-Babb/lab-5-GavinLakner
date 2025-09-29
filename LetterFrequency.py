#LetterFrequency.py
#Name: Gavin Lakner
#Date: 9/28/25
#Assignment: Letter Frequency

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter
    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1
    spot = (A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12, 
            M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20, U=21, V=22, W=23,
            X=24, Y=25, X=26)
    freq[spot] = freq[spot] + 1

    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.

    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)



if __name__ == '__main__':
  main()

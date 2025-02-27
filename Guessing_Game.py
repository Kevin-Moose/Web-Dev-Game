import random

#def surprise():


#----------------------Quit Input------------------------#

def closeprogram():
    print("\n"+"                | Game Over |"+"\n")
    print("             Thank you for playing"+"\n")
    print("               Made by:Kevin M."'\n'+'-'*50+"\n")
    input()
    quit()

#--------------------Heading Display----------------------#

def UI():
    
    print("\n"*30)
    print('\n'+'-'*50+"\n")
    print("           | Random Number Guessing Game |"+'\n'*2+"                Player name: ",name)
    print('\n'+'-'*50+'\n')
    choice()


#--------------------------Main Menu----------------------#
    
def choice():

    print("                  1. Play Game",'\n')
    print("                  2. Surprise",'\n')
    print("                  3. Quit",'\n')
    print('-'*50+'\n')
    choice=input("               Choose an option: ")
    print('\n'+'-'*50)
    if choice =="1":
        game()
    elif choice =="2":
        surprise()
    elif choice =="3":
        closeprogram()
    else:
        print("\n"+"                Unknown option"+"\n"+"\n"+ "            Press Enter to try Again")
        input()
        UI()

#------------------------Surprise----------------------#

def surprise():
    print("\n"*3)
    print("         ___________________________________")
    print("        |                                   |")
    print("        |              /|                   |")
    print("        |             /_|                   |")
    print("        |            /__|_____________      |")
    print("        |            |                |     |")
    print("        |             |_____________ ( |    |")
    print("        |                  ________|  ( |   |")
    print("        |                 /            ) |  |")
    print("        |         ________|  )~~~~~~~~~~  | |")
    print("        |        /          _____________/  |")
    print("        |       | ~~~~~~~~~~~~~)   /        |")
    print("        |        |__________   (   |        |")
    print("        |      ______________|  )   |       |")
    print("        |   __|___   ( )         (  |       |")
    print("        |  | O  O |  ~~~~~~~~~~~~~) |       |")
    print("        | (________)_______________/        |")
    print("        |  |__||__|                         |")
    print("        |     ||                            |")
    print("        |                                   |")
    print("        |     |---- PYTHON  MASTER ----|    |")
    print("        |___________________________________|")

    print("\n"*5+"             Press anything to continue")
    input()
    UI()
#-----------------------Game Start----------------------#

def game():
    print("\n")
    totalguesses=(input("             Enter the guess limit: "))
    print('\n')
    try:

#---------------------Guess Limit----------------------#
        
        if (totalguesses=="") or (totalguesses.isspace()):
            print("               No number entered."+"\n"+ "               Set to default (15)"+"\n")
            limitprompt=input("            1.Continue  2.Try Again: ")
            if limitprompt=="1":
                totalguesses=15
                print("                  Limit confirmed")
                print('\n'+'-'*50)
            elif limitprompt=="2":
                print('\n'+'-'*50)
                game()
            else:
                print("                   Unknown input")
                game()

#-------------Guess Limit Error Handling---------------#

        elif totalguesses.isalpha():
            print("              Limit cannot be letters")
            print('\n'+'-'*50)
            game()
        elif not totalguesses.isdecimal():
            print("          Limit cannot be decimal numbers")
            print('\n'+'-'*50)
            game()
        elif int(totalguesses)<1 or int(totalguesses)>100:
            print("         Total limit must be between 1-100")
            print('\n'+'-'*50)
            game()
            
        else:
            print("                  Limit confirmed")
            print('\n'+'-'*50)
    except (ValueError):
        print("\n"+"               Unknown Error")
        print('\n'+'-'*50)
        game()

#-------------------Guess Counts---------------------#
        
    numofguesses=0
    numofbadguesses=0
    
    n = random.randint(1, 200)
    
    print("\n")

#-------------------Guess Input---------------------#

    guess = input("          Choose an integer from 1 to 200: ")
    while n != "guess":

#--------------Guess Error Handling-----------------#
        
        if guess.isalpha():
            numofbadguesses=numofbadguesses+1
            print("\n"+"                 Must be a number"+"\n"+'-'*50+"\n")
            guess = input("          Choose an integer from 1 to 200: ")
        elif (guess=="") or (guess.isspace()):
            numofbadguesses=numofbadguesses+1
            print("\n"+"              You must enter something"+"\n"+'-'*50+"\n")
            guess = input("          Choose an integer from 1 to 200: ")
        elif not guess.isdecimal():
            numofbadguesses=numofbadguesses+1
            print("\n"+"                 Cannot be a decimal"+"\n"+'-'*50+"\n")
            guess = input("          Choose an integer from 1 to 200: ")
        elif int(guess)< 1 or int(guess)>200:
            numofbadguesses=numofbadguesses+1
            print("\n"+"              Number must be between 1-200"+"\n"+'-'*50+"\n")
            guess = input("          Choose an integer from 1 to 200: ")

#-------------------Guess Results---------------------#

        elif int(guess)>1 or int(guess)<200:
            if (int(totalguesses)-numofguesses)==0:
                print ("                |-- You have lost --|"+"\n")
                print("                Total Guesses: ",numofguesses,"of",totalguesses+"\n")
                print("                  Guesses Left: ",(int(totalguesses)-numofguesses),"\n")
                print("                  Total Errors: ",numofbadguesses,"\n"+'-'*50+"\n")
                print("            Press Enter to continue")
                input()
                UI()
            
            elif int(guess) < n:
                numofguesses=numofguesses+1
                print ("                  |-- Go higher --| "+"\n")
                print("               Total Guesses: ",numofguesses,"of",totalguesses,"\n")
                print("                  Guesses Left: ",(int(totalguesses)-numofguesses),"\n"+'-'*50+"\n")
                if (int(totalguesses)-numofguesses)==0:
                    print ("                |-- You have lost --|"+"\n")
                    print("               Total Guesses: ",numofguesses,"of",totalguesses,"\n")
                    print("                  Guesses Left: ",(int(totalguesses)-numofguesses),"\n")
                    print("                  Total Errors: ",numofbadguesses,"\n"+'-'*50+"\n")               
                    print("            Press Enter to continue")
                    input()
                    UI()
                else:
                    guess = input("          Choose an integer from 1 to 200: ")
                print("\n")
            elif int(guess) > n:
                numofguesses=numofguesses+1
                print ("                  |-- Go lower --| "+"\n")
                print("                Total Guesses: ",numofguesses,"of",totalguesses,"\n")
                print("                  Guesses Left: ",(int(totalguesses)-numofguesses),"\n"+'-'*50+"\n")
                if (int(totalguesses)-numofguesses)==0:
                    print ("                |-- You have lost --|"+"\n")
                    print("               Total Guesses: ",numofguesses,"of",totalguesses,"\n")
                    print("                  Guesses Left: ",(int(totalguesses)-numofguesses),"\n")
                    print("                  Total Errors: ",numofbadguesses+'-'*50+"\n")
                    print("            Press Enter to continue")
                    input()
                    UI()
                else: 
                    guess = input("          Choose an integer from 1 to 200: ")
                    print("\n")
            else:                       
                print("                  |-- You have won! --|"+"\n"*2)
                print("             It took you",numofguesses,"out of",totalguesses,"guesses"+"\n")
                print("                    Guesses Left: ",(int(totalguesses)-numofguesses),"\n")
                print("                    Total Errors: ",numofbadguesses,"\n"+'-'*50+"\n")
                print('                Press Enter to continue ')
                input()
                UI()

        else:
            print("Unknown Error")
            guess = input("          Choose an integer from 1 to 200: ")
            
print("\n"*3)
name=(input("               Enter player name: "))              
UI()    

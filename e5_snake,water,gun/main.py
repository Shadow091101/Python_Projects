import math

def snakewatergun():
    def generatecomputerchoice():
        import random
        choice=["snake","water","gun"]
        randomindex=random.randint(0,2)
        print(randomindex)
        return choice[randomindex]
    def determinewinner(userchoice,computerchoice):
        if(userchoice==computerchoice):
            return "It is a Tie"
        elif((userchoice=='snake' and computerchoice=='water')or(userchoice=='water' and computerchoice=='gun')or(userchoice=='gun' and computerchoice=='snake')):
            return "You win!!!"
        else:
            return "Computer Wins"
    while True:
        print("Welcome to our wonderful game that is SNAKE,WATAR and GUN\n The rules are simple 'Snake' beats 'Water','Water' beats 'Gun' and 'Gun' beats 'Snake'\nSo lets get started\n")
        userint=int(input("Choose:\n '1' for Snake \t '2' for Water \t '3' for Gun \n"))
        if(userint==1):
            userchoice='snake'
        elif(userint==2):
            userchoice='water'
        elif(userint==3):
            userchoice='gun'
        if(userint!=1 and userint!=2 and userint!=3):
            print("\nError:The Value of the choice should be 1,2 or 3")
            continue
        computerchoice=generatecomputerchoice()
        result=determinewinner(userchoice,computerchoice)
        print(f"\nYour choice :{userchoice}\n Computer's Choice:{computerchoice}\n{result}")
        playagain=int(input("Do you want to play again?\n 1 for Yes \n2 for No\n"))
        if(playagain==2):
            print("*********Thanks for playing*********")
            break


    
snakewatergun()
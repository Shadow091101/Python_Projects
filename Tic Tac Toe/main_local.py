import random

def printBoard():
    print(f" {xState[0]} | {xState[1]} | {xState[2]} ")
    print("---|---|---")
    print(f" {xState[3]} | {xState[4]} | {xState[5]} ")
    print("---|---|---")
    print(f" {xState[6]} | {xState[7]} | {xState[8]} ")
    pass

class Computerplays:
    def __init__(self):
        self.wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

    # Step 1: Try to win if possible
    def Owins(self):
        # Priority 1: Win if possible
        for win in self.wins:
            values = [xState[i] for i in win]
            if values.count('O') == 2 and values.count('X') == 0:
                for i in win:
                    if xState[i] not in ['X', 'O']:
                        xState[i] = 'O'
                        print(f"Computer plays to WIN at position {i}")
                        return True

        # Priority 2: Create opportunity (1 O, 2 empty, 0 X)
        for win in self.wins:
            values = [xState[i] for i in win]
            if values.count('O') == 1 and values.count('X') == 0:
                for i in win:
                    if xState[i] not in ['X', 'O']:
                        xState[i] = 'O'
                        print(f"Computer CREATES OPPORTUNITY at position {i}")
                        return True

    # Step 2: Block X from winning
    def blokingX(self):
        for win in self.wins:
            values = [xState[i] for i in win]
            if values.count('X') == 2 and any(xState[i] not in ['X', 'O'] for i in win):
                for i in win:
                    if xState[i] not in ['X', 'O']:
                        xState[i] = 'O'
                        print(f"Computer BLOCKS X at position {i}")
                        return True

    # Step 3: Pick center if available
    def centerplacing(self):
        if xState[4] not in ['X', 'O']:
            xState[4] = 'O'
            print("Computer takes center at position 4")
            return True

    # Step 4: Pick a random available spot
    def randomplaciing(self):
        available = [i for i in range(9) if xState[i] not in ['X', 'O']]
        if available:
            move = random.choice(available)
            xState[move] = 'O'
            print(f"Computer plays randomly at position {move}")
    
        
            
    

# def winner():
#     if(
#         (xState[0]=="X" and xState[1]=="X" and xState[2]=="X") 
#        or (xState[3]=="X" and xState[4]=="X" and xState[5]=="X")
#        or (xState[6]=="X" and xState[7]=="X" and xState[8]=="X")
#        or (xState[0]=="X" and xState[3]=="X" and xState[6]=="X")
#        or (xState[1]=="X" and xState[4]=="X" and xState[7]=="X")
#        or (xState[2]=="X" and xState[5]=="X" and xState[8]=="X")
#        or (xState[0]=="X" and xState[4]=="X" and xState[8]=="X")
#        or (xState[6]=="X" and xState[2]=="X" and xState[4]=="X")): 
#         print("X is the Winner")
#         return True
#     elif((xState[0]=="O" and xState[1]=="O" and xState[2]=="O") 
#        or (xState[3]=="O" and xState[4]=="O" and xState[5]=="O")
#        or (xState[6]=="O" and xState[7]=="O" and xState[8]=="O")
#        or (xState[0]=="O" and xState[3]=="O" and xState[6]=="O")
#        or (xState[1]=="O" and xState[4]=="O" and xState[7]=="O")
#        or (xState[2]=="O" and xState[5]=="O" and xState[8]=="O")
#        or (xState[0]=="O" and xState[4]=="O" and xState[8]=="O")
#        or (xState[6]=="O" and xState[2]=="O" and xState[4]=="O")):
#         print("O is the Winner")
#         return True

def winner():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for win in wins:
        if xState[win[0]] == xState[win[1]] == xState[win[2]] == "X":
            print("\n\n")
            printBoard()
            print(f"\n{"-"*30}")
            print("X is the Winner")
            return True
        elif xState[win[0]] == xState[win[1]] == xState[win[2]] == "O":
            print("\n\n")
            printBoard()
            print(f"\n{"-"*30}")
            print("O is the Winner")
            return True
    return False

def play_with_computer():
    difficulty=int(input("\nSelect Difficulty : Enter 1 for Easy mode , Enter 2 for Medium mode and Enter 3 for Hard mode or Enter 0 to go back : "))
    turn=1
    if(difficulty==1):
        while(True):            
            print("\n")
            printBoard()
            print(f"\n{"-"*30}")
            if(turn==1):
                print("Player's Chance")
                value=int(input("Please enter a value where you want to place X given in the board : "))
                if(xState[value]!='X' and xState[value]!='O'):
                    xState[value]='X'
                    isWinner=winner()
                    if(isWinner):
                        break                    
                    turn=0
                else:
                    print("Cell already taken. Try a diffrent One")
            else:
                print("O's Chance")
                f=Computerplays()
                f.randomplaciing()
                isWinner=winner()
                if(isWinner):
                    break
                turn=1
            
            # Check for tie
            if all(isinstance(x, str) for x in xState):
                printBoard()
                print("It's a Tie!")
                break
    elif(difficulty==2):
        while(True):            
            print("\n")
            printBoard()
            print(f"\n{"-"*30}")
            if(turn==1):
                print("Player's Chance")
                value=int(input("Please enter a value where you want to place X given in the board : "))
                if(xState[value]!='X' and xState[value]!='O'):
                    xState[value]='X'
                    isWinner=winner()
                    if(isWinner):
                        break                    
                    turn=0
                else:
                    print("Cell already taken. Try a diffrent One")
            else:
                answer=False
                print("O's Chance")
                f=Computerplays()
                if not f.Owins():
                    f.randomplaciing()
                isWinner=winner()
                if(isWinner):
                    break
                turn=1

            # Check for tie
            if all(isinstance(x, str) for x in xState):
                printBoard()
                print("It's a Tie!")
                break      
    elif(difficulty==3):
        while(True):            
            print("\n")
            printBoard()
            print(f"\n{"-"*30}")
            if(turn==1):
                print("Player's Chance")
                value=int(input("Please enter a value where you want to place X given in the board : "))
                if(xState[value]!='X' and xState[value]!='O'):
                    xState[value]='X'
                    isWinner=winner()
                    if(isWinner):
                        break                    
                    turn=0
                else:
                    print("Cell already taken. Try a diffrent One")
            else:
                answer=False
                print("O's Chance")
                f=Computerplays()
                if not f.Owins():
                    if not f.blokingX():
                        if not f.centerplacing():
                            f.randomplaciing()                   
                isWinner=winner()
                if(isWinner):
                    break
                turn=1
            
            # Check for tie
            if all(isinstance(x, str) for x in xState):
                printBoard()
                print("It's a Tie!")
                break  
    elif(difficulty==0):
        return

if __name__=="__main__":    
    xState=[0,1,2,3,4,5,6,7,8]
    print("\nWelcome to Tic Tac Toe")
    while(True):
        print("\nWhat you want to choose : ")
        print("Play with Computer \t Play with Friend\n")
        choice=int(input("Enter 1 to Play with Computer , 2 to Play with Friend and Enter 3 to exit : "))
        if(choice==1):
            play_with_computer()
        elif(choice==2): 
            turn=1           
            while(True):
                printBoard()
                if(turn==1):
                    print("X's Chance")
                    value=int(input("Please enter a value where you want to place X : "))
                    if(xState[value]!='X' and xState[value]!='O'):
                        xState[value]='X'
                        isWinner=winner()
                        if(isWinner):
                            break                    
                        turn=0
                    else:
                        print("Cell already taken. Try a diffrent One")
                else:
                    print("O's Chance")
                    value=int(input("Please enter a value where you want to place O : "))
                    if(xState[value]!='O' and xState[value]!='X'):
                        xState[value]='O'
                        isWinner=winner()
                        if(isWinner):
                            break
                        turn=1
                    else:
                        print("Cell is already taken. Try a different one")
                
                # Check for tie
                if all(isinstance(x, str) for x in xState):
                    printBoard()
                    print("It's a Tie!")
                    break  
        elif(choice==3):
            exit()
            
    
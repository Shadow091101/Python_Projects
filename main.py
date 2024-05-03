questions=["What is our national animal?\n Option 1 : Lion\tOption 2:Tiger\tOption 3:Cheetah\tOption 4:Leopard\n","Which country is called as land of winds?\nOption 1 : India\tOption 2:Brazil\tOption 3:Denmark\tOption 4 : Switzerland","What is minimum age required to stand for the lok sabha election of our country?\nOption 1:20\tOption 2:30\tOption 3:35\tOption 4:25","Who gave the slogan 'Tum Mujhe Khoon do Mei Tumhe ajadi Dunga'?\nOption 1:M.K.Gandhi\tOption 2:Netaji Subash Chandra Bose\tOption 3:Bankim Chandra Chatterjee\tOption 4:Vinayak Damodar Savarkar","Which country currently has the most assets in the world?\nOption 1:Apple\tOption 2:Microsoft\tOption 3:Facebook\tOption 4:Nvidia"]

Correctanswers=["Tiger","Denmark","25","Netaji Subash Chandra Bose","Microsoft"]

money=[1000,10000,50000,5000000,10000000]
WinningAmount=0


def start():
    print("Welcome Ladies and Gentlemen for Todays Episode of 'Kaun Banega Crorepati'.\nSo our Todays Contestent is : \n")
    a=input("Enter Your Name : ")
    print("So our Today's Contestent is Mr.",a)
    b=input(("So are you ready For Today's Questions to come? 'Yes' or 'No'"))
    if b=="Yes":
       return questionsFunction()
    else:
        print("You are free to leave the game.")


def questionsFunction():
    global WinningAmount
    for i in range(len(questions)):
        print("\n\nSo Our Question No.",i+1," is \n",questions[i])
        answers=input("\n\nPlease Type The Corrected Answer as per the Options Given:")
        if answers==Correctanswers[i]:
            WinningAmount+=money[i]
            print("\n\nCongratulations You Won Ruppes",money[i],"\n Now Lets Move towards The Next Question:")
        else:
            break
    
    if WinningAmount>=10000000:
        print("\n\nLadies and gentlemen, hold your breath, for we have a winner amongst us tonight! Our contestant has just clinched the monumental sum of 1 crore rupees! What an exhilarating moment! Heartiest congratulations to you, my friend! You've not only won the game but also the hearts of millions watching across the nation! Keep shining and soaring high!")
        print("\n\nYou Played Very well Here Your Winning Amount : ",WinningAmount)
    else:
        print("\n\nYou Played Very well Here Your Winning Amount : ",WinningAmount)


start()

password="manavnaik123"
def reversestr(str):
    if len(str)==1 or len(str)==2:
        return str[::-1]
    
def randomletter():
    import random
    rand=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    random_int=random.randint(0,25)
    # print(random_int)
    randlet=rand[random_int]
    return randlet

def changestr(str):
    lst=list(str)
    # print(lst)
    pop1=lst.pop(0)
    # print(pop1)
    lst.append(pop1)
    # print(lst)
    lsttostr=''.join(lst)
    # print(lsttostr)
    for i in range(3):
        rnd=randomletter()
        # print(rnd)
        lst.insert(0,rnd)
    for i in range(3):
        rnd=randomletter()
        # print(rnd)
        lst.append(rnd)
    # print(lst)
    lsttostr=''.join(lst)
    # print(lsttostr)
    return lsttostr

def changestr1(encoded_str):
    # Remove the last three characters
    decoded_str = encoded_str[:-3]
    # Remove the first three characters
    decoded_str = decoded_str[3:]
    # Rotate the string by moving its last character to the beginning
    decoded_str = decoded_str[-1] + decoded_str[:-1]
    return decoded_str

def code():
    a = input("Enter the statement: ")

    b = a.split(" ")
    # print(b)
    endlst=[]
    for i in range(len(b)):
        # print(b[i])
        if(len(b[i]))<=2:
            revstr= reversestr(b[i])
            endlst.append(revstr)
            # print(revstr)
        else:
            chgestr=changestr(b[i])
            endlst.append(chgestr)
            
        
    # print("endlst:",endlst)
    endstr=' '.join(endlst)
    print("The coded message :",endstr)



def decode():
    a1 = input("Enter the coded message: ")
    b1=a1.split(" ")
    endlst1=[]
    for i in range(len(b1)):
        if(len(b1[i])<=2):
            revstr=reversestr(b1[i])
            endlst1.append(revstr)
        else:
            chgestr1=changestr1(b1[i])
            endlst1.append(chgestr1)
    endstr1=" ".join(endlst1)
    validate=input("Enter the Password to decode the coded message : ")
    if validate==password:
        print("The decoded message : ",endstr1)
    else:
        print("As the password was incorrect you were not allowed to decode this code due to security reason.")
        quit()
        
        

def main():   
    while True:
        print("Welcome to Coders and Decoders:")
        choice=int(input("Select what you want to do:\n 1)Code \n 2)Decode\n 3) Quit \n"))
        if(choice==1):
            code()
        if(choice==2):
            decode()
        if(choice==3):
            quit()
        confirm=input("So do you want to again Decode or code?\n Yes or No\n")
        if confirm.lower()=="yes":
            continue#i want the loop to again occur
        else:
            quit()
main()

   

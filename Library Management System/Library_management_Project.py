class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        mark="*"
        print('Books Present In the Library are :')
        for book,numberofBooks in self.books.items():
            if numberofBooks==0:
                mark="#"
            else:
                mark="*"
            print(f" {mark} {book} : {numberofBooks:02}")

    def borrowBook(self,bookName):
        self.displayAvailableBooks()
        if bookName in self.books and self.books[bookName]>0:
            self.books[bookName]-=1
            print(f"You have borrowed '{bookName}'. Remaining copies: {self.books[bookName]}")
            return True
        else:
            print(f"'{bookName}' is either not available or out of stock.")
            return False
    def returnBook(self,bookName):
        if bookName in self.books:
            self.books[bookName]+=1
            print(f"You have returned '{bookName}. Remaining copues : {self.books[bookName]}\n'")
            return True
        else:
            print(f"'{bookName}' that you are returning is not in our system.")
            return False

class Student:
    alreadyBorrowedBooks={}
    name=""
    def __init__(self,name):
        self.name=name
        if self.name not in Student.alreadyBorrowedBooks:
            Student.alreadyBorrowedBooks[self.name] = {}
    def displayBorrowedBooks(self):
        borrowed = Student.alreadyBorrowedBooks.get(self.name, {})
        if borrowed:
            print(f"\n The Books Borrowed by {self.name} are as follows : ")
            for book, number in borrowed.items():
                print(f" * {book} : {number:02}")
        else:
            print(f"\n{self.name} has 0 books.\n")
    def borrowBooks(self,library):
        bookName = input("Enter the name of the book you want to borrow : ").strip().upper()
        success = library.borrowBook(bookName)
        if success:
            if bookName in Student.alreadyBorrowedBooks[self.name]:
                Student.alreadyBorrowedBooks[self.name][bookName] += 1
            else:
                Student.alreadyBorrowedBooks[self.name][bookName] = 1

            print(f"{self.name} has borrowed: {Student.alreadyBorrowedBooks[self.name]}")
        pass
    def returnBook(self,library):
        borrowed = Student.alreadyBorrowedBooks.get(self.name, {})
        if not borrowed:
            print(f"\n{self.name} has no books to return.")
            return
        bookName=input("Enter the name of the book which you wants to return : ").strip().upper()
        success=library.returnBook(bookName)
        if success:
            if bookName in Student.alreadyBorrowedBooks[self.name] and Student.alreadyBorrowedBooks[self.name][bookName]>0:
                Student.alreadyBorrowedBooks[self.name][bookName] -= 1
                if Student.alreadyBorrowedBooks[self.name][bookName]==0:
                    del Student.alreadyBorrowedBooks[self.name][bookName]
            


if __name__=="__main__":
    centralLibrary = Library({"CN": 10, "AM": 16, "OS": 9, "TCS": 16, "MP": 12})
    student1 = Student("John")
    print("Welcome To Library Management System")
    while(True):
        print(f"\n{"-"*50}\n")
        choice=int(input("Select What You want to do :\
          \n1)Check the books in the Library \
              \n2)Display the Books that you have borrowed \
                  \n3)Borrow Books \
                  \n4)Return Book \
                      \n5)Exit \
                          \nEnter The Choice : "))
        if choice==1:                  
            centralLibrary.displayAvailableBooks()
        elif choice==2:
            student1.displayBorrowedBooks()
        elif choice==3:            
            student1.borrowBooks(centralLibrary)
        elif choice==4:
            student1.returnBook(centralLibrary)
        elif choice==5:
            exit()
        else:
            print("\n Invalid Option Choosen")
            

    # centralLibrary.displayAvailableBooks()
    
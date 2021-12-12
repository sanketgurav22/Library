
class Library:
    def __init__(self, list, name) -> None:
        self.booklist = list
        self.name = name
        self.lendDict = {}
        pass

    def displayBook(self):
        print(f"These are the Books we have in {self.name}")
        for book in self.booklist:
            print(book)
        pass

    def lendBook(self, user, book):
        if book not in self.lendDict.key():
            self.lendDict.update({book: user})
            print("Book database is update. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
        pass

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to book list")
        pass

    def returnBook(self, book):
        self.booklist.remove(book)
        pass


if __name__ == '__main__':
    sanket = Library(["Ramayan", "Mahabharat", "Mahatma Gandhi",
                      "Economics"], "Sanket Library")
    while(True):
        print(f"\t\t WELCOME TO THE {sanket.name}")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice=int(input("Enter your choice : "))

        # if user_choice  not in ['1','2','3','4']:
        #     print("Please Enter the valid option")
        #     continue
        # else:
        #     user_choice=int(user_choice)

        if user_choice==1:
            sanket.displayBook()

        elif user_choice==2:
            book=input("Enter the book name you want to lend : ")
            user=input("Enter your name : ")
            sanket.lendBook(user,book)

        elif user_choice==3:
            book=input("Enter the book you want to add : ")
            sanket.addBook(book)

        elif user_choice==4:
            book=input("Enter the name of that book which you want to return : ")
            sanket.returnBook(book)

        else:
            print("INVALID INPUT !!!!!!!!!!")

        print("Press Q to quite and C for continue : ")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()

            if user_choice2=="q":
                exit()

            elif user_choice2=="c":
                continue
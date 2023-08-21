RecordsList = [] #to save title, author, subject of books
lendDict={} #to save the borrow books

def Records():
    f = open("BookLists.txt", "r")
    for line in f:
        Member = {}
        Member[line.split(",")[0].split(":")[0]] = line.split(",")[0].split(":")[1]
        Member[line.split(",")[1].split(":")[0]] = line.split(",")[1].split(":")[1]
        Member[line.split(",")[2].split(":")[0]] = line.split(",")[2].split(":")[1]
        Member[line.split(",")[3].split(":")[0]] = line.split(",")[3].split(":")[1].replace("\n","")
        RecordsList.append(Member)

def display_books():
    global RecordsList
    RecordsList = []
    Records()
    No = 1
    print("S.no \t\t|\t\tTitle\t\t|\t\t Author \t\t|\t Subject  |  \tPublication Date")
    if len(RecordsList) > 0:
        for Record in RecordsList:
            print(f"{No} \t\t\t{Record['Title']}\t\t\t\t{Record['Author']}\t\t\t{Record['Subject']}\t\t\t{Record['Publication']}\t\t")
            No += 1        
    else:
        print("\n\t\t\tNo Book Found !!!")

def sort():
    display_books()
    x=[]                                     #to save book's name in a list
    for Record in RecordsList:
        a=Record['Title']        
        x.append(a)                                                                       
    print(f"\nBefore Sorting:{x}")
    n = len(x)                                  ##Using BubbleSort
    for i in range(n):
        for j in range(n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    print("\n________After Sorting________\n")
    for k in x:
        print(k)
        
def reserve():
    f=open("info.txt","a")
    res = input("Name Of Book You Want To Reserve?")
    nam=input("Provide Your Name:")
    f.write(f"{res}'s book Reserved By {nam}\n")
    print(f"{res}'s Book Reserved By {nam}!\n")
    f.close()
    
def renew():
    f=open("info.txt","a")
    reborrow=input("Provide Your Name To Reborrow:")
    b_nam=input("Provide Name Of The Book:")
    f.write(f"{b_nam} is renewed by {reborrow}\n")
    print(f"{b_nam} (book)is renewed by {reborrow}.\n")
    f.close()
    
def add_book():
    Title = input("Enter Title :")
    Author = input("Enter author name :")
    Subject = input("Enter subject :")
    Publication = input("Enter publication date :")
    f = open("BookLists.txt", "a")
    f.write(f"Title:{Title},Author:{Author},Subject:{Subject},Publication:{Publication}\n")
    f.close()
    print('\n')
    print("Record Added...")
    global RecordsList
    RecordsList = []
    Records()

def remove_book():
    SNo = int(input("Enter S.no of the Book: "))
    RecordsList.pop(SNo - 1)
    f = open("BookLists.txt", "w")
    for Record in RecordsList:
        f.write(f"Title:{Record['Title']},Author:{Record['Author']},Subject:{Record['Subject']},Publication:{Record['Publication']}\n")
    f.close()
    print('\n')
    print("Book Deleted...")

def update_book():
    SNo = int(input("Enter S.no of Book: "))
    print("Select a Column to Update ")
    print("\t1.Title\n\t2.Author \n\t3.Subject \n\t4.Publication date\n\t")
    option = int(input("WHAT YOU WANT? : "))
    if (option == 1):
        Title = input("Update Title : ")
        RecordsList[SNo - 1]['Title'] = Title
    elif (option == 2):
        Author = input("Update Author : ")
        RecordsList[SNo - 1]['Author'] = Author
    elif (option == 3):
        Subject = (input("Update Subject : "))
        RecordsList[SNo - 1]['Subject'] = Subject
    elif (option == 4):
        Publication = (input("Update Publication : "))
        RecordsList[SNo - 1]['Publication'] = Publication
    f = open("BookLists.txt", "w")
    for Record in RecordsList:
        f.write(f"Title:{Record['Title']},Author:{Record['Author']},Subject:{Record['Subject']},Publication:{Record['Publication']}\n")
    f.close()
    print('\n')
    print("Book Updated...")
    
def search_catalogue():
    global RecordsList
    RecordsList = []
    Records()
    No = 1
    print("Searching...")
    print("S.no | \tTitle\t|\tAuthor\t|\tSubject\t|\tPublication date")
    for Record in RecordsList:
        if Record['Title'] == Title:
            print(f"{No} \t\t{Record['Title']}\t\t{Record['Author']}\t\t{Record['Subject']}\t\t {Record['Publication']}\t\t")

def login():
    f=open("info.txt","a")
    print("\nAccount Registration\n")
    a=input("Enter Your Name:")
    b=input("Enter Your Password:")
    if len(a)>0 and len(b)>0:
        f.write(f"\nName:{a}\tPassword:{b}\n")
    else:
        print("\n\t\tRegistration Required !")
        login()

def check_out():
    global lendDict
    book = input("Enter Name Of The Book You Want To Borrow:")
    user = input("Enter Your Name:")
    if book not in lendDict.keys():
        lendDict.update({book: user})
        print("You can take the book now!")
    else:
        print(f"Book is already being used by {lendDict[book]}")

def returnBook(book):
    global lendDict
    lendDict.pop(book)
    print(f"Thank You For Returning.... {book}")
    
print("\t\t\t\tLIBRARY MANAGEMENT SYSTEM")
login()

while True:
    print('\n')
    print("'MAIN MENU'")
    print("\n\t1.Display Books\n\t2.Add Book \n\t3.Edit Book \n\t4.Remove Book\n\t5.Search Book\n\t6.Sort Book In Alphabetical Order \n\t7.Check_Out\n\t8.Return\n\t9.Reserve Book\n\t10.Renew Book\n\t0.Exit") 
    print("------------------------\n")
    option = int(input("WHAT YOU WANT? "))
    
    if (option == 1):
        display_books()
    elif (option == 2):
        add_book()
    elif (option == 3):
        update_book()
    elif (option == 4):
        remove_book()
    elif (option == 5):
        Title=input("Please provide Title of the book you want to search:")
        search_catalogue()
    elif (option == 6):
        sort()
    elif (option == 7):
        check_out()
    elif (option == 8):
        book = input("Enter the name of the book you want to return:")
        returnBook(book)
    elif (option == 9):
        reserve()
    elif (option ==10 ):
        renew()
    elif (option==0):
        print("ThankYou!")
        break

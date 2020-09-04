def borrow_book_transaction(data):
    id_of_the_book=[]
    borrowed_book =[]
    name_of_the_borrower = []
    user_entered_date = []
    
    print("BOOK   ID        BOOK NAME                  AUTHOR           QUANTITY      \tPRICE    ")
    print("\n")
    for a,books in enumerate(data):
        if books[3]!=0:
            print("   ",a,"     ","",books[0]," "*(25-len(books[0])),""," ",books[1]," "*(15-len(books[1])),"",
                  "  ",books[2]," "*(8-len(str(books[2]))),"","   ",
                  books[3]," "*(5-len(str((books[3])))),"")                #displaying the available products
            id_of_the_book.append(a)
            print("\n")
    
    first_name = input("ENTER FIRST NAME: ").upper()
    second_name = input("ENTER SECOND NAME: ").upper()
    full_name = first_name +" "+ second_name
    name_of_the_borrower.append(full_name)

    counter=0
    pick= 'y'
    while pick == 'y':
        ask = True
        while ask == True:
            result = True
            while result == True: 
                try:
                    book_id =int( input("INPUT THE ID OF THE BOOK YOU DESIRE TO BORROW? "))
                    result = False
                    if book_id in borrowed_book:
                        print("SINCE YOU HAVE NOT RETURNED THE PREVIOUS BOOK, SO SORRY!!. ")
                        result = True

                except:
                    print("INPUT VALID BOOK ID NUMBER? ")
               
            if book_id in id_of_the_book:
                    borrowed_book.append(book_id)
                    
                    ask = False
            else:
                print("MISTAKLY, YOU ENTERED THE INVALID BOOK ID NUMBER.")
                
            
        counter=counter+1
        
        if counter== 2:
            print("YOUR LIMITAIONS HAS BEEN ACHIEVED.")
            print(borrowed_book)
            pick = 'n' 
        else:
            pick = input("NOW, DO YOU WANT TO BORROW ANOTHER BOOK FROM THE STORE? (y/n)")

# billing starts from here

    grand_total=0
    j=0
    import datetime
    a=str(datetime.datetime.now().year) 
    b=str(datetime.datetime.now().month) 
    c=str(datetime.datetime.now().day)
    transaction_date = a+"-"+b+"-"+c
    d=str(datetime.datetime.now().hour) 
    e=str(datetime.datetime.now().minute) 
    f=str(datetime.datetime.now().second)
    print()
    user_intro = open("library_record.txt","a")
    for items in name_of_the_borrower:
        user_intro.write(str(items)+",")
        for numbers in borrowed_book:
            
            user_intro.write(str(numbers)+",")
            
        user_intro.write("\n")

    user_intro.close()

    user_entered_date = open("borrow_record.txt","a")
    for items in name_of_the_borrower:
        user_entered_date.write(str(items)+",")
        for items in name_of_the_borrower:
        
            user_entered_date.write(transaction_date)
        user_entered_date.write("\n")
    
    user_entered_date.close()
    
    print("###################INVOICE###################")
    print()
    print()
    print()
    bill= open(a+b+c+d+e+f+full_name+".txt","w") #writes and saves data in a text file
    bill.write("###################INVOICE###################")
    bill.write("\n")
    bill.write("\n")
    bill.write("DATE OF TRANSACTION: "+a+"-"+b+"-"+c+" TIME AT: "+d+":"+e+":"+f)
    print("DATE OF TRANSACTION: ",a,"-",b,"-",c," TIME AT: ",d,":",e,":",f)
    print()
    print()
    bill.write("\n")
    bill.write("\n")
    bill.write("NAME OF THE BORROWER IS: "+full_name)#writing borrrower name on bill
    print("NAME OF THE BORROWER IS: ",full_name)#printing borrower name
    print()
    bill.write("\n")
    bill.write("\n")
    bill.write("BookName               Author               Price")
    bill.write("\n")
    print("BookName        \t\tAuthor        \t\tPrice")
    for i in borrowed_book:
        grand_total+= data[i][3]
        data[i][2]-=1
        print(data[i][0],"               ",data[i][1],"               ",data[i][3])
        bill.write(str(data[i][0])+"               "+str(data[i][1])+"               "+str(data[i][3]))
        bill.write("\n")
    print()
    bill.write("\n")
    bill.write("\n")
    print("GRAND TOTAL AMOUNT TO BE PAID IS: "+str(grand_total))
    bill.write("GRAND TOTAL AMOUNT TO BE PAID IS: "+str(grand_total  ))
    bill.write("\n")
    bill.write("\n")
    bill.write("THANK YOU AND SEE YOU SOON AGAIN!!")
    bill.close()
    

    return data
    
 
        
    
    
  
   
     
   

def returning_books_transaction(p):
    import datetime
    id_of_the_book=[]
    book_returned =[]
    print("BOOK   ID        BOOK                      AUTHOR           QUANTITY      PRICE    ")
    print("\n")
    for a,books in enumerate(p):
        if books[3]!=0:
            print("   ",a,"     ","",books[0]," "*(25-len(books[0])),""," ",books[1]," "*(15-len(books[1])),"",
                  "  ",books[2]," "*(8-len(str(books[2]))),"","   ",
                  books[3]," "*(5-len(str((books[3])))),"") #displaying the available products
            id_of_the_book.append(a)
            print("\n")
    borrowed_namelist=[]                                                   
    nameStored_file = open("library_record.txt","r")
    lines = nameStored_file.readlines()
    
    for stored_name in lines:
        borrowed_namelist.append(stored_name.replace("\n","").split(","))
    nameStored_file.close()
    print(borrowed_namelist)
    first_name = input("ENTER FIRST NAME: ").upper()
    second_name = input("ENTER SECOND NAME: ").upper()
    full_name = first_name +" "+ second_name
    
    
    
    date_storedlist = []
    date_storedfile = open("borrow_record.txt","r")
    lines = date_storedfile.readlines()
    for stored_date in lines:
        date_storedlist.append(stored_date.replace("\n","").split(","))
    date_storedfile.close()
    
    for i in range(len(date_storedlist)):
        
        if full_name == date_storedlist[i][0]:

            string_date = date_storedlist[i][1]
            format = "%Y-%m-%d"
            datetime_object = datetime.datetime.strptime(string_date,format)
            t= datetime.datetime.today()-datetime_object
                
            counter=0
            pick= 'y'
            while pick == 'y':
                    
                result = True
                while result == True: 
                    try:
                        book_id =int( input("INPUT THE BOOK ID YOU DESIRE TO RETURN : "))
                        result = False
                        if book_id in book_returned:
                            print("HELLLO, YOU ALREADY RETURNED THIS BOOK!!")
                            result = True

                                
                                    
                    except:
                        print("INPUT VALID BOOK ID NUMBER? ")

                book_returned.append(book_id)

                counter = counter + 1

                if counter== 2:
                        print("YOU BORROWED TWO BOOKS FROM THIS LIBRARY.")
                        print(book_returned)
                        pick = 'n' 
                else:
                    pick = input("DO YOU WANT TO PROCEED FOR RETURNING ANOTHER BOOK?(y/n)")


            print("###################INVOICE###################")
            print()
            print()
            print()
            returnbill= open(full_name+".txt","w") #writes and saves data in a text file
            returnbill.write("###################INVOICE###################")
            returnbill.write("\n")
            returnbill.write("\n")
            #bill.write("Date: "+a+"/"+b+"/"+c+" Time: "+d+":"+e+":"+f)
            #print("Date: ",a,"/",b,"/",c," Time: ",d,":",e,":",f)
            print()
            print()
            returnbill.write("\n")
            returnbill.write("\n")
            returnbill.write("NAME OF THE RETURNER OF THE BOOK IS: "+full_name)#writing returner name on bill
            print("NAME OF THE RETURNER OF THE BOOK IS: ",full_name)#printing returner name
            print()
            returnbill.write("\n")
            returnbill.write("\n")
            
            returnbill.write("\n")
            returnbill.write("\n")
            print("Date : ",datetime.datetime.today())
            returnbill.write("Date : "+ str(datetime.datetime.today()))
            print()
            print()
            returnbill.write("BookName               Author               Price")
            returnbill.write("\n")
            print("BookName        \t\tAuthor        \t\tPrice")

            for i in book_returned:
                if t.days> 10:
                    total2=0
                    total2+=(t.days - 10)*0.1
                    

                    p[i][2]+=1
                    print(p[i][0],"               ",p[i][1],"               ",p[i][3])
                    returnbill.write(str(p[i][0])+"               "+str(p[i][1])+"               "+str(p[i][3]))
                    returnbill.write("\n")
                    print("The total fine is : ",total2)
                    returnbill.write("\n")
                    genius = True
                    
                
                else:
                    p[i][2]+=1
                    print(p[i][0],"               ",p[i][1],"               ",p[i][3])
                    returnbill.write(str(p[i][0])+"               "+str(p[i][1])+"               "+str(p[i][3]))
                    returnbill.write("\n")
                    
            print()
            returnbill.write("\n")
            
            returnbill.write("THANKS FOR COMING AND HAVE A GOOD DAY!!")
            returnbill.close
            break;
            
    if full_name != date_storedlist[i][0]:
        print("TOO SORRY!! NO SUCH BOOKS ARE BORROWED FROM THIS LIBRARY.")
            

    return p

        


            
    

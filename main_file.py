import reading_file
import borrow_book_transaction
import returning_books_transaction
import upgraded_file

a=reading_file.reading_file("library_stock.txt")
boolean = True
while boolean== True:
    letter = input("ENTER B or b FOR BORROW BOOK AND R or r FOR RETURN BOOK. WHAT YOU WANT TO ACT? ")
    if letter=="B" or letter=="b":
        b=borrow_book_transaction.borrow_book_transaction(a)
        l= upgraded_file.upgraded_file(b)
        boolean =False
        
    elif letter=="R" or letter=="r":
        c=returning_books_transaction.returning_books_transaction(a)
        m = upgraded_file.upgraded_file(c)
        boolean = False
        
    else:
        
        print("ENTER THE VALID ACT.")





    

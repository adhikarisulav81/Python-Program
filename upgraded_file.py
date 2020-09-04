def upgraded_file(reserve_info):

    books = []
    for i in reserve_info:
        books.append(map(str,i)) #converting the values of list into strings
    file = open("library_stock.txt","w")
    for j in books:
        file.write(",".join(j))
        file.write("\n")
    file.close()
        
        


  
    

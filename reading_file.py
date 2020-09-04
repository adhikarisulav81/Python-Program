def reading_file(a):    #defining a function to read a text file
    data =[]            #creating an empty list
    
    library_stocks = open(a,"r")
    lines = library_stocks.readlines() #changing the data of txt file into list
    for books in lines:
        data.append(books.replace("\n","").split(","))
   
    library_stocks.close()
    for i in range(len(data)):
        for j in range(len(data[i])):
           if j>1:
                data[i][j]=float(data[i][j])
    return data

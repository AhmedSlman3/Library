from Librarian import Librarian
from Book import Book
from Client import Client
client = Client
book = Book
librarian = Librarian

knew_client = []
knew_book = []

print ("Welcome to the library :\nWhat is your busnise {Client , Librarian , Book , Borrowing Order} ")
Order = input (str( "order : "))
Order= Order.lower()
if Order == "librarian" :
   print( "this is the librarians list " , librarian.librarian_list )
   print( "this is the clients list " , client.client_list)
   print( "this is the books list " , book.book_list )
   print ("do you went to add client or book ? :" )
   add = input("Add : ")
   if add == "client":
     name = input ("name : ")
     id_n = input ("id : ")
     age = input ("age : ")
     knew_client.append(name )
     knew_client.append(id_n)
     knew_client.append(age )
     client.client_list.append(knew_client)
     print(client.client_list)
   elif add == "book":
     book_n = input("Book name :")
     knew_book.append(book_n)
     book.book_list.append(knew_book)
     print (book.book_list)
elif Order == "client":
   print ( "this is the books list " , book.book_list )
elif Order == "book":
   print( "this is the books list " , book.book_list )




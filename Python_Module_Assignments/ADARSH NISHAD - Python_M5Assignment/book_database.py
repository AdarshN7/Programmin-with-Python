import sqlite3

#Creating DATABASE.
mybook=sqlite3.connect('bookstore.db')

#Creating TABLE books.
try:
    cursbook=mybook.cursor()
    cursbook.execute('''CREATE TABLE books (
                        Title  TEXT (20) PRIMARY KEY,
                        Author TEXT (20),
                        Price  REAL,
                        Copies INTEGER);
                     ''')
    print("\n\tDATABASE SUCCESFULLY CREATED\n")
except:
    print("\n\tDATABASE ALLREADY EXITS")
    mybook.rollback()

#Inserting records into table. 
try:
    cursbook=mybook.cursor()
    cursbook.execute('''INSERT INTO books
                        ( Copies,Price,Author,Title)
                      VALUES
                        (5,475,'Allen B. Drowney','think python'),
                        (6,599,'allen walker','c++'),
                        (2,460,'moriss manno','let us c'),
                        (5,335,'arijit singh','ds and algo'),
                        (4,644,'billie elish','java');
                     ''')
    mybook.commit()
    
except:
    print("\n\tDATABASE ALLREADY UPDATED\n")

#Printting all records in TABLE books.
sql="SELECT * from books"
cursbook=mybook.cursor()
cursbook.execute(sql)
record=cursbook.fetchall()
for i in record:print(i)

#Inserting new records from *user*.
ans=input("\nadd more books to database? Y/N : ")
while ans=='y' or ans=='Y':
    tl=input("input title : ")
    au=input("input author : ")
    pr=float(input("input price : "))
    cp=int(input("input copies : "))
    cursbook=mybook.cursor()
    cursbook.execute('''INSERT INTO books( Copies,Price,Author,Title)
                      VALUES(?,?,?,?);''',(cp,pr,au,tl))
    print("\n\tDATABASE SUCCESFULLY UPDATED\n")
    mybook.commit()
    ans=input("\nadd more books to database? Y/N : ")
mybook.close()

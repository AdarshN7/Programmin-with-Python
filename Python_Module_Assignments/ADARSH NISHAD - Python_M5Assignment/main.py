#main programm.
import sqlite3
mybook=sqlite3.connect('bookstore.db')

ans='y'
total=0
while ans=='y' or ans=='Y':
    bt=input("\nBook Title : ")
    sql="SELECT * from books WHERE Title='"+bt+"';"
    cursbook=mybook.cursor()
    cursbook.execute(sql)
    record=cursbook.fetchone()
    if record==None:
        print("\n*no result found*")
    else:
        print(record)
        qt=int(input("\nno. of copies : "))
        sql="SELECT Price from books WHERE Title='"+bt+"';"
        cursbook=mybook.cursor()
        cursbook.execute(sql)
        price=cursbook.fetchone()
        for i in price:
            total=total + i*qt
    ans=input("\nadd more books? Y/N : ")

print("\ntotal cost : ",total)

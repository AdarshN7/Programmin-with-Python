#*******************************************************************************************

#Parent Class BOOK.
class book:
   def _init_(self,title,author,publisher,price,copies):
      self.title    = title
      self.author   = author
      self.pulisher = publisher
      self.price    = price
      self.royalty  = 0.00
      self.copies   = copies
   def set_title(self, ti):
      self.title = ti
   def set_author(self, au):
      self.author = au 
   def set_publisher(self, pu):
      self.pulisher = pu    
   def set_price(self, pr):
      self.price = pr 
   def set_copies(self, cp):
      self.copies = cp
   def get_title(self):
      return self.title
   def get_author(self):
      return self.author
   def get_publisher(self):
      return self.pulisher
   def get_price(self):
      return self.price   
   def get_copies(self):
      return self.copies
   def royalty(self):      #method to calculate author's royalty.
      if self.copies <= 500:
         self.royalty = 0.1*self.price*self.copies
      elif self.copies > 500 and self.copies <= 1500:
         self.royalty = 0.125*self.price*(self.copies-500) +  0.1*self.price*500
      elif self.copies > 1500:
         self.royalty = 0.15*self.price*(self.copies-1500) +  0.125*self.price*1000 +  0.1*self.price*500       
      return self.royalty

#code to take input from user for class book.
'''  
b1 = book()   # b1 is the object of class book.
b1.set_title(input("input title : "))
b1.set_author(input("input author : "))
b1.set_publisher(input("input publisher : "))
b1.set_price(float(input("input price : ")))
b1.set_copies(int(input("input copies : ")))

print("\nTitle     : " , b1.get_title())
print("Author    : " , b1.get_author())
print("Publisher : " , b1.get_publisher())
print("Price     : " , b1.get_price())
print("Royalty   : {:.2f}\n".format(b1.royalty()))
'''

#***********************************************************************************************


#Child class EBOOK

class ebook(book):
   def _init_(self,title,author,publisher,price,copies,format):
      super()._init_(self,title,author,publisher,price,copies)
      self.format = format
   def set_format(self,ft):
      self.format = ft
   def get_format(self):
      return self.format
   def royalty(self):      #method to calculate author's royalty.
      if self.copies <= 500:
         self.royalty = 0.1*self.price*self.copies
      elif self.copies > 500 and self.copies <= 1500:
         self.royalty = 0.125*self.price*(self.copies-500) +  0.1*self.price*500
      elif self.copies > 1500:
         self.royalty = 0.15*self.price*(self.copies-1500) +  0.125*self.price*1000 +  0.1*self.price*500       
      return (self.royalty  - 0.12*self.royalty)

#code to take input from user for class ebook.
'''   
print("*************************************************\n class ebook")
eb1 = ebook()   # b1 is the object of class book.
eb1.set_title(input("input title : "))
eb1.set_author(input("input author : "))
eb1.set_publisher(input("input publisher : "))
eb1.set_price(float(input("input price : ")))
eb1.set_copies(int(input("input copies : ")))
eb1.set_format(input("input format(EPUB, PDF, MOBI etc) : "))

print("\nTitle     : " , eb1.get_title())
print("Author    : " , eb1.get_author())
print("Publisher : " , eb1.get_publisher())
print("format    : " , eb1.get_format())
print("Price     : " , eb1.get_price())
print("Royalty   : {:.2f}".format(eb1.royalty()))
'''
#****************************************************************************************************

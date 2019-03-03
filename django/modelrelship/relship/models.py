from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()

    class Meta:
        db_table = "Address_Info"

class Author(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.ManyToManyField(Address) #many to many with Address -- would be represented inside 3rd table

    class Meta:
        db_table = "Author_Info"

#book -- a1 a2 a3
#Book(bookName="Python",price=3202,qty=20)
class Book(models.Model):
    bookName = models.CharField(max_length=30)
    price = models.IntegerField()
    qty = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # book - Author -- 1- M
    class Meta:
        db_table = "Book_Info"

#Publisher(pname="AAA",noOfBooks=20)
class Publisher(models.Model):
    pname = models.CharField(max_length=30)
    noOfBooks = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE) # publisher - Address -- 1-1
    books = models.ForeignKey(Book, on_delete=models.CASCADE)# publisher - Book -- 1-M

    class Meta:
        db_table = "Publisher_Info"

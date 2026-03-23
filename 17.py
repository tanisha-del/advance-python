class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __del__(self):
        print("Book removed:",self.title)
class Member:
    count=0
    def __init__(self,name,mid):
        self.name=name
        self.mid=mid
        Member.count=Member.count+1

class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_book(self,title,author):
        self.books.append(Book(title,author))
    def add_member(self,name,mid):
        self.members.append(Member(name,mid))
    def remove_book(self,title):
        for i in self.books:
            if i.title==title:
                self.books.remove(i)
                del i
                break
    def show_books(self):
        for i in self.books:
            print(i.title,i.author)
lib=Library()
lib.add_book("Python","Guido")
lib.add_book("Java","James")
lib.add_book("OS","Rani")
lib.add_member("Anil",1)
lib.add_member("shil",1)
lib.add_member("mani",1)
lib.add_member("anig",1)
lib.add_member("ramaa",1)
lib.show_books()
lib.remove_book("Python")
print("total no of memebers: ",Member.count)

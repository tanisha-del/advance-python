class Post:
    count=0
    def __init__(self,text):
        self.text=text
        self.likes=0
        self.comments=[]
        Post.count+=1
    def like(self):
        self.likes+=1
    def add_comment(self,c):
        self.comments.append(c)
    def __str__(self):
        return self.text+"Likes:"+str(self.likes)+"\nComments:"+str(self.comments)
class User:
    def __init__(self,name):
        self.name=name
    def post(self,text):
        return Post(text)
u=User("Anil")
p=u.post("Hello!!!!\n")
p=u.post("hi!!!!\n")
p.like()
p.add_comment("Nice")
p.add_comment("Sweet picture!")
print(p)
print("Total posts:",Post.count)

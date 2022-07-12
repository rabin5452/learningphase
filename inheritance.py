class user:
    def __init__(self,id,username,pwd):
        self.id=id
        self.username=username
        self.pwd=pwd
    def login(self,uname,pwd1):
        if self.username==uname and self.pwd==pwd1:
            return "logged in successfully."
        return "unauthorized user:"
class teacher(user):
    def __init__(self, id, username, pwd,designation):
        super().__init__(id, username, pwd)## super calls parent class and initialize the parent class's data:
        self.designation=designation
class student(user):
    def __init__(self, id, username, pwd,facultly):
        super().__init__(id, username, pwd)
        self.faculty=facultly

t=teacher(1,"teacher","teacher","professor")
uname=input("enter your usernme:")
pwd=input("enter your password:")
print(t.login(uname,pwd))

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
        super().__init__(id, username, pwd)
        self.designation=designation
class student(user):
    def __init__(self, id, username, pwd,facultly):
        super().__init__(id, username, pwd)
        self.faculty=facultly
        
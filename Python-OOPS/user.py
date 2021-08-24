class User():
    def __init__(self, name='', passw=''):
        self.Set_Username(name)
        self.Set_Password(passw)
    
    def Set_Username(self, value):
        self.username = value
    
    def Set_Password(self, value):
        self.password = value
    
    def Get_Username(self):
        return self.username
    
    def Get_Password(self):
        return self.password

        
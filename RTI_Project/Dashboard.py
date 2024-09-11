from Login import UserLogin

class DashBoard(UserLogin):
    def __init__(self):
        super().__init__()
        self._name=""
        self._temp=""
    def Userlog(self):
        self.temp=self._username+".txt"
        userdata = open(self.temp,'r')
        for line in userdata:
            self.name = line
            break
    def start(self):
        print(f"welcome, {self.name}")
    
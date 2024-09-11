class User:
    def __init__(self):
        self.__Name=""
        self.__Username=""
        self.__password=""
    def set_Username(self,Username):
        self.Username = Username
    def set_Name(self,name):
        self.Name = name
    def set_password(self,password):
        self.password = password
    def save_Userdata(self):
        userdata = open('Userdata.txt','a')
        temp = self.Username + ".txt"
        userdata.writelines(self.Name+"\n")
        userdata.writelines(self.Username+"\n")
        userdata.writelines(self.password+"\n")
        personal_data = open(temp,'a')
        personal_data.writelines(self.Name+"\n")
        personal_data.writelines(self.password+"\n")
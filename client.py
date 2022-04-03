import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.Name.setEchoMode(QtWidgets.QLineEdit.Name)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Confirmpassword.setEchoMode(QtWidgets.QLineEdit.Confirmpassword)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("well connected")
    def userEmail(self):
        email=self.email.text()
        return email
    def userPassword(self):
            password=self.password.text()
            return password
    def userName(self):
            name=self.Name.text()
            return name
    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("user created!")
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()

import socket
import json

class Objetmail:
    def __init__(self,add_src,add_dest,obj_mail,corp_message):
        self.add_src= add_src
        self.add_dest = add_dest
        self.obj_mail = obj_mail
        self.corp_message = corp_message

host= '192.168.10.1'
port = 5566


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
try:
    client.connect((host, port))  # Connexion au server
    #Echange d'info avec le server cote client
    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)
    log=Login()
    clientInfo = []  # variable dinfo client
    nom =log.userName() 
    mail = log.userEmail() 
    mdp = log.userPassword() 
    clientInfo.append(nom)
    clientInfo.append(mail)
    clientInfo.append(mdp)
    messagesend = json.dumps(clientInfo)
    messagesend = messagesend.encode("utf8")
    client.sendall(messagesend)

    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)

except Exception as e:
    print(e)
finally:
    client.close()
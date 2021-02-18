from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
import sys
import sqlite3

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(0, 0, 1920, 1080)
win.setWindowTitle('TISA Scoreboard')


def loginin():
    if Username.text() == 'SRAA' and Password.text() == 'TISA2021':
        print('ok')
        Userlabel.hide()
        Passlabel.hide()
        Username.hide()
        Password.hide()
        Login.hide()
        NewTournament.show()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Wrong Password")
        msg.setText("Wrong Username or Password")

        x = msg.exec()

def NewTourney():
    NewTournament.hide()
    AddTeam.show()
    EditScoreboard.show()


def TeamAdd():
    AddTeam.hide()
    EditScoreboard.hide()
    EnterTeamName.show()
    Add.show()
    TeamList.show()


def AddSelected():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    newteam = EnterTeamName.text()

    c.executemany('INSERT INTO teams VALUES (?)', newteam)
    conn.commit()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    newteam = (EnterTeamName.text(),)
    query = (''' SELECT name,
                        from teams
                        WHERE name = ?
                        ''')
    c.execute(query, newteam)
    result = c.fetchall()

    TeamList.insertItem(0, result)







#login window
font = QtGui.QFont()
font.setFamily("Sitka Text")
font.setPointSize(22)
font.setBold(True)
font.setWeight(75)

fontbig = QtGui.QFont()
fontbig.setFamily("Sitka Text")
fontbig.setPointSize(24)
fontbig.setBold(True)
fontbig.setWeight(77)


Userlabel = QtWidgets.QLabel(win)
Userlabel.setText("Username:")
Userlabel.setFont(font)
Userlabel.resize(230, 50)
Userlabel.move(710, 375)

Passlabel = QtWidgets.QLabel(win)
Passlabel.setText('Password:')
Passlabel.setFont(font)
Passlabel.resize(225, 50)
Passlabel.move(720, 440)

Username = QtWidgets.QLineEdit(win)
Username.setFont(font)
Username.resize(220, 50)
Username.move(950, 380)

Password = QtWidgets.QLineEdit(win)
Password.setFont(font)
Password.resize(220, 50)
Password.move(950, 450)

Login = QtWidgets.QPushButton(win)
Login.setFont(font)
Login.resize(460, 70)
Login.setText('Login')
Login.move(710, 530)
Login.clicked.connect(loginin)

#2nd window
NewTournament = QtWidgets.QPushButton(win)
NewTournament.setFont(font)
NewTournament.setText('NewTournament')
NewTournament.resize(460, 100)
NewTournament.move(710, 530)
NewTournament.hide()
NewTournament.clicked.connect(NewTourney)

#3rd window
AddTeam = QtWidgets.QPushButton(win)
AddTeam.setText('Add Teams')
AddTeam.setFont(font)
AddTeam.resize(390, 70)
AddTeam.move(710, 375)
AddTeam.hide()
AddTeam.clicked.connect(TeamAdd)

EditScoreboard = QtWidgets.QPushButton(win)
EditScoreboard.setText('Edit Scoreboard')
EditScoreboard.setFont(font)
EditScoreboard.resize(390, 70)
EditScoreboard.move(710, 450)
EditScoreboard.hide()

#add team window
EnterTeamName = QtWidgets.QLineEdit(win)
EnterTeamName.resize(350, 80)
EnterTeamName.move(700, 400)
EnterTeamName.setFont(font)
EnterTeamName.hide()

Add = QtWidgets.QPushButton(win)
Add.setText('Add Team')
Add.setFont(fontbig)
Add.resize(350, 80)
Add.move(700, 500)
Add.hide()
Add.clicked.connect(AddSelected)

TeamList = QtWidgets.QListWidget(win)
TeamList.setFont(font)
TeamList.resize(500, 600)
TeamList.move(1250, 300)
TeamList.hide()

win.show()

sys.exit(app.exec_())

# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from pygame import mixer

class Ui_MainWindow(object):

    def __init__(self):
        self.boardList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.playerTurn = 1
        self.squaresFilled = 0
        self.win = False
        self.gameOver = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 321)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 321))
        MainWindow.setMaximumSize(QtCore.QSize(300, 321))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        # cross lines --------------------------------------------------------------------------------------------------
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_1.setLineWidth(4)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setObjectName("line_1")
        self.gridLayout.addWidget(self.line_1, 2, 0, 1, 5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 5)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(4)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(4)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 1, 3, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(4)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 3, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(4)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 5, 3, 1, 1)

        # sizePolicy of pushButton -------------------------------------------------------------------------------------
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # font of pushButton -------------------------------------------------------------------------------------------
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)

        # pushButton_11 ------------------------------------------------------------------------------------------------
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 0, 1, 1)

        # pushButton_12 ------------------------------------------------------------------------------------------------
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 2, 1, 1)

        # pushButton_13 ------------------------------------------------------------------------------------------------
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 1, 4, 1, 1)

        # pushButton_21 ------------------------------------------------------------------------------------------------
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setFlat(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 3, 0, 1, 1)

        # pushButton_22 ------------------------------------------------------------------------------------------------
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setFlat(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 3, 2, 1, 1)

        # pushButton_23 ------------------------------------------------------------------------------------------------
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 3, 4, 1, 1)

        # pushButton_31 ------------------------------------------------------------------------------------------------
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setFlat(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 5, 0, 1, 1)

        # pushButton_32 ------------------------------------------------------------------------------------------------
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setFlat(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 5, 2, 1, 1)

        # pushButton_33 ------------------------------------------------------------------------------------------------
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setFlat(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_33, 5, 4, 1, 1)

        # label_Player -------------------------------------------------------------------------------------------------
        self.label_Player = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Player.sizePolicy().hasHeightForWidth())
        self.label_Player.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Player.setFont(font)
        self.label_Player.setIndent(15)
        self.label_Player.setObjectName("label_Player")
        self.gridLayout.addWidget(self.label_Player, 0, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuNew_Game = QtWidgets.QMenu(self.menuOptions)
        self.menuNew_Game.setObjectName("menuNew_Game")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRestartGame = QtWidgets.QAction(MainWindow)
        self.actionRestartGame.setObjectName("actionRestartGame")
        self.actionNewGame = QtWidgets.QAction(MainWindow)
        self.actionNewGame.setObjectName("actionNewGame")
        self.menuOptions.addAction(self.actionNewGame)
        self.menuOptions.addAction(self.actionRestartGame)
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.disableBoard()
        self.menuOptions.triggered[QtWidgets.QAction].connect(self.menuFunction)
        self.addPushButtonFuntionality()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.fillBlankpushButtons()
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNewGame.setText(_translate("MainWindow", "New Game"))
        self.actionRestartGame.setText(_translate("MainWindow", "Restart Game"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def fillBlankpushButtons(self):
        self.pushButton_11.setText(" ")
        self.pushButton_12.setText(" ")
        self.pushButton_13.setText(" ")
        self.pushButton_21.setText(" ")
        self.pushButton_22.setText(" ")
        self.pushButton_23.setText(" ")
        self.pushButton_31.setText(" ")
        self.pushButton_32.setText(" ")
        self.pushButton_33.setText(" ")
        self.label_Player.setText(" ")

    def disableBoard(self):
        self.label_Player.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_21.setDisabled(True)
        self.pushButton_22.setDisabled(True)
        self.pushButton_23.setDisabled(True)
        self.pushButton_31.setDisabled(True)
        self.pushButton_32.setDisabled(True)
        self.pushButton_33.setDisabled(True)
        self.line_1.setDisabled(True)
        self.line_2.setDisabled(True)
        self.line_3.setDisabled(True)
        self.line_4.setDisabled(True)
        self.line_5.setDisabled(True)
        self.line_6.setDisabled(True)
        self.line_7.setDisabled(True)
        self.line_8.setDisabled(True)

    def enableboard(self):
        self.label_Player.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_21.setEnabled(True)
        self.pushButton_22.setEnabled(True)
        self.pushButton_23.setEnabled(True)
        self.pushButton_31.setEnabled(True)
        self.pushButton_32.setEnabled(True)
        self.pushButton_33.setEnabled(True)
        self.line_1.setEnabled(True)
        self.line_2.setEnabled(True)
        self.line_3.setEnabled(True)
        self.line_4.setEnabled(True)
        self.line_5.setEnabled(True)
        self.line_6.setEnabled(True)
        self.line_7.setEnabled(True)
        self.line_8.setEnabled(True)
        self.label_Player.setText("Player 1\'s Turn")

    def menuFunction(self, action):
        actiontext = action.text()
        if actiontext == 'Exit':
            sys.exit()
        elif actiontext == 'Restart Game':
            self.resetGame()
            pass
        elif actiontext == 'New Game':
            self.enableboard()
            pass

    def addPushButtonFuntionality(self):
        self.pushButton_11.clicked.connect(partial(self.onButtonPush, self.pushButton_11, 0, 0))
        self.pushButton_12.clicked.connect(partial(self.onButtonPush, self.pushButton_12, 0, 1))
        self.pushButton_13.clicked.connect(partial(self.onButtonPush, self.pushButton_13, 0, 2))
        self.pushButton_21.clicked.connect(partial(self.onButtonPush, self.pushButton_21, 1, 0))
        self.pushButton_22.clicked.connect(partial(self.onButtonPush, self.pushButton_22, 1, 1))
        self.pushButton_23.clicked.connect(partial(self.onButtonPush, self.pushButton_23, 1, 2))
        self.pushButton_31.clicked.connect(partial(self.onButtonPush, self.pushButton_31, 2, 0))
        self.pushButton_32.clicked.connect(partial(self.onButtonPush, self.pushButton_32, 2, 1))
        self.pushButton_33.clicked.connect(partial(self.onButtonPush, self.pushButton_33, 2, 2))

    def onButtonPush(self, btn, row, column):
        crossOrZero = None
        turn = None
        if self.playerTurn == 1:
            crossOrZero = 'X'
            self.boardList[row][column] = 1
            turn = 2
            pass
        elif self.playerTurn == 2:
            crossOrZero = 'O'
            self.boardList[row][column] = 2
            turn = 1
            pass
        btn.disconnect()
        btn.setText(crossOrZero)
        self.squaresFilled += 1
        print(self.boardList)
        if self.squaresFilled > 4:
            self.checkWinCondition()
        if self.win == False and self.gameOver == False:
            self.playerTurn = turn
            self.label_Player.setText("Player {}\'s Turn".format(self.playerTurn))

    def checkWinCondition(self):
        self.win = self.checkRowsColumnsDiagonalsWin()
        if self.win == True:
            self.disableBoard()
            self.label_Player.setEnabled(True)
            self.label_Player.setText("Player {} wins.".format(self.playerTurn))
            self.playSound('tada.mp3')
        elif self.squaresFilled == 9 and self.win == False:
            self.gameOver = True
            self.disableBoard()
            self.label_Player.setEnabled(True)
            self.label_Player.setText("Game Over")
            print("Game Over!!")
            self.playSound('error.mp3')

    def checkRowsColumnsDiagonalsWin(self):
        # rows
        for i in range(0, 3):
            if self.boardList[i][0] != 0 and self.boardList[i][0] == self.boardList[i][1] and self.boardList[i][1] == \
                    self.boardList[i][2]:
                return True
        # columns
        for i in range(0, 3):
            if self.boardList[0][i] != 0 and self.boardList[0][i] == self.boardList[1][i] and self.boardList[1][i] == \
                    self.boardList[2][i]:
                return True
        # diagonal left to right
        if self.boardList[0][0] != 0 and self.boardList[0][0] == self.boardList[1][1] and self.boardList[1][1] == \
                self.boardList[2][2]:
            return True
        # diagonal right to left
        if self.boardList[0][2] != 0 and self.boardList[0][2] == self.boardList[1][1] and self.boardList[1][1] == \
                self.boardList[2][0]:
            return True
        return False

    def resetGame(self):
        self.__init__()
        self.enableboard()
        self.fillBlankpushButtons()
        self.addPushButtonFuntionality()
        self.label_Player.setText("Player {}\'s Turn".format(self.playerTurn))

    def playSound(self,music_file):
        mixer.init()
        mixer.music.load(music_file)
        mixer.music.play()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

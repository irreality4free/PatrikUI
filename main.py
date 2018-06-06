import sys
# Импортируем наш интерфейс из файла
from patrikUI import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from analog_plot import AnalogPlot
from time import sleep
import serial
from serial_test import serial_ports


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.refreshButton.clicked.connect(self.Refresh)
        self.ui.ConnectButton.clicked.connect(self.Connect)

        self.ui.save_Button.clicked.connect(self.SAVE)
        self.ui.next_Button.clicked.connect(self.NEXT)

        self.ui.detach_all_Button.clicked.connect(self.DetachALL)
        self.ui.detach_hands_Button.clicked.connect(self.DetachHands)
        self.ui.attach_all_Button.clicked.connect(self.AttachALL)

        self.ui.handR_min.clicked.connect(self.HandRM)
        self.ui.handR_plus.clicked.connect(self.HandRP)
        self.ui.handL_plus.clicked.connect(self.HandLP)
        self.ui.handL_min.clicked.connect(self.HandLM)

        self.ui.armL_min.clicked.connect(self.ArmLM)
        self.ui.armL_plus.clicked.connect(self.ArmLP)
        self.ui.armR_plus.clicked.connect(self.ArmRP)
        self.ui.armR_min.clicked.connect(self.ArmRM)

        self.ui.shold1L_min.clicked.connect(self.Shold1LM)
        self.ui.shold1L_plus.clicked.connect(self.Shold1LP)
        self.ui.shold1R_plus.clicked.connect(self.Shold1RP)
        self.ui.shold1R_min.clicked.connect(self.Shold1RM)

        self.ui.shold2L_min.clicked.connect(self.Shold2LM)
        self.ui.shold2L_plus.clicked.connect(self.Shold2LP)
        self.ui.shold2R_plus.clicked.connect(self.Shold2RP)
        self.ui.shold2R_min.clicked.connect(self.Shold2RM)

        self.ui.rollL_min.clicked.connect(self.RollLP)
        self.ui.rollL_plus.clicked.connect(self.RollLM)
        self.ui.rollR_plus.clicked.connect(self.RollRP)
        self.ui.rollR_min.clicked.connect(self.RollRM)

        self.ui.DrinkButton.clicked.connect(self.Drink)
        self.ui.PourButton.clicked.connect(self.Pour)
        self.ui.SelfPourButton.clicked.connect(self.SelfPour)
        self.ui.WagButton.clicked.connect(self.Wag)
        self.ui.StartButton.clicked.connect(self.Start)
        self.ui.NiceButton.clicked.connect(self.Nice)


    def Refresh(self):

        self.ui.portsWidget.clear()

        com_list = serial_ports()

        for key in com_list:
            self.ui.portsWidget.addItem(key)

    def Connect(self):
        port = self.ui.portsWidget.selectedItems()[0].text()
        rate = self.ui.rateWidget.selectedItems()[0].text()
        try:
            self.ser = serial.Serial(port, rate)
            print('connected')
        except Exception as e:
            print (e)
            print ('connection exeption')





    def SAVE(self):
        self.ser.write('m'.encode('utf-8'))
        print("SAVE")

    def NEXT(self):
        self.ser.write(','.encode('utf-8'))
        print("NEXT")

    def DetachHands(self):
        self.ser.write('3'.encode('utf-8'))
        print("DETACH Hands")

    def DetachALL(self):
        self.ser.write('1'.encode('utf-8'))
        print("DETACH All")

    def AttachALL(self):
        self.ser.write('2'.encode('utf-8'))
        print("ATTACH all")





    def HandRP(self):
        self.ser.write('b'.encode('utf-8'))
        print("HandRP")

    def HandRM(self):
        self.ser.write('n'.encode('utf-8'))
        print("HandRM")




    def HandLP(self):
        self.ser.write('q'.encode('utf-8'))
        print("HandLP")

    def HandLM(self):
        self.ser.write('w'.encode('utf-8'))
        print("HandLM")






    def ArmRP(self):
        self.ser.write('c'.encode('utf-8'))
        print("ArmRP")

    def ArmRM(self):
        self.ser.write('v'.encode('utf-8'))
        print("ArmRM")



    def ArmLP(self):
        self.ser.write('e'.encode('utf-8'))
        print("ArmLP")

    def ArmLM(self):
        self.ser.write('r'.encode('utf-8'))
        print("ArmLM")






    def Shold1RP(self):
        self.ser.write('z'.encode('utf-8'))
        print("Shold1RP")

    def Shold1RM(self):
        self.ser.write('x'.encode('utf-8'))
        print("Shold1RM")



    def Shold1LP(self):
        self.ser.write('t'.encode('utf-8'))
        print("Shold1LP")

    def Shold1LM(self):
        self.ser.write('y'.encode('utf-8'))
        print("Shold1LM")




        # COXA COMMANDS

    def Shold2RP(self):
        self.ser.write('j'.encode('utf-8'))
        print("Shold2RP")

    def Shold2RM(self):
        self.ser.write('k'.encode('utf-8'))
        print("Shold2RM")




    def Shold2LP(self):
        self.ser.write('u'.encode('utf-8'))
        print("Shold2LP")

    def Shold2LM(self):
        self.ser.write('i'.encode('utf-8'))
        print("Shold2LM")






    def RollRP(self):
        self.ser.write('g'.encode('utf-8'))
        print("RollRP")

    def RollRM(self):
        self.ser.write('h'.encode('utf-8'))
        print("RollRM")



    def RollLP(self):
        self.ser.write('o'.encode('utf-8'))
        print("RollLP")

    def RollLM(self):
        self.ser.write('p'.encode('utf-8'))
        print("RollLM")






    def NeckP(self):
        self.ser.write('a'.encode('utf-8'))
        print("NeckP")

    def NeckM(self):
        self.ser.write('s'.encode('utf-8'))
        print("NeckM")



    def HeadP(self):
        self.ser.write('d'.encode('utf-8'))
        print("HeadP")

    def HeadM(self):
        self.ser.write('f'.encode('utf-8'))
        print("HeadM")


    ##############POSES####################

    def Drink(self):
        self.ser.write('1'.encode('utf-8'))
        print("Drink")

    def SelfPour(self):
        self.ser.write('2'.encode('utf-8'))
        print("SelfPour")




    def Wag(self):
        self.ser.write('3'.encode('utf-8'))
        print("Wag")

    def Pour(self):
        self.ser.write('4'.encode('utf-8'))
        print("Pour")






    def Nice(self):
        self.ser.write('5'.encode('utf-8'))
        print("Nice")

    def Start(self):
        self.ser.write('6'.encode('utf-8'))
        print("Start")



    def Calibration(self):
        self.ser.write('calibration\n'.encode('utf-8'))
        print("Calibration")









if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
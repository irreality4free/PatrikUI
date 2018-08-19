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
        self.connected = False

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
        self.ui.head_min.clicked.connect(self.HeadM)
        self.ui.head_plus.clicked.connect(self.HeadP)

        self.ui.neck_plus.clicked.connect(self.NeckP)
        self.ui.neck_min.clicked.connect(self.NeckM)

        self.ui.DrinkButton.clicked.connect(self.Drink)
        self.ui.PourButton.clicked.connect(self.Pour)
        self.ui.SelfPourButton.clicked.connect(self.SelfPour)
        self.ui.WagButton.clicked.connect(self.Wag)
        self.ui.StartButton.clicked.connect(self.Start)
        self.ui.NiceButton.clicked.connect(self.Nice)
        self.ui.CalibrationButton.clicked.connect(self.Calibration)


    def Refresh(self):

        self.ui.portsWidget.clear()

        com_list = serial_ports()

        for key in com_list:
            self.ui.portsWidget.addItem(key)

    def Connect(self):
        try:
            port = self.ui.portsWidget.selectedItems()[0].text()
            rate = str(self.ui.comboBox.currentText())

            self.ser = serial.Serial(port, rate)
            self.connected = True
            print('connected')
        except Exception as e:
            print (e)
            print ('connection exeption')





    def SAVE(self):
        try:
            self.ser.write('m'.encode('utf-8'))
            print("SAVE")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def NEXT(self):
        try:
            self.ser.write(','.encode('utf-8'))
            print("NEXT")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def DetachHands(self):
        try:
            self.ser.write('3'.encode('utf-8'))
            print("DETACH Hands")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def DetachALL(self):
        try:
            self.ser.write('1'.encode('utf-8'))
            print("DETACH All")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def AttachALL(self):
        try:
            self.ser.write('2'.encode('utf-8'))
            print("ATTACH all")
        except Exception as e:
            print (e)
            print ('connection exeption')





    def HandRP(self):
        try:
            self.ser.write('n'.encode('utf-8'))
            print("HandRP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def HandRM(self):
        try:
            self.ser.write('b'.encode('utf-8'))
            print("HandRM")
        except Exception as e:
            print (e)
            print ('connection exeption')




    def HandLP(self):
        try:
            self.ser.write('q'.encode('utf-8'))
            print("HandLP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def HandLM(self):
        try:
            self.ser.write('w'.encode('utf-8'))
            print("HandLM")
        except Exception as e:
            print (e)
            print ('connection exeption')






    def ArmRP(self):
        try:
            self.ser.write('c'.encode('utf-8'))
            print("ArmRP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def ArmRM(self):
        try:
            self.ser.write('v'.encode('utf-8'))
            print("ArmRM")
        except Exception as e:
            print (e)
            print ('connection exeption')



    def ArmLP(self):
        try:
            self.ser.write('r'.encode('utf-8'))
            print("ArmLP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def ArmLM(self):
        try:
            self.ser.write('e'.encode('utf-8'))
            print("ArmLM")
        except Exception as e:
            print (e)
            print ('connection exeption')






    def Shold1RP(self):
        try:
            self.ser.write('z'.encode('utf-8'))
            print("Shold1RP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def Shold1RM(self):
        try:
            self.ser.write('x'.encode('utf-8'))
            print("Shold1RM")
        except Exception as e:
            print (e)
            print ('connection exeption')



    def Shold1LP(self):
        try:
            self.ser.write('y'.encode('utf-8'))
            print("Shold1LP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def Shold1LM(self):
        try:
            self.ser.write('t'.encode('utf-8'))
            print("Shold1LM")
        except Exception as e:
            print(e)
            print('connection exeption')





        # COXA COMMANDS

    def Shold2RP(self):
        try:
            self.ser.write('j'.encode('utf-8'))
            print("Shold2RP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def Shold2RM(self):
        try:
            self.ser.write('k'.encode('utf-8'))
            print("Shold2RM")
        except Exception as e:
            print (e)
            print ('connection exeption')




    def Shold2LP(self):
        try:
            self.ser.write('i'.encode('utf-8'))
            print("Shold2LP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def Shold2LM(self):
        try:
            self.ser.write('u'.encode('utf-8'))
            print("Shold2LM")
        except Exception as e:
            print (e)
            print ('connection exeption')






    def RollRP(self):
        try:
            self.ser.write('h'.encode('utf-8'))
            print("RollRP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def RollRM(self):
        try:
            self.ser.write('g'.encode('utf-8'))
            print("RollRM")
        except Exception as e:
            print (e)
            print ('connection exeption')



    def RollLP(self):
        try:
            self.ser.write('p'.encode('utf-8'))
            print("RollLP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def RollLM(self):
        try:
            self.ser.write('o'.encode('utf-8'))
            print("RollLM")
        except Exception as e:
            print (e)
            print ('connection exeption')






    def NeckP(self):
        try:
            self.ser.write('s'.encode('utf-8'))
            print("NeckP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def NeckM(self):
        try:
            self.ser.write('a'.encode('utf-8'))
            print("NeckM")
        except Exception as e:
            print (e)
            print ('connection exeption')



    def HeadP(self):
        try:
            self.ser.write('d'.encode('utf-8'))
            print("HeadP")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def HeadM(self):
        try:
            self.ser.write('f'.encode('utf-8'))
            print("HeadM")
        except Exception as e:
            print (e)
            print ('connection exeption')


    ##############POSES####################

    def Drink(self):
        try:
            self.ser.write('1'.encode('utf-8'))
            print("Drink")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def SelfPour(self):
        try:
            self.ser.write('2'.encode('utf-8'))
            print("SelfPour")
        except Exception as e:
            print (e)
            print ('connection exeption')




    def Wag(self):
        try:
            self.ser.write('3'.encode('utf-8'))
            print("Wag")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def Pour(self):
        try:
            self.ser.write('4'.encode('utf-8'))
            print("Pour")
        except Exception as e:
            print (e)
            print ('connection exeption')






    def Nice(self):
        try:
            self.ser.write('5'.encode('utf-8'))
            print("Nice")
        except Exception as e:
            print (e)
            print ('connection exeption')

    def Start(self):
        try:
            self.ser.write('6'.encode('utf-8'))
            print("Start")
        except Exception as e:
            print (e)
            print ('connection exeption')



    def Calibration(self):
        try:
            self.ser.write('calibration\n'.encode('utf-8'))
            print("Calibration")
        except Exception as e:
            print (e)
            print ('connection exeption')









if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

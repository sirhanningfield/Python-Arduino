import sys
import serial, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from design2 import Ui_MainWindow

#-------------------------------------------------------------------------------

Comport = 'COM8'
Baudrate = 9600

class WorkThread(QThread):

    def __init__(self,parent= None):
        QThread.__init__(self,parent)
        self.parent = parent
        self.wert = ""

    def run(self):

        while True:
            time.sleep(0.2)
            self.wert = str(self.parent.Buffer())
            self.emit(SIGNAL('update(QString)'),self.wert)
        return


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(lambda: self.CloseApp())
        self.ui.pushButton_5.clicked.connect(lambda: self.Connect_Arduino())
        self.ui.pushButton_8.clicked.connect(lambda: self.Connect_Arduino2())
        self.ui.pushButton_10.clicked.connect(lambda: self.CloseSerial())
        self.ui.pushButton_3.clicked.connect(lambda: self.GetPanAngle1())
        self.ui.pushButton.clicked.connect(lambda: self.GetPanAngle2())
        self.ui.pushButton_4.clicked.connect(lambda: self.GetTiltAngle1())
        self.ui.pushButton_2.clicked.connect(lambda: self.GetTiltAngle2())


    def Connect_Arduino(self):

        try:
            self.ser = serial.Serial(Comport,Baudrate, timeout=0)
            time.sleep(0.5)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_8.setEnabled(False)
            self.workThread = WorkThread(self)
            self.connect( self.workThread,SIGNAL("update(QString)"), self.dummy )
            self.workThread.start()

        except:
            print ('No Arduino found')
            sys.exit()



    def Connect_Arduino2(self):

        try:
            self.ser = serial.Serial(Comport,Baudrate, timeout=0)
            time.sleep(0.5)
            self.ui.pushButton_8.setEnabled(False)
            self.ui.pushButton_5.setEnabled(False)
            self.workThread = WorkThread(self)
            self.connect( self.workThread,SIGNAL("update(QString)"), self.dummy2)
            self.workThread.start()

        except:
            print ('No Arduino found')
            sys.exit()


    def CloseSerial(self):
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)
        self.ser.close()



    def dummy(self,text):
        self.ui.label_3.setText(str(text))

    def dummy2(self,text):
        self.ui.label_6.setText(str(text))


    def Buffer(self):
        buffer = ''
        while True:
            buffer = buffer + str(self.ser.read(self.ser.inWaiting()).strip().decode())
            time.sleep(0.05)
            if '\n' in buffer:
                lines = buffer.split('\n')
                last_received = lines.pop(0)
                buffer = '\n'.join(lines)
                break
            return buffer



    def GetPanAngle1(self):
        String1 = self.ui.lineEdit.text()
        try:
            Arduino = serial.Serial(Comport,Baudrate,timeout=0)
            time.sleep(2)
            Arduino.write(b"A")
            time.sleep(0.4)
            Arduino.write(String1.encode())
            Arduino.close()
            print("A")
            time.sleep(0.4)
            print(String1)
        except:
            print("No Arduino found")
            pass



    def GetPanAngle2(self):
        String2 = self.ui.lineEdit_2.text()
        try:
            Arduino = serial.Serial(Comport,Baudrate,timeout=0)
            time.sleep(2)
            Arduino.write(b'B')
            time.sleep(0.4)
            Arduino.write(String2.encode() )
            Arduino.close()
            print("B")
            time.sleep(0.4)
            print(String2)
        except:
            print("No Arduino found")
            pass



    def GetTiltAngle1(self):
        String3 = self.ui.lineEdit_5.text()

        try:
            Arduino = serial.Serial(Comport,Baudrate,timeout=0)
            time.sleep(2)
            Arduino.write(b"C")
            time.sleep(0.4)
            Arduino.write(String3.encode())
            Arduino.close()
            print("C")
            time.sleep(0.4)
            print(String3)
        except:
            print("No Arduino found")
            pass




    def GetTiltAngle2(self):
        String4 = self.ui.lineEdit_6.text()
        try:
            Arduino = serial.Serial(Comport,Baudrate,timeout=0)
            time.sleep(2)
            Arduino.write(b"D")
            time.sleep(0.4)
            Arduino.write(String4.encode())
            Arduino.close()
            print("D")
            time.sleep(0.4)
            print(String4)
        except:
            print("No Arduino found")
            pass



    def CloseApp(self):
        option = QMessageBox.question(self,'Quit?',"Are you sure you want to Quit?", QMessageBox.Yes | QMessageBox.No)
        if option == QMessageBox.Yes:
            sys.exit()
        else:
            pass




def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

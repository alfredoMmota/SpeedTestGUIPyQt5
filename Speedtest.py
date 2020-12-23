import style
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout, QLabel,QLineEdit,QPushButton
from pyspeedtest import SpeedTest


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 250)
        self.setWindowTitle("SpeedTest")
        self.setStyleSheet(style.style)
        grid_layout = QGridLayout()
        
        self.label_download = QLabel("Download ")
        self.label_upload = QLabel("Upload ")
        self.label_ping = QLabel("Ping")
        self.label_complete = QLabel()
        
        self.text_download = QLineEdit()
        self.text_upload = QLineEdit()     
        self.text_ping = QLineEdit()
        
        self.button_iniciar = QPushButton("Iniciar")
        self.button_iniciar.clicked.connect(self.getTest)
        
        grid_layout.addWidget(self.label_download, 0, 0)
        grid_layout.addWidget(self.text_download, 0, 1)
        grid_layout.addWidget(self.label_upload, 1, 0)
        grid_layout.addWidget(self.text_upload, 1, 1)
        grid_layout.addWidget(self.label_ping, 2, 0)
        grid_layout.addWidget(self.text_ping, 2, 1)
        grid_layout.addWidget(self.label_complete,3,0,1,2)
        grid_layout.addWidget(self.button_iniciar,4,0,1,2)
        self.setLayout(grid_layout)
    
    def getTest(self):
        try:
            st = SpeedTest()
            down_test = int(st.download()//pow(10,6))
            uplo_test = int(st.upload()//pow(10,6))
            ping_test = int(st.ping())
            self.text_download.setText(f"{down_test} Mbps")
            self.text_upload.setText(f"{uplo_test} Mbps")
            self.text_ping.setText(f"{ping_test} MS")
            self.label_complete.setText("¡SPEED TEST COMPLETE!")
        except Exception as ex:
            self.label_complete.setText(str(ex))          
        
        
        
        
#EJECUTAMOS APLICACIÓN.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_speed = App()
    app_speed.show()
    sys.exit(app.exec_())
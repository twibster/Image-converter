from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import sys

formats = ['JPG','JPEG','TIFF','PNG','BMB','DIB','EPS','GIF','ICNS','ICO','IM','JPEG 2000'\
           ,'MSP','PCX','PPM','SGI','SPIDER','TGA','WebP','XBM','PALM','PDF']

class MyWindow(QMainWindow):
    def __init__(self):
        '''Initiates the main program'''

        super(MyWindow,self).__init__()
        self.initUI()
        self.setGeometry(200,200,520,334)
        self.setWindowTitle('Image Converter')

    def initUI(self):
        '''Creates controls such as buttons'''

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Select your image")
        self.label.setGeometry(170,30,151,31)

        self.formate_label = QtWidgets.QLabel(self)
        self.formate_label.setText("Format")
        self.formate_label.setGeometry(190,115,151,31)

        self.browser = QtWidgets.QPushButton(self)
        self.browser.setText("Browse")
        self.browser.setGeometry(290,80,101,31)
        self.browser.clicked.connect(self.browsefiles)

        self.converter =QtWidgets.QPushButton(self)
        self.converter.setText("Convert")
        self.converter.setGeometry(140,190,171,61)
        self.converter.clicked.connect(self.convertimg)

        self.filename = QtWidgets.QLineEdit(self)
        self.filename.setGeometry(80,80,211,31)

        self.formats = QtWidgets.QComboBox(self)
        self.formats.setGeometry(170,140,101,22)
        self.formats.addItems(formats)

    def browsefiles(self):
        '''Starts the images browser'''

        global path,original,name
        fname = QFileDialog.getOpenFileName(self,'Open file',r"C:","Images (*.png \
        *.xmp *.jpeg *.tiff *.bitmap *.jpg *.bmb *.dib *.eps *.icns *.ico *.Webp\
        *.tga *.psd)")

        self.filename.setText(fname[0])

        if fname[0] != '':      #Checks for no inputs
            path =fname[0]
            name = path.split('/')[-1].split('.')[0]
            original = Image.open(path)
            if original.mode != 'RGB':     #fixes the jpeg format bug
                original = original.convert('RGB')

            self.label.setText("Image Selected")

    def convertimg(self):
        '''Converts to the requested format'''
        try:
            format = self.formats.currentText()
            original.save('{}.{}'.format(name,format.lower()))
            self.label.setText("Image Saved in the same directory of the program")
            self.label.move(130,30)
            self.label.adjustSize()
        except NameError:
            pass

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

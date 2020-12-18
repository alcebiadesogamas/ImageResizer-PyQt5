import sys
from novo.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap #manipular a imagem

class ImageResizer(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.openImage)
        self.btnResize.clicked.connect(self.resizeImagem)
        self.btnSave.clicked.connect(self.saveNewImage)
    def openImage(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open Image',
            r'..\Imagens',
            #options=QFileDialog.DontUseNativeDialog
        )
        self.inputOpenFile.setText(image)
        self.original_img =QPixmap(image)
        self.lblImagem.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))
    def resizeImagem(self):
        width = int(self.inputWidth.text())
        self.newImage = self.original_img.scaledToWidth(width)
        self.lblImagem.setPixmap(self.newImage)
        self.inputWidth.setText(str(self.newImage.width()))
        self.inputHeight.setText(str(self.newImage.height()))
    def saveNewImage(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'..\Imagens',
            #options=QFileDialog.DontUseNativeDialog
        )
        self.newImage.save(image, 'PNG')
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = ImageResizer()
    app.show()
    qt.exec_()

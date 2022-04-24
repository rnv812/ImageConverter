import sys
from PIL import Image
import pillow_avif
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.images_area: QtWidgets.QLabel = self.images_area
        self.formats_combobox: QtWidgets.QComboBox = self.formats_combobox
        self.convert_button: QtWidgets.QPushButton = self.convert_button

        self.convert_button.clicked.connect(self.convert_images)

        self.setWindowTitle("Image Converter")
        self.setWindowIcon(QIcon('icon.png'))

        self.POSSIBLE_FORMATS = ['jpg', 'avif', 'bmp', 'ico', 'png', 'tiff', 'webp']
        self.dropped_images_paths = []

        self.set_init_state()

    def set_init_state(self):
        self.images_area.setText("Drop images here")
        self.images_area.setStyleSheet('''
            QLabel{
                border: 2px dashed #222222
            }
        ''')
        self.setAcceptDrops(True)
        self.convert_button.setDisabled(True)
        self.formats_combobox.addItems(self.POSSIBLE_FORMATS)

    def set_prepared_state(self):
        self.images_area.setText(f"{len(self.dropped_images_paths)} item(s) loaded")
        self.convert_button.setEnabled(True)

    def set_process_state(self):
        self.images_area.setText("In process...")
        self.images_area.setStyleSheet('QLabel{}')
        self.setAcceptDrops(False)
        self.convert_button.setDisabled(True)

    def set_ready_state(self):
        self.images_area.setText("Done")
        self.images_area.setStyleSheet('''
            QLabel{
                border: 2px dashed #222222
            }
        ''')
        self.setAcceptDrops(True)
        self.convert_button.setDisabled(True)
        self.dropped_images_paths.clear()

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.dropped_images_paths.append(url.toLocalFile())
            event.accept()
            self.set_prepared_state()
        else:
            event.ignore()

    def convert_images(self):
        self.set_process_state()
        output_format = self.formats_combobox.currentText()
        for path in self.dropped_images_paths:
            try:
                img = Image.open(path).convert('RGB')
                img.save(f'{path.rsplit(".", 1)[0]}.{output_format}')
            except Exception as e:
                self.show_critical_message(e)
        self.set_ready_state()

    @staticmethod
    def show_critical_message(e: Exception):
        message = QMessageBox()
        message.setWindowIcon(QIcon('icon.png'))
        message.setWindowTitle("Warning")
        message.setIcon(QMessageBox.Warning)
        message.setText("Warning")
        message.setInformativeText(str(e).capitalize())
        message.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

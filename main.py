import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic.properties import QtGui
from composer import compressor, decompressor

file_name = ''

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 500, 250)
    win.setWindowTitle("COMPRESSOR")

# TEXT1
    lbl_file = QtWidgets.QLabel(win)
    lbl_file.setText('Enter Text File ')
    lbl_file.move(200, 0)

# TEXT2
    lbl_destination = QtWidgets.QLabel(win)
    lbl_destination.setText('Enter Destination')
    lbl_destination.move(190, 80)

# BOX1
    file_name = QtWidgets.QLineEdit(win)
    file_name.move(200, 40)

# BOX2
    dest_name = QtWidgets.QLineEdit(win)
    dest_name.move(200, 120)

# BUTTON COMPRESS
    btn_comp = QtWidgets.QPushButton(win)
    btn_comp.setText('COMPRESS')
    btn_comp.move(150, 180)

# BUTTON DECOMPRESS
    btn_dec = QtWidgets.QPushButton(win)
    btn_dec.setText('DECOMPRESS')
    btn_dec.move(270, 180)



# CLICKING
    def clicked_decomp(self):
        print('clicked decomposer')

        input_file_name = file_name.text()
        file_object = open(input_file_name, 'r')

        output_file_name = dest_name.text()
        output_file = open(output_file_name, 'w')

        for line in file_object:
            print(line)
            output_file.write(decompressor(line))

        file_object.close()
        output_file.close()




    def clicked_comp(self):
        print('clicked compressor')

        input_file_name = file_name.text()
        file_object = open(input_file_name, 'r')

        output_file_name = dest_name.text()
        output_file = open(output_file_name, 'w')

        for line in file_object:
            output_file.write(compressor(line))

        file_object.close()
        output_file.close()

    btn_comp.clicked.connect(clicked_comp)
    btn_dec.clicked.connect(clicked_decomp)
    win.show()
    sys.exit(app.exec())

window()
import sys
from PySide6.QtWidgets import QApplication
from mainwindow import Aplikasi_Forensik

app = QApplication(sys.argv)
w = Aplikasi_Forensik(app)
w.show()
app.exec()

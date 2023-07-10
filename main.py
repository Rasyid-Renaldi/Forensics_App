import sys
from PySide6.QtWidgets import QApplication
from mainwindow import Aplikasi_Forensik

app = QApplication(sys.argv) # membuat instance objek QApplication dengan menggunakan argumen sys.argv.
w = Aplikasi_Forensik(app) # membuat instance objek Aplikasi_Forensik dengan mengirimkan objek app sebagai argumen konstruktor.
w.show() # memanggil method show() pada objek w untuk menampilkan window aplikasi forensik.
app.exec() # menjalankan eksekusi utama aplikasi PySide6. Ini akan mengaktifkan kinerja GUI dan menunggu interaksi pengguna sampai aplikasi ditutup.

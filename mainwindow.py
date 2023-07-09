from PySide6.QtCore import QStringListModel
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QGraphicsDropShadowEffect
import enum
from pytesseract import pytesseract
from PIL import Image

from main_ui import Ui_Aplikasi_Forensik
from splash_screen_ui import Ui_SplashScreen


# * Mendefinisikan kelas enumerasi OS (Operating System) yang memiliki satu anggota yaitu Windows dengan nilai 1
class OS(enum.Enum):
    Windows = 1

# * Mendefinisikan kelas enumerasi Language yang memiliki satu anggota yaitu IND dengan nilai 'ind'
class Language(enum.Enum):
    IND = 'ind'

# * class untuk menampung sinyal, slot dan fungsi yang berinteraksi dengan antarmuka
class Aplikasi_Forensik (QMainWindow, Ui_Aplikasi_Forensik):
    # adalah konstruktor kelas yang diinisialisasi ketika objek kelas dibuat. Method ini menerima parameter app yang digunakan untuk menyimpan aplikasi utama.
    def __init__(self, app):
        # memanggil konstruktor dari kelas parent untuk melakukan inisialisasi dasar dari kelas saat ini.
        super().__init__()
        # merupakan method untuk mengatur tampilan antarmuka pengguna (UI) menggunakan Qt Designer.
        self.setupUi(self)
        # menyimpan objek aplikasi utama ke dalam atribut self.app.
        self.app = app
        # menginisialisasi atribut self.text_file_path dengan None.
        self.text_file_path = None

        # menghubungkan sinyal currentIndexChanged dari widget self.detectDevice ke method dialog_connect().
        self.detectDevice.currentIndexChanged.connect(self.dialog_connect)
        # menghubungkan sinyal clicked dari tombol self.extractButton ke method start_extract_image().
        self.extractButton.clicked.connect(self.start_extract_image)

        # menghubungkan sinyal triggered dari aksi self.actionAbout_App ke method about().
        self.actionAbout_App.triggered.connect(self.about)
        # menghubungkan sinyal triggered dari aksi self.actionAbout_QT ke method aboutQt().
        self.actionAbout_QT.triggered.connect(self.aboutQt)

        # menghubungkan sinyal clicked dari tombol self.searchFile ke method search_button().
        self.searchFile.clicked.connect(self.search_button)
        # menghubungkan sinyal clicked dari tombol self.browse ke method save_locations().
        self.browse.clicked.connect(self.save_locations)

        # menghubungkan sinyal clicked dari tombol self.scanButton ke method dialog_scan().
        self.scanButton.clicked.connect(self.dialog_scan)
        # menghubungkan sinyal clicked dari tombol self.checkButton ke method check_button().
        self.checkButton.clicked.connect(self.check_button)

        # membuat objek QStringListModel dan menyimpannya dalam atribut self.activity_model.
        self.activity_model = QStringListModel()
        # mengatur model data self.activity_model pada self.viewData, yang merupakan sebuah widget untuk menampilkan daftar aktivitas.
        self.viewData.setModel(self.activity_model)

        # menghubungkan sinyal clicked dari tombol self.okButton ke method exit().
        self.okButton.clicked.connect(self.exit)

    # * Fungsi untuk menampilkan informasi tentang aplikasi
    def about(self):
        QMessageBox.information(
            self, "Aplikasi Forensik", "Aplikasi ini hanya bisa digunakan untuk kepentingan akuisisi data!")

    # * Fungsi untuk menampilkan informasi tentang QT
    def aboutQt(self):
        QApplication.aboutQt()

    # * Menentukan smartphone yang akan digunakan
    def dialog_scan(self):
        scan = QMessageBox.question(
            self, "Scan Smartphone", "Ingin melakukan Scan Handphone Anda ?")  # menampilkan kotak dialog QMessageBox.question() dengan judul "Scan Smartphone" dan pesan "Ingin melakukan Scan Handphone Anda?".
        # memeriksa apakah pengguna memilih opsi "Yes" pada kotak dialog QMessageBox. Jika ya, maka blok kode berikutnya akan dieksekusi.
        if scan == QMessageBox.Yes:
            # mengambil teks yang dipilih oleh pengguna dari widget self.detectDevice dan menyimpannya dalam variabel selected_item.
            selected_item = self.detectDevice.currentText()
            # variabel self.circular menginisialiasi class SplashScreen untuk menampilkan progresbar
            self.circular = SplashScreen()
            self.circular.progress  # variabel self.circular memanggil method progres
            # variabel self.circular memanggil method progressBarValue
            self.circular.progressBarValue

            # memeriksa apakah nilai selected_item sama dengan teks yang ada pada indeks ke-2 dari widget self.detectDevice. Jika ya, maka blok kode berikutnya akan dieksekusi.
            if selected_item == self.detectDevice.itemText(2):
                # menampilkan hasil atau status scan.
                self.result.setText("Not Root!")
            # akan dieksekusi jika nilai selected_item tidak sama dengan teks yang ada pada indeks ke-2 dari widget self.detectDevice.
            else:
                # mengambil teks yang dipilih oleh pengguna dari widget self.detectDevice dan menyimpannya dalam variabel selected_item.
                selected_item = self.detectDevice.currentText()
                # menampilkan hasil atau status scan.
                self.result.setText("Root!")
        else:  # akan dieksekusi jika pengguna memilih opsi "No" pada kotak dialog.
            print("No")  # mencetak "No" ke konsol.

    # * Fungsi cek smartphone agar dilakukan scan terlebih dahulu
    def check_button(self):
        # menyimpan objek QMessageBox dan disimpan kedalam variabel dlg.
        dlg = QMessageBox()
        # mengatur judul dialog dlg menjadi "Check Smartphone".
        dlg.setWindowTitle("Check Smartphone")
        # mengatur teks pesan pada dialog dlg menjadi "Silakan lakukan scan Smartphone anda terlebih dahulu!".
        dlg.setText("Silakan lakukan scan Smartphone anda terlebih dahulu !")
        # mengatur tombol-tombol standar yang akan ditampilkan pada dialog dlg dan menampilkan tombol "Yes" dan "No".
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # mengatur tombol default yang akan ditekan jika pengguna menekan tombol "Enter" pada keyboard
        dlg.setDefaultButton(QMessageBox.No)

        # menampilkan dialog dlg dan menyimpan hasil tombol yang diklik oleh pengguna dalam variabel button_clicked.
        button_clicked = dlg.exec_()
        # Baris dibawah ini memeriksa apakah pengguna mengklik tombol "Yes" pada dialog. Jika ya, maka blok kode berikutnya akan dieksekusi.
        if button_clicked == QMessageBox.Yes:
            print("Ok")  # mencetak "Ok" ke konsol.
        else:  # akan dieksekusi jika pengguna memilih tombol "No" pada dialog.
            print("No")  # mencetak "No" ke konsol.

    # * Fungsi untuk membuka folder penyimpanan file image
    def search_button(self):
        search = QFileDialog.getOpenFileName(
            self, "Open File", "D:\Skripsi", "JPG files (*.jpg)")  # digunakan untuk memilih file gambar dengan ekstensi JPG pada folder Skripsi.
        # digunakan untuk menampilkan lokasi file gambar yang dipilih.
        self.search.setText(search[0])
        # memanggil method add_activity() untuk ditambahkan ke dalam daftar aktivitas atau keterangan.
        self.add_activity("Path gambar: {}".format(search[0]))

    # * Menentukan folder penyimpanan hasil extract file image
    def save_locations(self):
        selected_location = QFileDialog.getSaveFileName(
            self, "Save File", "D:\Skripsi", "TXT files (*.txt)")  # meminta pengguna untuk memilih lokasi dan nama file yang akan disimpan.
        # mengatur teks menjadi nilai path (lokasi) file yang dipilih oleh pengguna dan digunakan untuk menampilkan lokasi file tersebut.
        self.browseLocation.setText(selected_location[0])
        # mengatur nilai self.text_file_path dan digunakan untuk menyimpan informasi lokasi file yang akan digunakan dalam proses lain.
        self.text_file_path = selected_location[0]
        # memanggil method add_activity() untuk ditambahkan ke dalam daftar aktivitas atau keterangan.
        self.add_activity("Path penyimpanan: {}".format(selected_location[0]))

    # * Fungsi untuk koneksi smartphone dengan aplikasi forensik
    def dialog_connect(self):
        connect = QMessageBox.question(
            self, "Connect Smartphone", "Ingin melakukan Connect perangkat ini ?")  # menampilkan kotak dialog QMessageBox.question() dan disimpan dalam variabel connect.
        # mengatur teks pada widget self.result menjadi "Not Root!".
        self.result.setText("Not Root!")
        # memeriksa apakah pengguna memilih opsi "Yes" pada kotak dialog QMessageBox. Jika ya, maka blok kode berikutnya akan dieksekusi.
        if connect == QMessageBox.Yes:
            # mengambil teks yang dipilih oleh pengguna dari widget self.detectDevice dan menyimpannya dalam variabel selected_item.
            selected_item = self.detectDevice.currentText()
            # mencetak nilai dari selected_item ke konsol.
            print(selected_item)
            # membuat objek QMessageBox baru dengan menggunakan objek self sebagai parent.
            dlg = QMessageBox(self)
            # mengatur teks pesan pada dlg menjadi "Berhasil terkoneksi dengan perangkat".
            dlg.setText('Berhasil terkoneksi dengan perangkat')
            # menampilkan kotak dialog dlg dan menyimpan hasil tombol yang diklik oleh pengguna dalam variabel btn.
            btn = dlg.exec_()
            # memeriksa apakah pengguna mengklik tombol "Ok" pada kotak dialog. Jika ya, maka blok kode berikutnya akan dieksekusi.
            if btn == QMessageBox.Ok:
                print('OK')  # mencetak "Ok" ke konsol.
        else:  # akan dieksekusi jika pengguna memilih tombol "No" pada dialog.
            print("No")  # mencetak "No" ke konsol.

    # * Memanggil fungsi extract_image_to_text() dan Menambahkan kegiatan ke dalam model activity_model (keterangan)
    # * Memulai animasi progressBar acquisitionBar dengan menggunakan QPropertyAnimation.
    def start_extract_image(self):
        # mengatur status tombol extractButton menjadi tidak aktif (disabled) dengan memanggil method setEnabled(False)
        self.extractButton.setEnabled(False)
        # dilakukan untuk menghindari ekstraksi gambar lebih dari satu kali saat proses sedang berlangsung.
        # menambahkan kegiatan atau aktivitas baru ke dalam suatu daftar aktivitas.
        self.add_activity("======= Mengubah gambar menjadi teks =======")
        # menambahkan pesan yang berisi jalur (path) gambar yang diambil dari teks yang dimasukkan oleh pengguna melalui self.search.
        self.add_activity("Path gambar: {}".format(self.search.text()))
        # menambahkan pesan yang berisi jalur (path) penyimpanan yang diperoleh dari variabel self.text_file_path menggunakan method add_activity().
        self.add_activity("Path penyimpanan: {}".format(self.text_file_path))
        # menambahkan pesan yang berisi nama examiner yang diperoleh dari teks yang dimasukkan oleh pengguna melalui self.lineEdit.
        self.add_activity("Nama examiner: {}".format(self.lineEdit.text()))
        # menambahkan pesan yang berisi lokasi file output yang diperoleh dari variabel self.text_file_path menggunakan method add_activity().
        self.add_activity("Lokasi file output: {}".format(self.text_file_path))

        # membuat objek animasi (animation) menggunakan kelas QPropertyAnimation dengan memasukkan widget self.acquisitionBar dan properti value sebagai argumen.
        animation = QPropertyAnimation(self.acquisitionBar, b"value")
        # mengatur durasi animasi menjadi 3000 milidetik (3 detik).
        animation.setDuration(3000)
        animation.setStartValue(0)  # mengatur nilai awal animasi menjadi 0.
        animation.setEndValue(100)  # mengatur nilai akhir animasi menjadi 100.
        # menghubungkan sinyal finished dari animasi dengan method extract_image_to_text().
        animation.finished.connect(self.extract_image_to_text)
        animation.start()  # memulai animasi.

        # secara langsung memanggil method extract_image_to_text() agar method tersebut dijalankan tanpa menunggu animasi selesai.
        self.extract_image_to_text()

    # * Fungsi untuk menambahkan keterangan atau activitas
    def add_activity(self, activity):
        # inisialisasi variabel act adalah self.activity_model.stringList() dan self.activity_model merupakan objek yang menyimpan activitas
        act = self.activity_model.stringList()
        act.append(activity)  # menambahkan activitas kedalam variabel act
        # mengatur nilai dari self.activity_model dengan daftar act yang sudah diperbarui
        self.activity_model.setStringList(act)

    # * Berfungsi untuk melakukan proses ekstrak teks dari gambar
    def extract_image_to_text(self):
        # path file image dihubungkan dengan QLineEdit yang memiliki variabel self.search.text()
        image_path = self.search.text()

        if image_path and self.text_file_path:
            # inisialisasi variabel image adalah image = Image.open(image_path)
            image = Image.open(image_path)
            # path module ekstrak file image ke file text
            win_path = r'E:\Program Files\Tesseract-OCR\tesseract.exe'
            # mengkonfigurasi library pytesseract untuk menggunakan executable file Tesseract OCR yang terletak pada jalur yang diberikan oleh win_path.
            pytesseract.tesseract_cmd = win_path
            print('Run on: Windows\n')

            # inisialisasi variabel extracted_text adalah pytesseract.image_to_string(image)
            extracted_text = pytesseract.image_to_string(image)

            # nilai "w" digunakan untuk membuka file dalam mode penulisan ("write mode")
            with open(self.text_file_path, "w", encoding="utf-8") as text_file:
                # untuk menulis teks yang diekstraksi (extracted_text) ke dalam file yang telah dibuka sebelumnya dengan menggunakan objek file text_file.
                text_file.write(extracted_text)
            QMessageBox.information(
                self, "Ekstraksi Selesai", "Teks berhasil diekstrak dan disimpan dalam file teks"
            )
        else:
            QMessageBox.warning(
                self, "Error", "Mohon pilih file gambar dan lokasi penyimpanan terlebih dahulu!")

        # digunakan untuk mengaktifkan (enable) tombol yang disebut extractButton.
        self.extractButton.setEnabled(True)

    # * Fungsi keluar dari aplikasi
    def exit(self):
        self.app.exit()


# GLOBALS
# inisialisasi variabel counter dengan nilai awal 0. Variabel counter akan digunakan untuk menghitung suatu nilai dalam program.
counter = 0
# inisialisasi variabel jumper dengan nilai awal 10. Variabel jumper akan digunakan sebagai suatu nilai tetap.
jumper = 10


# definisi dari kelas SplashScreen yang merupakan turunan dari kelas QMainWindow.
class SplashScreen(QMainWindow):
    # konstruktor kelas SplashScreen yang diinisialisasi ketika objek kelas dibuat.
    def __init__(self):
        # memanggil konstruktor dari kelas parent (QMainWindow) untuk melakukan inisialisasi dasar dari kelas SplashScreen.
        QMainWindow.__init__(self)
        # membuat objek Ui_SplashScreen() dan menyimpannya dalam atribut self.ui.
        self.ui = Ui_SplashScreen()
        # memanggil method setupUi() dari objek self.ui untuk mengatur tampilan antarmuka (UI) window SplashScreen.
        self.ui.setupUi(self)

        # * Progress Bar dari nol (0)
        # memanggil hodode progressBarValue() yang merupakan method khusus yang didefinisikan dalam kelas SplashScreen untuk mengatur nilai awal dari progress bar.
        self.progressBarValue(0)
        # mengatur tipe window dengan menggunakan atribut Qt.FramelessWindowHint.
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Tipe window ini menghilangkan frame atau bingkai pada window SplashScreen, sehingga membuatnya tidak memiliki tombol close, minimize, atau maximize yang biasanya ada pada jendela standar.
        # mengatur atribut WA_TranslucentBackground dari window SplashScreen untuk memberikan efek transparansi pada latar belakang window.
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # membuat objek QGraphicsDropShadowEffect dan menyimpannya dalam atribut self.shadow.
        self.shadow = QGraphicsDropShadowEffect(self)
        # mengatur radius blur bayangan pada self.shadow menjadi 20.
        self.shadow.setBlurRadius(20)
        # mengatur posisi offset horizontal bayangan pada self.shadow menjadi 0.
        self.shadow.setXOffset(0)
        # mengatur posisi offset vertikal bayangan pada self.shadow menjadi 0.
        self.shadow.setYOffset(0)
        # mengatur warna bayangan pada self.shadow menjadi QColor(0, 0, 0, 120).
        self.shadow.setColor(QColor(0, 0, 0, 120))
        # mengatur efek bayangan yang telah dibuat (self.shadow) pada elemen grafis self.ui.circularBg.
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # * QTIMER ==> START
        # membuat objek QTimer dan menyimpannya dalam atribut self.timer. Objek QTimer digunakan untuk membuat suatu timer yang akan memicu suatu aksi atau fungsi setiap kali periode waktu tertentu berlalu.
        self.timer = QtCore.QTimer()
        # menghubungkan sinyal timeout dari objek self.timer ke method progress(), yang berarti etika timer mencapai timeout (waktu habis), method progress() akan dieksekusi.
        self.timer.timeout.connect(self.progress)
        # * TIMER IN MILLISECONDS
        # memulai timer self.timer dengan mengatur periode waktu atau interval sebesar 20 milidetik (ms), yang berarti method progress() akan dieksekusi setiap 20 ms.
        self.timer.start(20)
        # memanggil method show() untuk menampilkan jendela SplashScreen.
        self.show()

    def progress(self):
        # mendeklarasikan variabel counter sebagai variabel global, yang artinya variabel tersebut dapat diakses dan diubah nilainya di luar lingkup method progress().
        global counter
        # mendeklarasikan variabel jumper sebagai variabel global, yang artinya variabel tersebut dapat diakses dan diubah nilainya di luar lingkup method progress().
        global jumper
        # menginisialisasi variabel value dengan nilai dari variabel counter.
        value = counter
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""  # untuk memformat dan menampilkan persentase pada elemen UI dan mendefinisikan sebuah string format HTML yang mengandung placeholder {VALUE} yang akan digantikan dengan nilaijumper`.
        newHtml = htmlText.replace("{VALUE}", str(
            jumper))  # menggantikan placeholder {VALUE} dalam htmlText dengan nilai jumper yang dikonversi menjadi string. Hasilnya disimpan dalam variabel newHtml.

        # memeriksa apakah nilai value lebih besar dari jumper. Jika kondisi ini terpenuhi, maka blok kode berikutnya akan dieksekusi.
        if(value > jumper):
            # mengatur teks pada elemen label self.ui.labelPercentage dengan nilai newHtml serta digunakan untuk menampilkan persentase pada tampilan SplashScreen .
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10  # menambahkan nilai 10 ke variabel jumper.

        # * fix max value error if > than 100
        if value >= 100:  # memeriksa apakah nilai value lebih besar atau sama dengan 100. Jika kondisi ini terpenuhi, maka blok kode berikutnya akan dieksekusi.
            # mengatur nilai value menjadi 1.000 dan menunjukkan bahwa proses telah selesai.
            value = 1.000
        # memanggil method progressBarValue() dengan argumen value, untuk mengatur nilai pada progress bar.
        self.progressBarValue(value)

        if counter > 101:  # memeriksa apakah nilai counter lebih besar dari 101. Jika kondisi ini terpenuhi, maka blok kode berikutnya akan dieksekusi.
            # * STOP TIMER
            # memanggil method stop() pada objek self.timer untuk menghentikan timer.
            self.timer.stop()

            # * CLOSE SPLASH SCREEN
            # memanggil method close() pada window SplashScreen untuk menutup window.
            self.close()
        counter += 0.5  # menambahkan nilai 0.5 ke variabel counter.

    # menerima parameter value yang digunakan untuk mengatur nilai pada progress bar.
    def progressBarValue(self, value):
        # Baris dibawah ini mendefinisikan string multiline styleSheet yang berisi CSS style untuk mengatur tampilan progress bar.
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        # menghitung nilai progress berdasarkan selisih antara 100 dengan value.
        progress = (100 - value) / 100.0
        # menghitung nilai stop_1 dengan mengurangi 0.001 dari nilai progress. Nilai ini digunakan dalam stylesheet untuk mengatur titik berhenti gradient pertama pada progress bar.
        stop_1 = str(progress - 0.001)
        # mengonversi nilai progress menjadi string dan menyimpannya dalam variabel stop_2. Nilai ini digunakan dalam stylesheet untuk mengatur titik berhenti gradient kedua pada progress bar.
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)  # menggantikan placeholder {STOP_1} dan {STOP_2} dalam styleSheet dengan nilai stop_1 dan stop_2 yang telah dihitung sebelumnya. Hasilnya disimpan dalam variabel newStylesheet.
        # mengatur stylesheet newStylesheet pada elemen UI self.ui.circularProgress. Yang mana tampilan progress bar akan diperbarui sesuai dengan nilai yang diberikan.
        self.ui.circularProgress.setStyleSheet(newStylesheet)
    # ENG = 'eng'

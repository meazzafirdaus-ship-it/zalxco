from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QGroupBox, QButtonGroup, QRadioButton, QPushButton)
from random import shuffle, randint

APP = QApplication([])
JENDELA = QWidget()
JENDELA.setFixedSize(200, 200)

PERTANYAAN = QLabel("ibukota Jawa Barat adalah?")
JAWAB1 = QRadioButton("JAKARTA")
JAWAB2 = QRadioButton("BANDUNG")
JAWAB3 = QRadioButton("PURWAKARTA")
JAWAB4 = QRadioButton("SURABAYA")
GRUP_R_BTN = QGroupBox("PILIHAN JAWABAN")
TOMBOL = QPushButton("Jawab")

GRUP_HASIL = QGroupBox("HASILNYA")
BENARSALAH = QLabel("BENAR / SALAH")
JAWABAN_BENAR = QLabel("INI JAWABAN BENAR")

garis_v_grup_hasil = QVBoxLayout()
garis_v_grup_hasil.addWidget(BENARSALAH)
garis_v_grup_hasil.addWidget(JAWABAN_BENAR, alignment=Qt.AlignHCenter)
GRUP_HASIL.setLayout(garis_v_grup_hasil)

garis_v_grup_rbtn = QVBoxLayout()
garis_h1_grup_rbtn = QHBoxLayout()
garis_h2_grup_rbtn = QHBoxLayout()

garis_h1_grup_rbtn.addWidget(JAWAB1)
garis_h1_grup_rbtn.addWidget(JAWAB2)

garis_h2_grup_rbtn.addWidget(JAWAB3)
garis_h2_grup_rbtn.addWidget(JAWAB4)

garis_v_grup_rbtn.addLayout(garis_h1_grup_rbtn)
garis_v_grup_rbtn.addLayout(garis_h2_grup_rbtn)

GRUP_R_BTN.setLayout(garis_v_grup_rbtn)

garis_v_jendela = QVBoxLayout()
garis_v_jendela.addWidget(PERTANYAAN, alignment=Qt.AlignHCenter)
garis_v_jendela.addWidget(GRUP_R_BTN)
garis_v_jendela.addWidget(TOMBOL)
JENDELA.setLayout(garis_v_jendela)

kelompok_radio = QButtonGroup()
kelompok_radio.addButton(JAWAB1)
kelompok_radio.addButton(JAWAB2)
kelompok_radio.addButton(JAWAB3)
kelompok_radio.addButton(JAWAB4)

class Question:
    def __init__(self, soal, benar, salah1, salah2, salah3):
        self.soal = soal
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3

LIST_SOAL = list()
LIST_SOAL.append(Question("HARI INI SAYA MAKAN APA?", "BAKSO", "MIE", "NASGOR", "SATE"))
LIST_SOAL.append(Question("HARI INI SAYA PAKE BAJU WARNA APA?", "BIRU", "MERAH", "KUNING", "HIJAU"))
LIST_SOAL.append(Question("HARI INI SAYA MAU PERGI KEMANA?", "TAMAN BERMAIN", "MALL", "MONAS", "ZOO"))
LIST_SOAL.append(Question("HARI LAHIR PANCASILA DIPERINGATI SETIAP TANGGAL?", "1 JUNI", "2 AGUSTUS", "15 JANUARI", "25 SEPTEMBER"))
LIST_SOAL.append(Question("IBUKOTA PROVINSI JAWA TIMUR ADALAH?", "SURABAYA", "BANDUNG", "BOGOR", "PONTIANAK"))

JENDELA.total_soal = 0
JENDELA.total_benar = 0
def show_result():
    GRUP_R_BTN.hide()
    GRUP_HASIL.show()
    TOMBOL.setText("PERTANYAAN BERIKUTNYA")

def show_question():
    GRUP_R_BTN.show()
    GRUP_HASIL.hide()
    TOMBOL.setText("JAWAB")
    kelompok_radio.setExclusive(False)
    JAWAB1.setChecked(False)
    JAWAB2.setChecked(False)
    JAWAB3.setChecked(False)
    JAWAB4.setChecked(False)
    kelompok_radio.setExclusive(True)

def ok():
    if TOMBOL.text() == "JAWAB":
        # show_result()
        check_answer()
    else:
        # show_question()
        next_question()

LIST_RADIO = [JAWAB1, JAWAB2, JAWAB3, JAWAB4]
def ask(objek_soal):
    shuffle(LIST_RADIO)
    LIST_RADIO[0].setText(objek_soal.benar)
    LIST_RADIO[1].setText(objek_soal.salah1)
    LIST_RADIO[2].setText(objek_soal.salah2)
    LIST_RADIO[3].setText(objek_soal.salah3)
    PERTANYAAN.setText(objek_soal.soal)
    JAWABAN_BENAR.setText(objek_soal.benar)
    show_question()

def check_answer():
    if LIST_RADIO[0].isChecked():
        BENARSALAH.setText("BENARR")
        JENDELA.total_benar += 1
    else:
        BENARSALAH.setText("SALAHH")
    show_result()
    print("=================")
    print("TOTAL BENAR =", JENDELA.total_benar)
    print("PERSENTASE =", (JENDELA.total_benar / JENDELA.total_soal) * 100, "%")
    print("=================")

def next_question():
    JENDELA.total_soal += 1
    print("================")
    print("TOTAL SOAL =", JENDELA.total_soal)
    print("================")
    counter = randint(0, len(LIST_SOAL)-1)
    ask(LIST_SOAL[counter])

#JENDELA.counter = -1
#def next_question():
   # JENDELA.counter +=1
    #JENDELA.counter = 0
    #ask(LIST_SOAL[JENDELA.counter])

next_question()

TOMBOL.clicked.connect(ok)

GRUP_R_BTN.hide()
GRUP_HASIL.show()

JENDELA.show()
APP.exec_()
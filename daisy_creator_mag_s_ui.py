# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daisy_creator_mag_s.ui'
#
# Created: Sat Oct 20 10:54:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DaisyMain(object):
    def setupUi(self, DaisyMain):
        DaisyMain.setObjectName(_fromUtf8("DaisyMain"))
        DaisyMain.resize(809, 781)
        DaisyMain.setWindowTitle(QtGui.QApplication.translate("DaisyMain", "Daisy-Creator", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(DaisyMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(640, 640, 111, 27))
        self.pushButton.setText(QtGui.QApplication.translate("DaisyMain", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEditFileCounter = QtGui.QLineEdit(self.tab)
        self.lineEditFileCounter.setGeometry(QtCore.QRect(24, 182, 610, 27))
        self.lineEditFileCounter.setText(QtGui.QApplication.translate("DaisyMain", "Counter-Datei waehlen", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFileCounter.setObjectName(_fromUtf8("lineEditFileCounter"))
        self.toolButtonCopyDest = QtGui.QToolButton(self.tab)
        self.toolButtonCopyDest.setGeometry(QtCore.QRect(640, 127, 24, 25))
        self.toolButtonCopyDest.setToolTip(QtGui.QApplication.translate("DaisyMain", "Zielverzeichnis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCopyDest.setText(QtGui.QApplication.translate("DaisyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCopyDest.setObjectName(_fromUtf8("toolButtonCopyDest"))
        self.label_1 = QtGui.QLabel(self.tab)
        self.label_1.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setText(QtGui.QApplication.translate("DaisyMain", "Daisy-Tool-Special", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.checkBoxCopyBhzIntro = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyBhzIntro.setGeometry(QtCore.QRect(332, 338, 301, 22))
        self.checkBoxCopyBhzIntro.setText(QtGui.QApplication.translate("DaisyMain", "Intro kopieren", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCopyBhzIntro.setObjectName(_fromUtf8("checkBoxCopyBhzIntro"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 248, 610, 17))
        self.label_4.setText(QtGui.QApplication.translate("DaisyMain", "Bhz und Ausgabe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.toolButtonCopySource = QtGui.QToolButton(self.tab)
        self.toolButtonCopySource.setGeometry(QtCore.QRect(640, 94, 24, 25))
        self.toolButtonCopySource.setToolTip(QtGui.QApplication.translate("DaisyMain", "Quellverzeichnis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCopySource.setText(QtGui.QApplication.translate("DaisyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCopySource.setObjectName(_fromUtf8("toolButtonCopySource"))
        self.toolButtonCopyFile1 = QtGui.QToolButton(self.tab)
        self.toolButtonCopyFile1.setGeometry(QtCore.QRect(640, 183, 24, 25))
        self.toolButtonCopyFile1.setText(QtGui.QApplication.translate("DaisyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCopyFile1.setObjectName(_fromUtf8("toolButtonCopyFile1"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(24, 443, 610, 191))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.checkBoxCopyBitrateChange = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyBitrateChange.setGeometry(QtCore.QRect(25, 368, 301, 22))
        self.checkBoxCopyBitrateChange.setText(QtGui.QApplication.translate("DaisyMain", "Bitrate anpassen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCopyBitrateChange.setObjectName(_fromUtf8("checkBoxCopyBitrateChange"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 159, 610, 17))
        self.label_6.setText(QtGui.QApplication.translate("DaisyMain", "Counter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEditCopyDest = QtGui.QLineEdit(self.tab)
        self.lineEditCopyDest.setGeometry(QtCore.QRect(24, 126, 610, 27))
        self.lineEditCopyDest.setText(QtGui.QApplication.translate("DaisyMain", "Ziel-Ordner", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCopyDest.setObjectName(_fromUtf8("lineEditCopyDest"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(24, 641, 610, 25))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.checkBoxCopyID3Change = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyID3Change.setEnabled(True)
        self.checkBoxCopyID3Change.setGeometry(QtCore.QRect(332, 368, 301, 22))
        self.checkBoxCopyID3Change.setText(QtGui.QApplication.translate("DaisyMain", "ID3-Tags entfernen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCopyID3Change.setObjectName(_fromUtf8("checkBoxCopyID3Change"))
        self.comboBoxCopyBhz = QtGui.QComboBox(self.tab)
        self.comboBoxCopyBhz.setGeometry(QtCore.QRect(24, 270, 610, 27))
        self.comboBoxCopyBhz.setObjectName(_fromUtf8("comboBoxCopyBhz"))
        self.checkBoxCopyBhzAusgAnsage = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyBhzAusgAnsage.setGeometry(QtCore.QRect(25, 338, 301, 22))
        self.checkBoxCopyBhzAusgAnsage.setText(QtGui.QApplication.translate("DaisyMain", "Ausgabe-Ansage kopieren", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCopyBhzAusgAnsage.setObjectName(_fromUtf8("checkBoxCopyBhzAusgAnsage"))
        self.lineEditCopySource = QtGui.QLineEdit(self.tab)
        self.lineEditCopySource.setGeometry(QtCore.QRect(24, 93, 610, 27))
        self.lineEditCopySource.setText(QtGui.QApplication.translate("DaisyMain", "Quell-Ordner", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCopySource.setObjectName(_fromUtf8("lineEditCopySource"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(640, 443, 111, 191))
        self.commandLinkButton.setText(QtGui.QApplication.translate("DaisyMain", "Kopieren", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.comboBoxCopyBhzAusg = QtGui.QComboBox(self.tab)
        self.comboBoxCopyBhzAusg.setGeometry(QtCore.QRect(24, 300, 610, 27))
        self.comboBoxCopyBhzAusg.setObjectName(_fromUtf8("comboBoxCopyBhzAusg"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 610, 17))
        self.label_2.setText(QtGui.QApplication.translate("DaisyMain", "Quelle und Ziel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 60, 790, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("DaisyMain", "Daisy-Metadaten-Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_3 = QtGui.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(0, 60, 790, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 610, 17))
        self.label_9.setText(QtGui.QApplication.translate("DaisyMain", "Quelldatei der Metadaten", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEditMetaSource = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaSource.setGeometry(QtCore.QRect(24, 93, 610, 27))
        self.lineEditMetaSource.setText(QtGui.QApplication.translate("DaisyMain", "Metadaten-Datei waehlen", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaSource.setObjectName(_fromUtf8("lineEditMetaSource"))
        self.toolButtonMetaFile = QtGui.QToolButton(self.tab_3)
        self.toolButtonMetaFile.setGeometry(QtCore.QRect(640, 93, 24, 25))
        self.toolButtonMetaFile.setText(QtGui.QApplication.translate("DaisyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonMetaFile.setObjectName(_fromUtf8("toolButtonMetaFile"))
        self.lineEditMetaProducer = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaProducer.setGeometry(QtCore.QRect(160, 150, 471, 27))
        self.lineEditMetaProducer.setText(QtGui.QApplication.translate("DaisyMain", "Produzent", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaProducer.setObjectName(_fromUtf8("lineEditMetaProducer"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(30, 155, 121, 17))
        self.label_10.setText(QtGui.QApplication.translate("DaisyMain", "Produzent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.commandLinkButtonMeta = QtGui.QCommandLinkButton(self.tab_3)
        self.commandLinkButtonMeta.setGeometry(QtCore.QRect(640, 150, 131, 261))
        self.commandLinkButtonMeta.setText(QtGui.QApplication.translate("DaisyMain", "Meta laden", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButtonMeta.setObjectName(_fromUtf8("commandLinkButtonMeta"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(30, 180, 121, 17))
        self.label_11.setText(QtGui.QApplication.translate("DaisyMain", "Autor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEditMetaAutor = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaAutor.setGeometry(QtCore.QRect(160, 180, 471, 27))
        self.lineEditMetaAutor.setText(QtGui.QApplication.translate("DaisyMain", "Autor", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaAutor.setObjectName(_fromUtf8("lineEditMetaAutor"))
        self.lineEditMetaTitle = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaTitle.setGeometry(QtCore.QRect(160, 210, 471, 27))
        self.lineEditMetaTitle.setText(QtGui.QApplication.translate("DaisyMain", "Titel", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaTitle.setObjectName(_fromUtf8("lineEditMetaTitle"))
        self.lineEditMetaEdition = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaEdition.setGeometry(QtCore.QRect(160, 240, 471, 27))
        self.lineEditMetaEdition.setText(QtGui.QApplication.translate("DaisyMain", "Edition", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaEdition.setObjectName(_fromUtf8("lineEditMetaEdition"))
        self.lineEditMetaNarrator = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaNarrator.setGeometry(QtCore.QRect(160, 270, 471, 27))
        self.lineEditMetaNarrator.setText(QtGui.QApplication.translate("DaisyMain", "Sprecher", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaNarrator.setObjectName(_fromUtf8("lineEditMetaNarrator"))
        self.lineEditMetaKeywords = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaKeywords.setGeometry(QtCore.QRect(160, 300, 471, 27))
        self.lineEditMetaKeywords.setText(QtGui.QApplication.translate("DaisyMain", "Stichworte", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaKeywords.setObjectName(_fromUtf8("lineEditMetaKeywords"))
        self.lineEditMetaRefOrig = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaRefOrig.setGeometry(QtCore.QRect(160, 330, 471, 27))
        self.lineEditMetaRefOrig.setText(QtGui.QApplication.translate("DaisyMain", "Ref-Original", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaRefOrig.setObjectName(_fromUtf8("lineEditMetaRefOrig"))
        self.lineEditMetaPublisher = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaPublisher.setGeometry(QtCore.QRect(160, 360, 471, 27))
        self.lineEditMetaPublisher.setText(QtGui.QApplication.translate("DaisyMain", "Verlag", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaPublisher.setObjectName(_fromUtf8("lineEditMetaPublisher"))
        self.lineEditMetaYear = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaYear.setGeometry(QtCore.QRect(160, 390, 471, 27))
        self.lineEditMetaYear.setText(QtGui.QApplication.translate("DaisyMain", "Erscheinungsjahr", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMetaYear.setObjectName(_fromUtf8("lineEditMetaYear"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(30, 210, 121, 17))
        self.label_15.setText(QtGui.QApplication.translate("DaisyMain", "Titel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(30, 240, 121, 17))
        self.label_16.setText(QtGui.QApplication.translate("DaisyMain", "Edition", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(30, 270, 121, 17))
        self.label_17.setText(QtGui.QApplication.translate("DaisyMain", "Sprecher", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(30, 300, 121, 17))
        self.label_18.setText(QtGui.QApplication.translate("DaisyMain", "Stichworte", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(30, 330, 121, 17))
        self.label_19.setText(QtGui.QApplication.translate("DaisyMain", "Ref-Original", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(30, 360, 121, 17))
        self.label_20.setText(QtGui.QApplication.translate("DaisyMain", "Verlag", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(30, 390, 121, 17))
        self.label_21.setText(QtGui.QApplication.translate("DaisyMain", "Erscheinungsjahr", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("DaisyMain", "Daisy-Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 833, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 610, 17))
        self.label_5.setText(QtGui.QApplication.translate("DaisyMain", "Quelle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.toolButtonDaisySource = QtGui.QToolButton(self.tab_2)
        self.toolButtonDaisySource.setGeometry(QtCore.QRect(640, 93, 24, 25))
        self.toolButtonDaisySource.setToolTip(QtGui.QApplication.translate("DaisyMain", "Quellverzeichnis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonDaisySource.setText(QtGui.QApplication.translate("DaisyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonDaisySource.setObjectName(_fromUtf8("toolButtonDaisySource"))
        self.lineEditDaisySource = QtGui.QLineEdit(self.tab_2)
        self.lineEditDaisySource.setGeometry(QtCore.QRect(24, 93, 610, 27))
        self.lineEditDaisySource.setText(QtGui.QApplication.translate("DaisyMain", "Quell-Ordner", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDaisySource.setObjectName(_fromUtf8("lineEditDaisySource"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 610, 17))
        self.label_7.setText(QtGui.QApplication.translate("DaisyMain", "Trenner für Autor und Titel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBoxDaisyTrenner = QtGui.QComboBox(self.tab_2)
        self.comboBoxDaisyTrenner.setGeometry(QtCore.QRect(24, 150, 610, 27))
        self.comboBoxDaisyTrenner.setObjectName(_fromUtf8("comboBoxDaisyTrenner"))
        self.textEditDaisy = QtGui.QTextEdit(self.tab_2)
        self.textEditDaisy.setGeometry(QtCore.QRect(20, 420, 610, 191))
        self.textEditDaisy.setObjectName(_fromUtf8("textEditDaisy"))
        self.commandLinkButtonDaisy = QtGui.QCommandLinkButton(self.tab_2)
        self.commandLinkButtonDaisy.setGeometry(QtCore.QRect(640, 420, 111, 191))
        self.commandLinkButtonDaisy.setText(QtGui.QApplication.translate("DaisyMain", "Daisyfizieren", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButtonDaisy.setObjectName(_fromUtf8("commandLinkButtonDaisy"))
        self.spinBoxEbenen = QtGui.QSpinBox(self.tab_2)
        self.spinBoxEbenen.setGeometry(QtCore.QRect(130, 250, 59, 27))
        self.spinBoxEbenen.setObjectName(_fromUtf8("spinBoxEbenen"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 250, 121, 21))
        self.label.setText(QtGui.QApplication.translate("DaisyMain", "Anzahl Ebenen", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBoxPages = QtGui.QSpinBox(self.tab_2)
        self.spinBoxPages.setGeometry(QtCore.QRect(360, 250, 59, 27))
        self.spinBoxPages.setObjectName(_fromUtf8("spinBoxPages"))
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(250, 250, 91, 21))
        self.label_14.setText(QtGui.QApplication.translate("DaisyMain", "Anzahl Seiten", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setText(QtGui.QApplication.translate("DaisyMain", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.line_4 = QtGui.QFrame(self.tab_4)
        self.line_4.setGeometry(QtCore.QRect(0, 60, 790, 3))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(20, 90, 610, 17))
        self.label_13.setText(QtGui.QApplication.translate("DaisyMain", "Datenrate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.comboBoxPrefBitrate = QtGui.QComboBox(self.tab_4)
        self.comboBoxPrefBitrate.setGeometry(QtCore.QRect(24, 120, 610, 27))
        self.comboBoxPrefBitrate.setObjectName(_fromUtf8("comboBoxPrefBitrate"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        DaisyMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DaisyMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DaisyMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DaisyMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DaisyMain.setStatusBar(self.statusbar)

        self.retranslateUi(DaisyMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DaisyMain)

    def retranslateUi(self, DaisyMain):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("DaisyMain", "1 Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("DaisyMain", "2 Meta", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("DaisyMain", "3 Daisy", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("DaisyMain", "Pref", None, QtGui.QApplication.UnicodeUTF8))


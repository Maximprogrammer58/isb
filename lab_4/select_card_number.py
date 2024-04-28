import sys

from card_number_functions import select_card_number, check_card_using_luna
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    """ Main window of the gui-program
        Methods:
            setupUi(MainWindow): creating widget objects
            retranslateUi(MainWindow): sets the text and headers of the widgets
            __warning_icon(text, info): pop-up message when an exception occurs
            __success_icon(text, info): pop-up message when the process is success
            load_bins(): downloading bins number from a file
            select_card_number(): selecting a bank card number
            check_card_number(): checking for the correctness of the bank card number
    """
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Creating widget objects in the appropriate containers
            Args:
                MainWindow: base window of the gui-program
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 919)
        self.bins = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_last_digit = QtWidgets.QLineEdit(self.centralwidget)
        self.input_last_digit.setGeometry(QtCore.QRect(40, 180, 251, 22))
        self.input_last_digit.setObjectName("input_last_digit")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(290, 380, 231, 21))
        self.input.setObjectName("input")
        self.input_hash = QtWidgets.QLineEdit(self.centralwidget)
        self.input_hash.setGeometry(QtCore.QRect(40, 120, 251, 22))
        self.input_hash.setObjectName("input_hash")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 10, 721, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.PlainText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.hash = QtWidgets.QLabel(self.centralwidget)
        self.hash.setGeometry(QtCore.QRect(40, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.hash.setFont(font)
        self.hash.setObjectName("hash")
        self.last_digit = QtWidgets.QLabel(self.centralwidget)
        self.last_digit.setGeometry(QtCore.QRect(40, 160, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.last_digit.setFont(font)
        self.last_digit.setObjectName("last_digit")
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(50, 300, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.selectButton.setFont(font)
        self.selectButton.setObjectName("selectButton")
        self.selectButton.clicked.connect(self.select_card_number)
        self.card_number = QtWidgets.QLabel(self.centralwidget)
        self.card_number.setGeometry(QtCore.QRect(40, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.card_number.setFont(font)
        self.card_number.setObjectName("card_number")
        self.bins = QtWidgets.QLabel(self.centralwidget)
        self.bins.setGeometry(QtCore.QRect(40, 220, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bins.setFont(font)
        self.bins.setObjectName("bins")
        self.titl_luna = QtWidgets.QLabel(self.centralwidget)
        self.titl_luna.setGeometry(QtCore.QRect(10, 520, 721, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titl_luna.setFont(font)
        self.titl_luna.setTextFormat(QtCore.Qt.PlainText)
        self.titl_luna.setAlignment(QtCore.Qt.AlignCenter)
        self.titl_luna.setObjectName("titl_luna")
        self.card_number_for_luna = QtWidgets.QLabel(self.centralwidget)
        self.card_number_for_luna.setGeometry(QtCore.QRect(30, 610, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.card_number_for_luna.setFont(font)
        self.card_number_for_luna.setObjectName("card_number_for_luna")
        self.input_for_luna = QtWidgets.QLineEdit(self.centralwidget)
        self.input_for_luna.setGeometry(QtCore.QRect(210, 620, 371, 21))
        self.input_for_luna.setObjectName("input_for_luna")
        self.correct_flag = QtWidgets.QLabel(self.centralwidget)
        self.correct_flag.setGeometry(QtCore.QRect(610, 610, 81, 41))
        self.correct_flag.setText("")
        self.correct_flag.setObjectName("correct_flag")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load_bins)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 670, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.raise_()
        self.pushButton_2.clicked.connect(self.check_card_number)
        self.input_last_digit.raise_()
        self.input.raise_()
        self.input_hash.raise_()
        self.title.raise_()
        self.hash.raise_()
        self.last_digit.raise_()
        self.selectButton.raise_()
        self.card_number.raise_()
        self.bins.raise_()
        self.titl_luna.raise_()
        self.card_number_for_luna.raise_()
        self.input_for_luna.raise_()
        self.correct_flag.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Sets the text and headers of the widgets
            Args:
                MainWindow: base window of the gui-program
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Selecting a bank card number by hash"))
        self.hash.setText(_translate("MainWindow", "Hash"))
        self.last_digit.setText(_translate("MainWindow", "Last 4 digit of bank card"))
        self.selectButton.setText(_translate("MainWindow", "Select"))
        self.card_number.setText(_translate("MainWindow", "Bank card number:"))
        self.bins.setText(_translate("MainWindow", "Download the list of bin numbers"))
        self.titl_luna.setText(_translate("MainWindow", "Checking the correctness of entering the card number"))
        self.card_number_for_luna.setText(_translate("MainWindow", "Bank card number:"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Check"))

    def __warning_icon(self, text: str, info: str) -> None:
        """A pop-up message when an exception occurs
            Args:
                text: the MessageBox header
                info: text of MessageBox
        """
        error = QtWidgets.QMessageBox()
        error.setIcon(QMessageBox.Warning)
        error.setWindowTitle(text)
        error.setText(info)
        error.exec_()

    def __success_icon(self, text: str, info: str) -> None:
        """A pop-up message when the process is completed successfully
            Args:
                text: the MessageBox header
                info: text of MessageBox
         """
        success = QtWidgets.QMessageBox()
        success.setWindowTitle(text)
        success.setText(info)
        success.exec_()

    def load_bins(self) -> None:
        """Downloading bins number from a file"""
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if path != '':
            try:
                with open(path, "r", encoding="utf-8") as file:
                    self.bins = file.read().split(", ")
            except Exception as e:
                self.__warning_icon("Error", f"Details{e}")
        else:
            self.__warning_icon("Warning", "The file is not selected")

    def select_card_number(self) -> None:
        """Selecting a bank card number"""
        hash = self.input_hash.text().strip()
        last_digit = self.input_last_digit.text()
        if hash and last_digit and self.bins:
            self.__warning_icon("Info", "The selection process has started")
            card_number = select_card_number(hash, self.bins, int(last_digit))
            self.__success_icon("Success", f"the card number has been selected: {card_number}")
            self.input.setText(card_number)
        else:
            self.__warning_icon("Warning", "Enter the data correctly")

    def check_card_number(self) -> None:
        """Checking for the correctness of the bank card number"""
        card_number = self.input_for_luna.text().strip()
        if card_number:
            is_card_number = check_card_using_luna(card_number)
            if is_card_number:
                self.correct_flag.resize(160, 40)
                self.correct_flag.setStyleSheet("color: green")
                self.correct_flag.setText("The card number is correct")
            else:
                self.correct_flag.resize(180, 40)
                self.correct_flag.setStyleSheet("color: red")
                self.correct_flag.setText("The card number is not correct")
        else:
            self.__warning_icon("Warning", "Enter the data correctly")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    print(type(MainWindow))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
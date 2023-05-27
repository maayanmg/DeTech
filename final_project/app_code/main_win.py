# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'appDate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import webbrowser
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QHeaderView
import detection_stats
import login1
import report_case
import results_win
import sendCurl
import sign_up1

class Ui_MainWindow(object):
    doctor_id = None
    selected_row = None
    def setupUi(self, MainWindow, client):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 690)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.about_btn = QtWidgets.QPushButton(self.centralwidget)
        self.about_btn.setGeometry(QtCore.QRect(690, 610, 161, 31))
        self.about_btn.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.about_btn.setDefault(False)
        self.about_btn.setFlat(False)
        self.about_btn.setObjectName("pushButton_6")
        self.books_img = QtWidgets.QLabel(self.centralwidget)
        self.books_img.setGeometry(QtCore.QRect(690, 60, 141, 91))
        self.books_img.setText("")
        self.books_img.setPixmap(QtGui.QPixmap("books.png"))
        self.books_img.setObjectName("label_12")
        self.report_a_visit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.report_a_visit_btn.hide()
        self.report_a_visit_btn.setGeometry(QtCore.QRect(690, 230, 161, 31))
        self.report_a_visit_btn.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.report_a_visit_btn.setDefault(False)
        self.report_a_visit_btn.setFlat(False)
        self.report_a_visit_btn.setObjectName("pushButton_5")
        self.x_ray_detection_btn = QtWidgets.QPushButton(self.centralwidget)
        self.x_ray_detection_btn.hide()
        self.x_ray_detection_btn.setGeometry(QtCore.QRect(690, 270, 161, 31))
        self.x_ray_detection_btn.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.x_ray_detection_btn.setDefault(False)
        self.x_ray_detection_btn.setFlat(False)
        self.x_ray_detection_btn.setObjectName("pushButton_7")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(690, 140, 161, 31))
        self.login_btn.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 16pt\n"
"")
        self.login_btn.setObjectName("pushButton")
        self.DeTech_text = QtWidgets.QLabel(self.centralwidget)
        self.DeTech_text.setGeometry(QtCore.QRect(230, 10, 211, 111))
        self.DeTech_text.setStyleSheet("color: rgb(14, 154, 175);\n"
"font-size: 42pt ")
        self.DeTech_text.setObjectName("label_2")
        self.logo_img = QtWidgets.QLabel(self.centralwidget)
        self.logo_img.setGeometry(QtCore.QRect(450, 20, 161, 91))
        self.logo_img.setText("")
        self.logo_img.setPixmap(QtGui.QPixmap("main_logo.png"))
        self.logo_img.setObjectName("label")
        self.slogan_text = QtWidgets.QLabel(self.centralwidget)
        self.slogan_text.setGeometry(QtCore.QRect(200, 110, 361, 31))
        self.slogan_text.setStyleSheet("color: rgb(0, 209, 255);\n"
"font-size: 20pt \n"
"")
        self.slogan_text.setObjectName("label_6")
        self.x_ray_img = QtWidgets.QLabel(self.centralwidget)
        self.x_ray_img.setGeometry(QtCore.QRect(30, 190, 461, 461))
        self.x_ray_img.setText("")
        self.x_ray_img.setPixmap(QtGui.QPixmap("x_ray.png"))
        self.x_ray_img.setObjectName("label_4")
        self.ai_img = QtWidgets.QLabel(self.centralwidget)
        self.ai_img.setGeometry(QtCore.QRect(400, 280, 421, 321))
        self.ai_img.setText("")
        self.ai_img.setPixmap(QtGui.QPixmap("ai_human.png"))
        self.ai_img.setObjectName("label_5")
        self.sign_up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_btn.setGeometry(QtCore.QRect(690, 180, 161, 31))
        self.sign_up_btn.setStyleSheet("\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(140, 140, 140);\n"
"font-size: 16pt\n"
"")
        self.sign_up_btn.setObjectName("pushButton_4")
        self.log_out_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_out_btn.setGeometry(QtCore.QRect(690, 190, 161, 31))
        self.log_out_btn.setStyleSheet("background-color: rgb(255, 84, 42);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-size: 16pt\n")
        self.log_out_btn.setObjectName("pushButton_2")
        self.log_out_btn.hide()
        self.user_text = QtWidgets.QLabel(self.centralwidget)
        self.user_text.setGeometry(QtCore.QRect(690, 150, 201, 31))
        self.user_text.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.user_text.setObjectName("user_text")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 190, 621, 451))
        self.tableWidget.setStyleSheet("background-color: rgb(197,197,197);\n"
                                       "color: rgb(42, 42, 42);\n"
                                       "font-size: 12pt")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.resizeColumnsToContents()
        self.ai_img.raise_()
        self.books_img.raise_()
        self.DeTech_text.raise_()
        self.logo_img.raise_()
        self.slogan_text.raise_()
        self.x_ray_img.raise_()
        self.report_a_visit_btn.raise_()
        self.x_ray_detection_btn.raise_()
        self.sign_up_btn.raise_()
        self.user_text.raise_()
        self.user_text.hide()
        self.about_btn.raise_()
        self.login_btn.raise_()
        self.tableWidget.raise_()
        self.tableWidget.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("background-color: rgb(255, 255, 255); color:white")
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setToolTipsVisible(False)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.detection_stats_btn = QtWidgets.QPushButton(self.centralwidget)
        self.detection_stats_btn.hide()
        self.detection_stats_btn.setGeometry(QtCore.QRect(690, 310, 161, 31))
        self.detection_stats_btn.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                        "color: rgb(255,255,255);\n"
                                        "font-size: 14pt\n"
                                        "")
        self.detection_stats_btn.setDefault(False)
        self.detection_stats_btn.setFlat(False)
        self.detection_stats_btn.setObjectName("pushButton_8")
        self.ai_img.raise_()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.login_btn.clicked.connect(lambda: self.open_login_Dialog(client))
        self.sign_up_btn.clicked.connect(lambda: self.open_sign_up_Dialog(client))
        self.x_ray_detection_btn.clicked.connect(lambda: self.select_photo_and_send_curl())
        self.report_a_visit_btn.clicked.connect(lambda: self.open_report_a_visit_Dialog(client))
        self.tableWidget.selectionModel().selectionChanged.connect(self.selected_row)
        self.tableWidget.doubleClicked.connect(lambda: self.watch_patient_datails(client))
        self.log_out_btn.clicked.connect(lambda: self.sign_out())
        self.about_btn.clicked.connect(lambda: self.open_project_book())
        self.detection_stats_btn.clicked.connect(lambda: self.open_statistical_analysis_Dialog(client))

    #The function opens the project book from a url.
    def open_project_book(self):
        webbrowser.open("https://docs.google.com/document/d/1xoxYSfxPT1LbkVRRw4hjJANpfWASCB1bWV0eGYCthco/edit?usp=sharing")

    #A function that always updates the row in the table that is selected
    def selected_row(self, selected):
        for ix in selected.indexes():
            self.selected_row = ix.row()

    def watch_patient_datails(self, client):
        patient_id = self.tableWidget.item(self.selected_row, 1).text()
        self.dialog = QtWidgets.QDialog()
        self.ui = report_case.Ui_Report_a_visit()
        self.ui.setupUi(self.dialog, client, self, self.doctor_id)
        self.ui.turn_into_show_patient_mode(client, patient_id)
        self.dialog.show()

    #A function that receives a client. The function opens the login dialog
    def open_login_Dialog(self, client):
        self.dialog = QtWidgets.QDialog()
        self.ui = login1.Ui_Login()
        self.ui.setupUi(self.dialog, client, self)
        self.dialog.show()

    #A function that receives a client. The function opens the sign up dialog
    def open_sign_up_Dialog(self, client):
        self.dialog = QtWidgets.QDialog()
        self.ui = sign_up1.Ui_Sign_up()
        self.ui.setupUi(self.dialog, client, self)
        self.dialog.show()

    #A function that receives the username and its unique id. The function changes the view of the main window. It turns it into a screen that shows the personal area of the logged in user
    def turn_into_logged_in_mode(self, username, doctor_id):
        _translate = QtCore.QCoreApplication.translate
        self.login_btn.hide()
        self.sign_up_btn.hide()
        self.x_ray_img.hide()
        self.ai_img.hide()
        self.user_text.show()
        self.user_text.setText(_translate("MainWindow", "Hello " + username + ","))
        self.x_ray_detection_btn.show()
        self.detection_stats_btn.show()
        self.report_a_visit_btn.show()
        self.doctor_id = doctor_id
        self.tableWidget.show()
        self.log_out_btn.show()

    #A function that receives a client. The function gets the patient list from the server and fills the table of patients
    def fill_table(self, client):
        self.clear_table()
        self.tableWidget.setSortingEnabled(False)
        patient_list = client.get_patients_list(self.doctor_id)
        if patient_list is None:
            return
        table = self.tableWidget
        for row in patient_list:
            try:
                row = row.split('#')
                table.insertRow(table.rowCount())
                rowCount = table.rowCount()
                columnCount = table.columnCount()
                for j in range(columnCount-1):
                    table.setItem(rowCount - 1, j, QtWidgets.QTableWidgetItem(row[j]))
                age = self.calculate_age(row[4])
                table.setItem(rowCount - 1, 3, QtWidgets.QTableWidgetItem(str(age)))
            except:
                pass
        self.tableWidget.setSortingEnabled(True)

    #A function that cleat the table widget. Row number becomes 0 and contents are empty.
    def clear_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    #A function that receives birth date and calculate the age of the person. Returns the age.
    def calculate_age(self, birth_date):
        today = date.today()
        spllited_birth_date = birth_date.split('-')
        age = today.year - int(spllited_birth_date[0]) -((today.month, today.day) <(int(spllited_birth_date[1]), int(spllited_birth_date[2])))
        return age

    #A function that ask the user to choose x-ray photo from the computer(using another fumction) and then the function sends it to the web server. In the end (if everything went well) the function open the results Dialog with the detection of the x-ray (using another function).
    def select_photo_and_send_curl(self):
        photo_path = self.get_file_name()
        if photo_path == '':
            return
        try:
            chance = sendCurl.send_curl(photo_path)
            if chance != '':
                split_chance = chance.split()
                is_pneu = True
                if split_chance[0] == 'normal':
                    is_pneu = False
                self.open_results_Dialog(is_pneu)
        except:
            None

    # A function that ask the user to choose x-ray photo from the computer. The function allows only 'jpeg' files. The function returns the file location.
    def get_file_name(self):
        file_filter = 'Data File (*.jpeg)'
        response = QFileDialog.getOpenFileName(
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='jpeg File (*.jpeg)'
        )
        print(response)
        return response[0]

    # A function that receives a client and a detection of an x-ray. The function opens the results dialog in accordance to the detection.
    def open_results_Dialog(self, is_pneu):
        self.dialog = QtWidgets.QDialog()
        self.ui = results_win.Ui_results_win()
        self.ui.setupUi(self.dialog)
        self.ui.turn(is_pneu, "x_ray")
        self.dialog.show()

    #A function that receives a client. The function opens the report_a_visit dialog
    def open_report_a_visit_Dialog(self, client):
        self.dialog = QtWidgets.QDialog()
        self.ui = report_case.Ui_Report_a_visit()
        self.ui.setupUi(self.dialog, client, self, self.doctor_id)
        self.dialog.show()

    #A function that chnage the display to the design of home page. The user exits the personal area
    def sign_out(self):
        self.login_btn.show()
        self.sign_up_btn.show()
        self.x_ray_img.show()
        self.ai_img.show()
        self.user_text.hide()
        self.x_ray_detection_btn.hide()
        self.detection_stats_btn.hide()
        self.report_a_visit_btn.hide()
        self.doctor_id = None
        self.clear_table()
        self.tableWidget.hide()
        self.log_out_btn.hide()

    # A function that receives a client. The function opens the statistical_analysis Dialog.
    def open_statistical_analysis_Dialog(self, client):
        self.dialog = QtWidgets.QDialog()
        self.ui = detection_stats.Ui_statistical_analysis()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
        self.ui.fill_stats_table("x_ray_stats", client, self.dialog, self.doctor_id)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DeTech", "DeTech"))
        self.about_btn.setText(_translate("MainWindow", "about DeTech"))
        self.report_a_visit_btn.setText(_translate("MainWindow", "report a visit"))
        self.x_ray_detection_btn.setText(_translate("MainWindow", "X-ray detection"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.DeTech_text.setText(_translate("MainWindow", "DeTech"))
        self.slogan_text.setText(_translate("MainWindow", "Pneumonia detection using AI"))
        self.sign_up_btn.setText(_translate("MainWindow", "Sign up"))
        self.user_text.setText(_translate("MainWindow", "Hello "))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "patient name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "age"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.log_out_btn.setText(_translate("MainWindow", "Log out"))
        self.detection_stats_btn.setText(_translate("MainWindow", "Statistical analysis"))


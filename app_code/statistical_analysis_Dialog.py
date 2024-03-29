# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Statistical_analysis_Dialog(object):
    # A function that receives a Dialog. The function builds the dialog with its details
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 705)
        Dialog.setFixedSize(640, 705)
        Dialog.setModal(True)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 531, 461))
        self.tableWidget.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.heading_text = QtWidgets.QLabel(Dialog)
        self.heading_text.setGeometry(QtCore.QRect(20, 20, 331, 71))
        self.heading_text.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.heading_text.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 571, 131))
        self.textEdit.setStyleSheet("color: rgb(255,255,255);\n"
                                      "font-size: 15pt")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # A function that receives directory_path, client, dialog, doctor_id. The function fills a table with x-ray images and it's results.
    def fill_stats_table(self, directory_path, client, dialog, doctor_id):
        count = 0
        patient_list = client.get_patients_list(doctor_id)
        if patient_list is None:
            return
        for filename in os.listdir(directory_path):
            image_label = QtWidgets.QLabel(dialog)
            image_label.setText("")
            image_label.setScaledContents(True)
            pixmap = QtGui.QPixmap()
            # Convert digital data to binary format
            photo_path = os.path.join(directory_path, filename)
            with open(photo_path, 'rb') as file:
                binaryData = file.read()
            pixmap.loadFromData(binaryData, 'jpeg')
            image_label.setPixmap(pixmap)
            item = image_label
            filename = filename.split('.')
            for row in patient_list:
                row = row.split('#')
                if row[1] == filename[0]:
                    results = row[8]
                    if results == 'None':
                        continue
                    results = results.split(' ')
                    self.tableWidget.insertRow(self.tableWidget.rowCount())
                    self.tableWidget.setCellWidget(count, 0, item)
                    self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(results[0]))
                    self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(results[2]))
                    count += 1
                    break
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setText(_translate("Dialog", "Below are presented some statistical data regarding the x-rays you uploaded to the system.\r\nX-rays uploaded: " + str(self.tableWidget.rowCount()) + "\r\nX-rays that were detected as pneumonia: " + self.count_pneu_among_table()+ "\r\nOverall accuracy: " +self.check_accuracy()))

    # A function that counts the number of x-rays that were detected as pneumonia
    def count_pneu_among_table(self):
        count = 0
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 1).text() == 'Pneumonia':
                count += 1
        return str(count)

    # A function that calculates the average accuracy of detection.
    def check_accuracy(self):
        sum = 0
        for row in range(self.tableWidget.rowCount()):
            result = self.tableWidget.item(row, 2).text()
            result = result[:-1]
            sum += float(result)
        if self.tableWidget.rowCount() != 0:
            sret = str(sum/self.tableWidget.rowCount())
        else:
            sret = str(0)
        return sret[:4] + "%"

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "X-ray"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Detection"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Accuracy"))
        self.heading_text.setText(_translate("Dialog", "Statistical analysis:"))
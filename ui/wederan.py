# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Website Design Ranker.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request as req
from bs4 import BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup
REGEX_CSS = re.compile(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})')
f = open("result.txt", "a")
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.url_input_label = QtWidgets.QLabel(Dialog)
        self.url_input_label.setGeometry(QtCore.QRect(50, 230, 101, 21))
        self.url_input_label.setObjectName("url_input_label")
        self.rank_display = QtWidgets.QTextBrowser(Dialog)
        self.rank_display.setGeometry(QtCore.QRect(50, 370, 701, 151))
        self.rank_display.setObjectName("rank_display")
        self.rank_button = QtWidgets.QPushButton(Dialog)
        self.rank_button.setGeometry(QtCore.QRect(40, 540, 711, 25))
        self.rank_button.setObjectName("rank_button")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(100, 140, 200, 20))
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 340, 48, 14))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 210, 601, 70))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

     # creating connection
        self.rank_button.clicked.connect(self.run_command)

    def run_command(self):
        global num_of_line
        num_of_line=0
        rank = [['',''] for _ in range(num_of_line)]
        total_count = 0
        txt = str(self.plainTextEdit.toPlainText())
        #print(txt)
        #self.textEdit.insertPlainText(str(out, "utf-8"))
        #Parse through example CSS files and find the regex of colour codes. Then count all the colour codes and set it as a variable.
        count = 0
        #with open(txt) as fp:
        num_of_line = len(txt.splitlines())
        for line in txt.splitlines():
            try:
                print(line)
                url = line
                #length = len(line.splitlines())
                #print(length)
                html = req.urlopen(line) # request the initial page
                soup = BeautifulSoup(html, 'html.parser')
                for styles in soup.select('style'): # get in-page style tags
                    try:
                        regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
                        result = re.findall(regex, styles.string)
                        #print((set(result)))
                        #print(len(set(result)))
                    except:
                        print("Error in ins")
                        pass
                    count = count + len(set(result))
                for link in soup.find_all('link', type='text/css'): # get links to external style sheets
                    try:
                        address = link['href'] # the address of the stylesheet
                        #if address.startswith('/'): # relative link
                        add = url + address
                        #print(add)
                        css = req.urlopen(add).read() # make a request to download the stylesheet from the address
                        #print(css)
                        regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
                        result = re.findall(regex, css.decode('utf-8'))
                        #print((set(result)))
                        #print(len(set(result)))
                        count = count + len(set(result))
                    except:
                        #print("Error")
                        pass
                #rank[][0]=""
                #f.write(url,"--number of colorcode--",result)

            except:
                #print("Error")
                pass
            print(count)
            total_count = total_count + count
            print (total_count)   
            count = 0
        avg_value = total_count/num_of_line
        print(avg_value)   
            
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.url_input_label.setText(_translate("Dialog", "Input URL :"))
        self.rank_button.setText(_translate("Dialog", "Rank"))
        self.label1.setText(_translate("Dialog", "Website Design Ranking"))
        self.label.setText(_translate("Dialog", "Output :"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

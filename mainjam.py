# Import the necessary PyQt5 modules
from PyQt5 import QtCore, QtGui, QtWidgets

# Define the Ui_Form class
class Ui_Form(object):
    def setupUi(self, Form):
        # Set up the main form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        
        # Set up the time edit widget
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(140, 60, 121, 22))
        self.timeEdit.setObjectName("timeEdit")
        
        # Set up the labels
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 210, 47, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 210, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 210, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(290, 210, 81, 16))
        self.label_4.setObjectName("label_4")
        
        # Set up the date edit widget
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(140, 90, 121, 22))
        self.dateEdit.setObjectName("dateEdit")
        
        # Set up the push button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 21, 21))
        self.pushButton.setObjectName("pushButton")
        
        # Set up the tool button
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(260, 20, 31, 16))
        self.toolButton.setObjectName("toolButton")

        # Set the text for the widgets
        self.retranslateUi(Form)
        
        # Connect the slots and signals
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        # Set the window title
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        # Set the text for the labels
        self.label.setText(_translate("Form", "Alarm"))
        self.label_2.setText(_translate("Form", "Jam Dunia"))
        self.label_3.setText(_translate("Form", "Stopwatch"))
        self.label_4.setText(_translate("Form", "Pengatur Waktu"))
        
        # Set the text for the buttons
        self.pushButton.setText(_translate("Form", "+"))
        self.toolButton.setText(_translate("Form", "..."))

# Main function to run the application
if __name__ == "__main__":
    import sys
    # Create the application object
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the main form (window) object
    Form = QtWidgets.QWidget()
    
    # Create an instance of the UI class and set up the UI
    ui = Ui_Form()
    ui.setupUi(Form)
    
    # Show the main form
    Form.show()
    
    # Execute the application and exit
    sys.exit(app.exec_())

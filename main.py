#Author: S.ABILASH
#CopyRight (c) 2021 All Rights Reserved

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QMainWindow,QAction,QMenu,QPushButton,QLineEdit,QMessageBox
from PyQt5 import QtGui
import keyboard as key
import os
import threading



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.setWindowTitle("BlogPad ~S.ABILASH")
        self.setWindowIcon(QtGui.QIcon("notepad.png"))
        self.resize(750,450)
        self.blog_file_name ="Untitled.txt"
        self.render()
        self.statusBar()
        self.show()

    def render(self):
        self.user_text_area = QTextEdit(self)
        self.user_text_area.setStyleSheet("color:black;font-size:16px;font-family:SansSerif;font-weight:bold")
        self.user_text_area.setPlaceholderText("Blog Here...")
        self.user_text_area.resize(1360,740)
        self.user_text_area.move(0,-1)

        #Status Bar
        self.statusBar().showMessage(self.blog_file_name)
        self.statusBar().setStyleSheet("background-color:purple;color:white;font-family:monospace")
        
        #New Button
        self.blog_new_file = QPushButton("New",self)
        self.blog_new_file.setStyleSheet("font-family:monospace;font-size:12px;")
        self.blog_new_file.clicked.connect(self.create_new_file)
        self.statusBar().addPermanentWidget(self.blog_new_file)

        #Open Button
        self.blog_open_file = QPushButton("Open",self)
        self.blog_open_file.setStyleSheet("font-family:monospace;font-size:12px")
        self.blog_open_file.clicked.connect(self.open_blog_file)
        self.statusBar().addPermanentWidget(self.blog_open_file)

        #Save Button
        self.blog_save_file = QPushButton("Save",self)
        self.blog_save_file.setStyleSheet("font-family:monospace;font-size:12px;")
        self.blog_save_file.clicked.connect(self.save_blog_file)
        self.statusBar().addPermanentWidget(self.blog_save_file)

        #View Button
        self.blog_view_file = QPushButton("View",self)
        self.blog_view_file.setStyleSheet("font-family:monospace;font-size:12px;")
        self.blog_view_file.clicked.connect(self.view_blog_file)
        self.statusBar().addPermanentWidget(self.blog_view_file)


        #Clear Button
        self.blog_clear_file = QPushButton("Clear",self)
        self.blog_clear_file.setStyleSheet("font-family:monospace;font-size:12px")
        self.blog_clear_file.clicked.connect(self.clear_blog_file)
        self.statusBar().addPermanentWidget(self.blog_clear_file)
    

    #Event Action
    def view_blog_file(self):
        self.write_everything()
    def clear_blog_file(self):
        self.user_text_area.clear()
    def save_blog_file(self):
        try:
            file = open(os.getcwd()+"\\"+self.blog_file_name,"w")
            file.write(self.user_text_area.toPlainText())

            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText("File Saved Successfully!!")
            message.setWindowTitle("BlogPad")
            message.setWindowIcon(QtGui.QIcon("notepad.png"))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
        except:
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText("An Error Occurred While Saving The File")
            message.setWindowTitle("BlogPad")
            message.setWindowIcon(QtGui.QIcon("notepad.png"))
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
    
    def open_blog_file(self):
        self.omessage_box = OpenTextBox()
        self.omessage_box.show()
        self.thread1 = threading.Thread(target= self.check_oname)
        self.thread1.start()

    def create_new_file(self):
            self.message_box = NewTextBox()
            self.message_box.show()
            thread = threading.Thread(target= self.check_name)
            thread.start()          

    def write_everything(self):
        try:
            file = open(self.blog_file_name,"r")
            content=""
            line = file.readlines()
            for i in line:
                content +=i.strip()+"\n"
            self.user_text_area.setPlainText(content)
        except:
            pass
    
    def check_oname(self):
        while(True):
            if(self.omessage_box.isVisible() == False):
                self.blog_file_name = self.omessage_box.new_name
                self.statusBar().showMessage(self.blog_file_name)
                break


    def check_name(self):
        while(True):
            if(self.message_box.isVisible() == False):
                self.blog_file_name = self.message_box.new_name
                self.statusBar().showMessage(self.blog_file_name)
                break


class OpenTextBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BlogPad - OpenFile")
        self.setWindowIcon(QtGui.QIcon("notepad.png"))
        self.resize(280,80)
        self.new_name = "Untitled.txt"
        self.render()
        self.show()
    
    def render(self):
        self.text_box = QLineEdit(self)
        self.text_box.resize(280,40)
        self.text_box.setText("Untitled.txt")
        self.text_box.setStyleSheet("font-size:14px;font-family:SansSerif;font-weight:bold")
        
        #Open Button
        self.open_button = QPushButton("Open",self)
        self.open_button.move(95,40)
        self.open_button.clicked.connect(self.open_file)

    def open_file(self):
        get_file_name = self.text_box.text()
        if(get_file_name.find(":")):
            if(os.path.exists(get_file_name)== True):
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setText("File Opened Successfully!!\nClick View")
                message.setWindowTitle("BlogPad")
                message.setWindowIcon(QtGui.QIcon("notepad.png"))
                message.setStandardButtons(QMessageBox.Ok)
                message.exec_()
                self.new_name = get_file_name

            else:
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setText("No Such File Exist!!")
                message.setWindowTitle("BlogPad")
                message.setWindowIcon(QtGui.QIcon("notepad.png"))
                message.setStandardButtons(QMessageBox.Ok)
                message.exec_() 
        else:
            if(os.path.exists(os.getcwd()+"\\"+get_file_name) == True):
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setText("File Opened Successfully!!\n Click View")
                message.setWindowTitle("BlogPad")
                message.setStandardButtons(QMessageBox.Ok)
                message.exec_()
            else:
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setText("No Such File Exist")
                message.setWindowTitle("BlogPad")
                message.setStandardButtons(QMessageBox.Ok)
                message.exec_()
        self.close()



class NewTextBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BlogPad - NewFile")
        self.setWindowIcon(QtGui.QIcon("notepad.png"))
        self.resize(280,80)
        self.new_name = "Untitled.txt"
        self.render()
        self.show()

    def render(self):
        self.text_box = QLineEdit(self)
        self.text_box.resize(280,40)
        self.text_box.setText("Untitled.txt")
        self.text_box.setStyleSheet("font-size:14px;font-family:SansSerif;font-weight:bold")

        #Create Button
        self.create_button = QPushButton("Create",self)
        self.create_button.move(95,40)
        self.create_button.clicked.connect(self.new_file)

    def new_file(self):
        self.new_name = self.text_box.text()
        self.close()
        


#driver Code
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    if(len(sys.argv)==2):
        ex = App()
        ex.blog_file_name= sys.argv[1]
        ex.write_everything()
        ex.statusBar().showMessage(sys.argv[1])
        sys.exit(app.exec_())
    elif(len(sys.argv)==1):
        ex = App()
        sys.exit(app.exec_())
    else:
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText("Too Much Files To Be Handled!!")
        message.setWindowTitle("BlogPad")
        message.setWindowIcon(QtGui.QIcon("notepad.png"))
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()
        


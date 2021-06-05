#%%
import sys
from chatmodule import Message
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QListWidget
import time
from threading import Thread


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.msg = Message()

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        
        self.btn_send = QPushButton("Send")
        self.list = QListWidget()
        
        self.edit_sender = QLineEdit()
        self.edit_message = QLineEdit()
        self.edit_sender.setPlaceholderText("Enter your name...")
        self.edit_message.setPlaceholderText("Message...")

        self.h_box.addWidget(self.edit_message)
        self.h_box.addWidget(self.btn_send)

        self.v_box.addWidget(self.edit_sender)
        self.v_box.addWidget(self.list)
        self.v_box.addLayout(self.h_box)

        self.btn_send.clicked.connect(self.send_message)
        Thread(target=self.get_all_messages).start()
        self.setLayout(self.v_box)
        

    def send_message(self):
        sender = self.edit_sender.text()
        text = self.edit_message.text()
        self.msg.send(text, sender)
        self.edit_message.clear()
        

    def get_all_messages(self):
        while 1:
            time.sleep(0.5)
            messages = self.msg.receive()
            self.list.clear()
            for item in messages:
                self.list.addItem(f"%-10s | %12s | %s" % (item.get("time"), item.get("sender"), item.get("message")))

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()

# %%

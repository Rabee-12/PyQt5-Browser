import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction("BACK", self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        Forward_button = QAction("Forward", self)
        Forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_button)

        reload_Button = QAction("reload", self)
        reload_Button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_Button)

        home_Button = QAction("Home", self)
        home_Button.triggered.connect(self.navigate_home)
        navbar.addAction(home_Button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))


    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())




app = QApplication(sys.argv)
QApplication.setApplicationName("rabee browser")
window = MainWindow()
app.exec_()

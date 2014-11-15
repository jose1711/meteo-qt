#!/usr/bin/env python3


from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AboutDialog(QDialog):
    def __init__(self, title, text, image, contributors, parent=None):
        super(AboutDialog, self).__init__(parent)
        layout = QVBoxLayout()
        titleLayout = QHBoxLayout()
        name_versionLabel = QLabel(title)
        contentsLayout = QHBoxLayout()
        aboutBrowser = QTextBrowser()
        aboutBrowser.append(text)
        aboutBrowser.setOpenExternalLinks(True)
        creditsBrowser = QTextBrowser()
        creditsBrowser.append(contributors)
        creditsBrowser.setOpenExternalLinks(True)
        TabWidget = QTabWidget()
        TabWidget.addTab(aboutBrowser, self.tr('About'))
        TabWidget.addTab(creditsBrowser, self.tr('Contributors'))
        creditsBrowser.moveCursor(QTextCursor.Start)
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap(image))
        titleLayout.addWidget(imageLabel)
        titleLayout.addWidget(name_versionLabel)
        titleLayout.addStretch()
        contentsLayout.addWidget(TabWidget)
        buttonLayout = QHBoxLayout()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonLayout.addWidget(buttonBox)
        layout.addLayout(titleLayout)
        layout.addLayout(contentsLayout)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

        buttonBox.clicked.connect(self.accept)
        #creditsButton.clicked.connect(self.show_credits)

        self.setMinimumSize(QSize(350, 400))
        #self.setMaximumSize(QSize(400, 440))
        self.setWindowTitle(self.tr('About Meteo-qt'))
